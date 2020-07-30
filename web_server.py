import utils, base_web_server # utils.py, base_web_server.py

import threading
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
        "/": "root"
    }
    def bind_to (self, *, _base_web_server): # A function that binds routes on the given base web server to functions on this object.
        for route_url, route_func_name in self.routes.items ():
            _base_web_server.route (route_url) (getattr (self, route_func_name))
    # The following functions handle certain routes.
    # Look in the routes dictionary to see which routes match which functions.
    def root (self):
        return base_web_server.Response.init_with_text (text = f"HealthBox version {self.terminal_wrapper.version} is running!") # This is a placeholder
