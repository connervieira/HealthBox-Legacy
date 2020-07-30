import utils # utils.py
import traceback
import urllib.parse

try:
    import requests
except ModuleNotFoundError as error:
    if traceback.format_exception_only (ModuleNotFoundError, error) != ["ModuleNotFoundError: No module named 'requests'\n"]: # Make sure the error we're catching is the right one
        raise # If not, raise the error
    raise utils.MissingLibraryError ("making web server requests", "requests")

print ("requests import succeeded!")

class APICallError (Exception): pass

class ExampleAPIConsumer:
    def __init__ (self, *, host, port, tls, api_key):
        self.host = host
        self.port = port
        self.tls = tls
        self.api_key = api_key
    def make_request (self, *, caller_type, endpoint, submission = None, print_url = False):
        protocol = "https" if self.tls else "http"
        url = f"{protocol}://{self.host}:{self.port}/api/{caller_type}/{'/'.join (endpoint)}?api_key={urllib.parse.quote (self.api_key)}"
        if submission is not None:
            url += f"&submission={urllib.parse.quote (submission)}"
        if print_url: print (f"Making a request to {url}")
        response = requests.get (url)
        response_data = response.json ()
        if not response_data ["success"]:
            raise APICallError (response_data ["error"])
        del response_data ["success"]
        del response_data ["error"]
        return response_data

class ExampleAPIConsumerTerminalWrapper:
    def __init__ (self, skip_preparation = False):
        self.consumer = None
        if not skip_preparation:
            self.prepare_to_make_requests ()
    def prepare_to_make_requests (self):
        utils.clear ()
        host = input ("Enter the host/IP of the server: ")
        port = int (input ("Enter the port of the server: "))
        tls = True if input ("Enable TLS (HTTPS)? true/false, default false: ") == "true" else False
        api_key = input ("Enter your API key: ")
        self.consumer = ExampleAPIConsumer (host = host, port = port, tls = tls, api_key = api_key)
    def main_menu (self):
        if self.consumer is None: self.prepare_to_make_requests ()
        while True:
            utils.clear ()
            choice = input ("m to make a request, r to reconfigure the API consumer, q to quit: ")
            if choice not in "mrq":
                utils.pause_with_message ("Invalid choice!")
                continue
            if choice == "m":
                self.prompt_to_make_request ()
                utils.pause_with_message ("")
            elif choice == "r":
                self.prepare_to_make_requests ()
                utils.pause_with_message ("Ready to make requests.")
            elif choice == "q":
                break
    def prompt_to_make_request (self):
        utils.clear ()
        caller_type = input ("Enter the caller type, source/app: ")
        endpoint = input ("Enter the endpoint, e.g. metrics/a1/current: ").split ('/')
        if endpoint [-1] == "submit":
            submission = input ("Enter the submission data, which should be valid JSON: ")
            print (f"Submission data: {submission}")
        else:
            submission = None
        try:
            response = self.consumer.make_request (caller_type = caller_type, endpoint = endpoint, submission = submission, print_url = True)
            print (f"A response was received from the API call: {response}")
        except APICallError as api_call_error:
            print (f"An error occured when calling the API: {str (api_call_error)}")
        except:
            print (f"An internal error occured: ")
            print ('-' * 50)
            traceback.print_exc ()
            print ('-' * 50)

if __name__ == "__main__": # The script was run from the command line
    ExampleAPIConsumerTerminalWrapper ().main_menu () # Make a new instance of the ExampleAPIConsumerTerminalWrapper class and call main_menu
