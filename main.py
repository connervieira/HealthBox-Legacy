import metrics, utils, database, crypto, database_interfaces # metrics.py, utils.py, database.py, crypto.py, database_interfaces.py

import traceback # For use with the debug console

class HealthBoxTerminalWrapper: # contains various facilities for access to HealthBox via a terminal
    def __init__ (self):
        self.db_file_name = "db.json" # TODO: add a way to change this
        self.default_db_data = {
            "api_keys": [],
            # an entry for each metric category is created
            # when data is submitted to the server for the first time.
            # this saves space if certain metrics are never tracked
            "metric_categories": []
        }
        self.crypto_data_file_name = "db.cryptodata" # TODO: this too
        self.encryption_text_encoding = "utf-8" # no reason to change this
        self.db = None # stays None until database is initialized through option 4

        self.api_key_manager_terminal_wrapper = None # Initialized when option 6 in the menu is called
    def main_menu (self):
        while True: # Run the program as an endless loop until terminated
            utils.clear()
            utils.print_red_if_false ("1. Start HealthBox", self.db is not None)
            print("2. Instructions")
            print("3. Settings")
            print("4. Initialize database")
            print("5. List supported health metrics")
            utils.print_red_if_false ("6. Manage API keys", self.db is not None)
            print("7. Exit")
            # print ("c. Debug console") # This is only meant for debugging purposes, so the print statement is commented out.
            selection = input (utils.color.WHITE + "Selection: " + utils.color.END)
            selection.lower ()

            utils.clear()

            if selection in ["2", "3"]:
                utils.pause_with_message ("This feature has not yet been implemented")
            elif selection == "1":
                self.start ()
            elif selection == "4":
                self.initialize_database ()
            elif selection == "5":
                self.list_health_metrics ()
            elif selection == "6":
                self.manage_keys ()
            elif selection == "7":
                break # Terminate program
            elif selection == "c":
                self.debug_console ()
            else:
                utils.pause_with_message ("Unknown option")
    def start (self): # option 1 in main menu
        utils.clear ()

        if self.db is None:
            utils.pause_with_message ("Initialize the database first! (option 4)")
            return
        utils.pause_with_message ("Database looks good")
        # TODO: start up the web server here
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
        if self.api_key_manager_terminal_wrapper is None: # Check if an instance of the terminal wrapper has been created yet
            self.api_key_manager_terminal_wrapper = database_interfaces.HealthKitAPIKeyManagerTerminalWrapper (self.db) # If not, create the instance
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
