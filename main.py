import metrics, utils, database, crypto, database_interfaces, web_server # metrics.py, utils.py, database.py, crypto.py, database_interfaces.py, web_server.py

import numpy
import pickle
import traceback # For use with the debug console

config_root = str(Path.home()) + "/.config/HealthBox"


def prepare_settings_database():

    # settings_database_array[0] is whether or not to highlight invalid options as red

    if os.path.isdir(str(Path.home()) + "/.config") == False:
        print("Error: ~/.config is missing")
        print("This suggests that your host OS might be damaged")
    else:
        if os.path.isdir(config_root + "") == False:
            # ~/.config/HealthBox doesn't exist, and will be created
            os.mkdir(config_root + "") # Create ~/.config/HealthBox
        else:
            if os.path.isfile(config_root + "/settings.db") == False: # If the settings database doesn't exist, create it, and fill it with the default array
                # ~/.config/HealthBox/settings.db is missing, and will be created
                settings_database = open(config_root + "/settings.db", "wb")
                settings_database_array = ["true", "placeholder", "placeholder", "placeholder"] # Default settings
                settings_database.write(pickle.dumps(settings_database_array, protocol=0))
                settings_database.close()
                
            else: # If the settings database does exist, open it, and load the database from it
                print("The vOS file system appears to be intact")
                settings_database = open(config_root + "/settings.db", "rb")
                settings_database_array = pickle.loads(settings_database.read())
                settings_database.close()

def settings():
    prepare_settings_database()
    utils.clear()
    input("Test")

class HealthBoxTerminalWrapper: # contains various facilities for access to HealthBox via a terminal
    version = "BETA (WIP)" # This string is currently part of a message shown when the root of the web server is accessed.
    def __init__ (self):
        self.db_file_name = "db.json" # TODO: add a way to change this
        self.default_db_data = {
            "api_keys": [],
            # An entry for each metric is created
            # when data is submitted to the server for the first time.
            # This saves space if certain metrics are never tracked.
            "metrics": {}
        }
        self.crypto_data_file_name = "db.cryptodata" # TODO: this too
        self.encryption_text_encoding = "utf-8" # no reason to change this
        self.db = None # stays None until database is initialized through option 4

        self.api_key_manager_terminal_wrapper = database_interfaces.HealthBoxAPIKeyManagerTerminalWrapper (self) # Initialized on app initialization for use by the web server's API handling

        # TODO: Add a way to change these web server settings.
        self.web_server_host = "0.0.0.0"
        self.web_server_port = 5050
        self.web_server = web_server.HealthBoxWebServer (host = self.web_server_host, port = self.web_server_port, terminal_wrapper = self)
    def main_menu (self):
        while True: # Run the program as an endless loop until terminated
            utils.clear()
            if not self.web_server.is_running:
                utils.print_red_if_false ("1. Start HealthBox", self.db is not None)
            else:
                print ("1. Shut down HealthBox")
            print("2. Instructions")
            print("3. Settings")
            print("4. Initialize database")
            print("5. List supported health metrics")
            utils.print_red_if_false ("6. Manage API keys", self.db is not None)
            print("7. Exit")
            # print ("c. Debug console") # This is only meant for debugging purposes, so the print statement is commented out.
            selection = input (utils.color.WHITE + "Selection: " + utils.color.END)
            selection.lower()

            utils.clear()

            if selection == "2":
                utils.pause_with_message ("This feature has not yet been implemented")
            elif selection == "1":
<<<<<<< HEAD
                self.start()
            elif selection == "3":
                settings()
=======
                self.start_or_stop_web_server ()
>>>>>>> 288720ca6e27dc8a5000d15f89a92e0fac6fc186
            elif selection == "4":
                self.initialize_database()
            elif selection == "5":
                self.list_health_metrics()
            elif selection == "6":
                self.manage_keys ()
            elif selection == "7":
                break # Terminate program
            elif selection == "c":
                self.debug_console ()
            else:
                utils.pause_with_message ("Unknown option")
    def start_or_stop_web_server (self): # Option 1 in main menu
        utils.clear ()

        if self.db is None:
            utils.pause_with_message ("Initialize the database first! (option 4)")
            return

        if not self.web_server.is_running:
            # Since the web server isn't running, run it.
            self.web_server.run ()
        else:
            # Since the web server is running, shut it down.
            self.web_server.shutdown ()
    def initialize_database (self):
        utils.clear ()

        if self.db is not None:
            utils.pause_with_message ("The database is already initialized!")
            return

        print ("Your database will be encrypted so other local apps can't access your data without your permission.")
        print ("You'll need an encryption key, which is basically a password that's used to encrypt and decrypt the database.")
        print ("If the database has existed in the past, use the previous encryption key.")
        print ("(An error will be thrown if it's incorrect.)")
        print ("Otherwise, choose an encryption key for the new database.")
        print ("")
        string_key = input ("Enter your encryption key: ")

        self.db = database.JSONDatabaseBackend (
            db_file_name = self.db_file_name,
            default = self.default_db_data,
            encryption = True,
            crypto_data_file_name = self.crypto_data_file_name,
            string_key = string_key,
            encryption_text_encoding = self.encryption_text_encoding
        )

        while True:
            good_key = True
            try:
                self.db.load ()
            except crypto.InvalidKeyError:
                good_key = False
                string_key = input ("Invalid encryption key! Try again: ")
                self.db.string_key = string_key
            if good_key: break

        # A fix for an old default database structure
        if "metric_categories" in self.db:
            del self.db ["metric_categories"]
            self.db ["metrics"] = {}
            self.db.save ()
        
        print ("")
        print ("Database initialized successfully.")
        utils.pause_with_message (f"You may want to write down your encryption key \"{string_key}\" for future reference.")
    def list_health_metrics (self): # option 5 in main menu
        while True:
            utils.clear ()

            print (metrics.generate_metric_printout ())

            print(utils.color.WHITE + "q|quit: Return to menu" + utils.color.END)

            selection = input(utils.color.WHITE + "Selection: " + utils.color.END)
            selection = selection.lower () # accept lowercase selections

            if selection in ["q", "quit"]:
                break

            match_success, id_type, resolved_category, resolved_metric = metrics.resolve_metric_id (selection)
            if not match_success:
                utils.pause_with_message ("Invalid metric or metric category ID!")
                continue

            utils.clear ()
            print (f"Metric category: {matched_category ['name']}")
            print (f"Metric name: {metric ['name']}")
            print (f"Metric description: {metric ['description']}")

            utils.pause_with_message ("\n")
    def manage_keys (self): # Option 6 in main menu
        # Make sure the database has been initialized before opening the API key management menu
        if self.db is None:
            utils.pause_with_message ("Initialize the database first! (option 4)")
            return
        self.api_key_manager_terminal_wrapper.api_key_management_menu () # Launch the menu using the terminal wrapper
    def debug_console (self):
        print ("Welcome to the debug console! Type your command at the >>> and type 'exit' to exit.")
        print ("To switch to evaluate mode (the default), where your command is evaluated as an expression and printed, type '_eval'.")
        print ("To switch to execute mode, where your command is executed (supports variable assignment, del, etc) and the result is not printed, type '_exec'.")
        console_func = eval
        while True:
            command = input (">>> ")
            if command == "exit": break
            if command == "_eval":
                console_func = eval
            elif command == "_exec":
                console_func = exec
            else:
                try:
                    if console_func == eval:
                        print (eval (command)) # Print the result of evaluating the command
                    else:
                        exec (command) # Execute the command; exec does not return a value
                except:
                    traceback.print_exc () # Print the exception thrown rather than crashing the program

if __name__ == "__main__":
    HealthBoxTerminalWrapper ().main_menu ()
