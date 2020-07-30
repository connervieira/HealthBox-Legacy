import utils, base_web_server, metrics # utils.py, base_web_server.py, metrics.py

import json
import http.server

class HealthBoxWebServer:
    def __init__ (self, *, terminal_wrapper, host = "0.0.0.0", port = 5050):
        # Copy parameters into the object scope.
        self.terminal_wrapper = terminal_wrapper # A reference to a HealthBoxTerminalWrapper object instance, stored here so routes can access the database and other information.
        self.host = host
        self.port = port

        # Make a new base web server instance.
        self.base_web_server = base_web_server.BaseWebServer (host = host, port = port, logging_enabled = False)

        self.is_running = False # Make a variable representing whether or not the server is running.

        # Make a new HealthBoxWebServerRoutes object, which handles requests to individual routes (URLs).
        self.routes = HealthBoxWebServerRoutes (terminal_wrapper = self.terminal_wrapper)
        self.routes.bind_to (_base_web_server = self.base_web_server) # Bind routes on the base_web_server to functions on the HealthBoxWebServerRoutes instance.
    def run (self):
        self.is_running = True
        self.base_web_server.run (threaded = True)
    def shutdown (self):
        self.base_web_server.shutdown ()
        self.is_running = False

class HealthBoxWebServerRoutes:
    def __init__ (self, *, terminal_wrapper):
        # Copy the terminal wrapper reference into the object scope.
        self.terminal_wrapper = terminal_wrapper
    # A dictionary mapping route URLs to the names of functions
    # placed on this object instance.
    # __init__ binds each function to be called when that route URL is visited.
    routes = {
        "/": ("root", [], {}),
        "/api/<string:caller_type>/<path:endpoint>": ("api", [], {"pass_reference_to_request_handler": True})
    }
    def bind_to (self, *, _base_web_server): # A function that binds routes on the given base web server to functions on this object.
        for route_url, route_func_name_and_args_and_kwargs_tuple in self.routes.items ():
            route_func_name, route_args, route_kwargs = route_func_name_and_args_and_kwargs_tuple
            _base_web_server.route (route_url, *route_args, **route_kwargs) (getattr (self, route_func_name))
    # The following functions handle certain routes.
    # Look in the routes dictionary to see which routes match which functions.
    def root (self):
        return base_web_server.Response.init_with_text (text = f"HealthBox version {self.terminal_wrapper.version} is running!") # This is a placeholder
    def api (self, request_handler, caller_type, endpoint):
        log_entry = {"client_address": f"{request_handler.client_address [0]}:{request_handler.client_address [1]}", "caller_type": caller_type, "endpoint": endpoint}
        def generate_success_response (*, api_key, **extra_data):
            log_entry ["success"] = True
            log_entry ["error"] = None
            log_entry ["extra_data"] = extra_data
            self.terminal_wrapper.api_key_manager_terminal_wrapper._manager.add_log_entry (api_key = matching_api_key, log_entry = log_entry)
            response = {"success": True, "error": None, **extra_data}
            return base_web_server.Response.init_with_json (data = response)
        def generate_error_response (*, api_key = None, error_text):
            log_entry ["success"] = False
            log_entry ["error"] = error_text
            if api_key is not None: self.terminal_wrapper.api_key_manager_terminal_wrapper._manager.add_log_entry (api_key = api_key, log_entry = log_entry)
            response = {"success": False, "error": error_text}
            return base_web_server.Response.init_with_json (data = response)
        if caller_type not in ["source", "app"]:
            return generate_error_response (error_text = "Bad caller type!")
        print (f"Caller type: {caller_type}")
        print (f"Endpoint: {endpoint}")
        print (f"URL arguments: {request_handler.args}")
        if "api_key" not in request_handler.args:
            return generate_error_response (error_text = "No API key!")
        api_key = request_handler.args ["api_key"]
        # Perform verification of this API key to make sure it's authorized to carry out the specified action.
        api_key_has_match = False
        for valid_api_key in self.terminal_wrapper.db ["api_keys"]:
            if valid_api_key ["key"] != api_key: continue
            print ("Found matching key!")
            api_key_has_match = True
            matching_api_key = valid_api_key
        if not api_key_has_match: return generate_error_response (error_text = "Invalid API key!")
        if matching_api_key ["type"] != caller_type: return generate_error_response (
            api_key = matching_api_key,
            error_text = f"This API key is not authorized for this type of caller! (Authorized for {valid_api_key ['type']}, attempt by {caller_type})"
        )
        if matching_api_key ["security"] == "none": return generate_error_response (
            api_key = matching_api_key,
            error_text = f"The security of this API key is set to none, so no requests are allowed through right now!"
        )
        if endpoint [0] not in ["metrics"]:
            return generate_error_response (api_key = matching_api_key, error_text = f"Invalid endpoint name {endpoint [0]}!")
        if endpoint [0] == "metrics":
            endpoint_args = endpoint [1:]
            if len (endpoint_args) != 2:
                return generate_error_response (api_key = matching_api_key, error_text = f"Too many arguments for metrics endpoint! (Need 2, received {len (endpoint_args)})")
            metric_id, metric_action = endpoint_args # Unpacks endpoint_args = ["a1", "past"] into metric_id = "a1", metric_action = "past"
            metric_id_resolution_success, metric_id_type, resolved_category, resolved_metric = metrics.resolve_metric_id (metric_id)
            if (not metric_id_resolution_success) or metric_id_type != metrics.MetricIDType.METRIC:
                return generate_error_response (api_key = matching_api_key, error_text = f"Invalid metric ID {metric_id}!")
            print (f"Resolved metric: {resolved_metric}")
            # Check whether or not we're allowed to operate on this metric based on the API key settings.
            if matching_api_key ["security"] == "all":
                pass # We don't have to check the metric since we're allowed to operate on all metrics.
            else:
                # Check if the filter contains the metric.
                filter_contains_metric = self.terminal_wrapper.api_key_manager_terminal_wrapper._manager.check_if_filter_contains (api_key = matching_api_key, target_metric_id = metric_id)
                if matching_api_key ["security"] == "whitelist": # In whitelist mode,
                    # fail if the filter does not contain the metric.
                    if not filter_contains_metric: return generate_error_response (api_key = matching_api_key, error_text = f"The API key's whitelist does not contain the given metric!")
                elif matching_api_key ["security"] == "blacklist": # In blacklist mode,
                    # fail if the filter contains the metric.
                    if filter_contains_metric: return generate_error_response (api_key = matching_api_key, error_text = f"The API key's blacklist contains the given metric!")
            if metric_action not in ["current", "past", "submit"]:
                return generate_error_response (api_key = matching_api_key, error_text = f"Invalid metric action {metric_action}!")
            if (metric_action in ["current", "past"] and caller_type != "app") or (metric_action in ["submit"] and caller_type != "source"):
                return generate_error_response (api_key = matching_api_key, error_text = f"Invalid metric action {metric_action} for caller type {caller_type}!")
            if metric_id not in self.terminal_wrapper.db ["metrics"]:
                metric_data = {"entries": []}
                self.terminal_wrapper.db [metric_id] = metric_data
            else:
                metric_data = self.terminal_wrapper.db ["metrics"] [metric_id]
            if metric_action == "current":
                if len (metric_data ["entries"]) == 0:
                    return generate_error_response (api_key = matching_api_key, error_text = "No data is available for this metric yet!")
                return generate_success_response (api_key = matching_api_key, current = metric_data ["entries"] [-1])
            elif metric_action == "past":
                return generate_success_response (api_key = matching_api_key, past = metric_data ["entries"])
            elif metric_action == "submit":
                if "submission" not in request_handler.args:
                    return generate_error_response (api_key = matching_api_key, error_text = "No submission data was provided!")
                submission_json = request_handler.args ["submission"]
                try:
                    submission = json.loads (submission_json)
                except json.decoder.JSONDecodeError:
                    return generate_error_response (api_key = matching_api_key, error_text = "Invalid submission data was provided!")
                if "timestamp" not in submission or not submission ["timestamp"].isdigit (): # isdigit () is only True if all characters in the string are digits and there is at least one character.
                    return generate_error_response (api_key = matching_api_key, error_text = "The submission timestamp was either not provided or invalid!")
                if "data" not in submission: # TODO: add more complex validation for data
                    return generate_error_response (api_key = matching_api_key, error_text = "The submission data was not provided!")
                metric_data.append (submission)
                metric_data.sort (key = lambda metric_data_entry: metric_data_entry ["timestamp"])
                # TODO: implement binary search algorithm instead of appending and re-sorting the list every time, as this quickly becomes more computationally expensive.
                self.terminal_wrapper.db.save ()
                return generate_success_response (api_key = matching_api_key)
