import http.server
import threading
import urllib.parse
import json

import base_web_server_route_url_management # base_web_server_route_url_management.py

class NewRouteError (Exception): pass

class NoRoutesDefinedError (Exception): pass

class BaseWebServer:
    def __init__ (self, host = "0.0.0.0", port = 5000, server_class = http.server.ThreadingHTTPServer, logging_enabled = True):
        self.logging_enabled = logging_enabled
        self.routes = {}
        def request_handler_generator (*request_handler_args, **request_handler_kwargs):
            return RequestHandler ( # Instantiates a new instance of the request handler,
                *request_handler_args, # passing through any arguments created by the HTTP server class,
                web_server_reference = self, # adding our own custom keyword argument that contains a reference to this web server,
                **request_handler_kwargs # and passing through any keyword arguments created by the HTTP server class.
            )
        self.httpd = server_class ((host, port), request_handler_generator)
    def route (self, route_url, overwrite = False, priority = False, pass_reference_to_request_handler = False): # Generates a function that gets passed a URL handler. Handy for @app.route (url)
        def route_generator (handler_func):
            if route_url in self.routes and not overwrite:
                raise NewRouteError (f"Duplicate route: {route_url}, set overwrite in the decorator to overwrite")
            parsed_route_url = base_web_server_route_url_management.RouteURLParser.parse_route_url (route_url = route_url)
            self.routes [route_url] = {"parsed_route_url": parsed_route_url, "handler_func": handler_func, "priority": priority, "pass_reference_to_request_handler": pass_reference_to_request_handler}
        return route_generator
    def run (self, threaded = False, daemon = True):
        if threaded:
            self._run_thread = threading.Thread (target = self.httpd.serve_forever, daemon = daemon)
            self._run_thread.start ()
        else:
            self.httpd.serve_forever ()
    def shutdown (self, threaded = False, daemon = True):
        if threaded:
            self._shut_down_thread = threading.Thread (target = self.httpd.shutdown, daemon = daemon)
            self._shut_down_thread.start ()
        else:
            self.httpd.shutdown ()

class RequestHandler (http.server.BaseHTTPRequestHandler):
    def __init__ (self, *request_handler_args, web_server_reference, **request_handler_kwargs):
        self.web_server_reference = web_server_reference # Stores a reference to the web server on this object instance.
        # Passes through all arguments and keyword arguments created by the HTTP server class to the call to super ().__init__,
        # which instantiates BaseHTTPRequestHandler using those arguments and keyword arguments.
        super (RequestHandler, self).__init__ (*request_handler_args, **request_handler_kwargs)
    def _handle (self, *, method_name):
        # Do route matching and call the appropriate function
        route_matched = False
        route_list = list ((route_url, route_info) for route_url, route_info in self.web_server_reference.routes.items ())
        # Sort the route list so that the routes marked as priority are handled first
        route_list.sort (
            reverse = True, # Allows routes with priority marked as True (with a sort value of 1) to be forced to the front, with lower list indices
            key = lambda route_tuple: int (route_tuple [1] ["priority"]) # Returns 1 if priority, 0 if not
        )
        path_with_query_string = self.path
        if '?' in path_with_query_string: # Path has a query string
            split_path = path_with_query_string.split ('?')
            path = '?'.join (split_path [:-1])
            self.query_string = split_path [-1]
            parsed_query_string_variables = {}
            query_string_segments = self.query_string.split ('&')
            for query_string_segment in query_string_segments:
                if query_string_segment == '': continue
                variable_name_and_value = query_string_segment.split ('=')
                if len (variable_name_and_value) != 2: continue
                variable_name, variable_value = variable_name_and_value
                variable_value = urllib.parse.unquote (variable_value) # Replaces "%20" with ' ', etc.
                parsed_query_string_variables [variable_name] = variable_value
            self.args = parsed_query_string_variables
        else: # Path doesn't have a query string
            path = path_with_query_string
            self.args = {}
        for route_url, route_info in route_list:
            match_success, url_variables = base_web_server_route_url_management.URLMatcher.check_url_against_parsed_route_url (url = path, parsed_route_url = route_info ["parsed_route_url"])
            if match_success:
                route_matched = True
                break
        if not route_matched:
            self.send_error (404)
        else:
            if route_info ["pass_reference_to_request_handler"]:
                handler_func_args = [self]
            else:
                handler_func_args = []
            response = route_info ["handler_func"] (*handler_func_args, **url_variables)
            if response is not None:
                response._apply_to (self)
                response._after_completion ()
    def log_message (self, format, *args):
        message = format % args
        if self.web_server_reference.logging_enabled:
            sys.stderr.write (message.encode ())

class ResponseCreationError (Exception): pass

class Response:
    def __init__ (self, *, response_code = 200, headers = {}, body = b"", from_code = False, after_completion_func = None):
        if not from_code:
            raise ResponseCreationError ("__init__ should only be called internally! Call one of the init_with functions instead.")
        self.response_code = response_code
        self.headers = headers
        self.body = body
        self.after_completion_func = after_completion_func
    def _apply_to (self, request_handler):
        request_handler.send_response (self.response_code)
        for header_name, header_value in self.headers.items ():
            request_handler.send_header (header_name, header_value)
        request_handler.send_header ("Content-Length", str (len (self.body)))
        request_handler.end_headers ()
        request_handler.wfile.write (self.body)
        request_handler.wfile.write (b"\r\n\r\n") # Finalizes the response. The client should close the connection after receiving this.
    def _after_completion (self): # This should be called after the response is applied to a request handler.
        if self.after_completion_func is not None:
            self.after_completion_func ()
    @staticmethod
    def init_with_text (*, text, content_type = "text/plain; charset=UTF-8", **kwargs):
        return Response (
            headers = {"Content-Type": content_type},
            body = text.encode (),
            from_code = True,
            **kwargs
        )
    @staticmethod
    def init_with_json (*, data, **kwargs):
        data_as_json = json.dumps (data)
        return Response.init_with_text (text = data_as_json, content_type = "application/json; charset=UTF-8", **kwargs)

# Add functions to RequestHandler for each method name based on a list of method names
# (HTTPServer finds the function to call based on the HTTP method, so we need a function for each HTTP method for maximum compatibility.)
method_names = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]
for method_name in method_names:
    setattr (RequestHandler, f"do_{method_name}", lambda self, method_name = method_name: self._handle (method_name = method_name))

if __name__ == "__main__":
    # Since the script was run from the command line, run a test
    server = BaseWebServer ()
    @server.route ("/<string:input_string>")
    def root (request_handler, input_string):
        response_text = f"Success! You said '{input_string}'."
        return Response.init_with_text (text = response_text)
    @server.route ("/shutdown", priority = True) # Setting priority forces this route to be checked before non-priority routes (e.g. root)
    def shutdown (request_handler):
        # after_completion_func allows us to provide a function to be called once the request completes.
        # This is especially useful in situations such as this one,
        # where trying to shut down the server before the request completes would cause the shut down operation to wait for the request to complete,
        # creating a deadlock.
        return Response.init_with_text (text = "Shutting down...", after_completion_func = server.shutdown)
    print ("Running the server")
    server.run ()
    print ("Done")
