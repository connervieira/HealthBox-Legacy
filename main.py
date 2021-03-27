# HealthBox
# V0LT
# Version 1.3
# Licensed under the GPLv3



# ----- Configuration -----

# The server_port is simply the port that HealthBox runs on. 5050 should work for most situations, but in the event that this conflicts with another service, you may want to change it here.
server_port = 5050



# This is the file name of the file that HealthBox uses to store cryptographic data about the database.
database_crypto_information_file = "db.cryptodata"

# This is the the file name of the database HealthBox uses to store information. This database is encrypted.
database_file = "db.json"

# ----- End Of Configuration -----



# Import other Python scripts
import metrics, utils, database, crypto, database_interfaces, web_server # metrics.py, utils.py, database.py, crypto.py, database_interfaces.py, web_server.py


# Import required Python modules
import os
from pathlib import Path
import pickle
import traceback # For use with the debug console
import json # for importing/exporting the database contents



class HealthBoxTerminalWrapper: # contains various facilities for access to HealthBox via a terminal
    version = "v1.3" # This string is currently part of a message shown when the root of the web server is accessed.
    def __init__ (self):
        utils.clear ()
        print ("HealthBox is starting up, one moment...\n")
        self.db_file_name = database_file
        self.default_db_data = {
            "api_keys": [],
            # An entry for each metric is created
            # when data is submitted to the server for the first time.
            # This saves space if certain metrics are never tracked.
            "metrics": {}
        }
        self.crypto_data_file_name = database_crypto_information_file
        self.encryption_text_encoding = "utf-8"
        self.db = None # Stays as None until database is initialized through option 4

        self.api_key_manager_terminal_wrapper = database_interfaces.HealthBoxAPIKeyManagerTerminalWrapper (self) # Initialized on app initialization for use by the web server's API handling

        self.web_server_host = "0.0.0.0"
        self.web_server_port = server_port
        self.web_server = web_server.HealthBoxWebServer (host = self.web_server_host, port = self.web_server_port, terminal_wrapper = self)

        self.config_root = str (Path.home ()) + "/.config/HealthBox"
        print ("Preparing the settings database...")
        self._prepare_settings_database ()

        utils.clear() # Clear the screen

        utils.pause_with_message ("Welcome to HealthBox!")
    def main_menu (self):
        while True: # Run the program as an endless loop until terminated
            utils.clear()
            if not self.web_server.is_running:
                utils.print_red_if_false ("1. Start HealthBox", self.db is not None)
            else:
                print ("1. Shut down HealthBox")
            print("2. Instructions")
            print("3. Settings")
            utils.print_red_if_false ("4. Initialize database", self.db is None)
            utils.print_red_if_false ("5. Import or export database", self.db is not None)
            print("6. List supported health metrics")
            utils.print_red_if_false ("7. Manage API keys", self.db is not None)
            print("8. Exit")
            # print ("c. Debug console") # This is only meant for debugging purposes, so the print statement is commented out.
            selection = input (utils.color.WHITE + "Selection: " + utils.color.END)
            selection.lower()

            utils.clear()

            if selection == "2":
                self.instructions()

            elif selection == "1":
                self.start_or_stop_web_server()

            elif selection == "3":
                self.settings()

            elif selection == "4":
                self.initialize_database()

            elif selection == "5":
                self.import_or_export_database()

            elif selection == "6":
                self.list_health_metrics()

            elif selection == "7":
                self.manage_keys ()

            elif selection == "8" or selection == "q":
                break # Terminate program

            elif selection == "c":
                self.debug_console ()

            else:
                utils.pause_with_message ("Unknown option")

    def _prepare_settings_database (self):

        # settings_database_array[0] is whether or not to highlight invalid options as red

        if os.path.isdir(str(Path.home()) + "/.config") == False: # ~/.config is missing, we're probably on Windows or something nasty happened to the OS
            os.mkdir (str (Path.home ()) + "/.config") # Create ~/.config
        if os.path.isdir(self.config_root + "") == False:
            # ~/.config/HealthBox doesn't exist, and will be created
            os.mkdir(self.config_root + "") # Create ~/.config/HealthBox
        else:
            if os.path.isfile(self.config_root + "/settings.db") == False: # If the settings database doesn't exist, create it, and fill it with the default array
                # ~/.config/HealthBox/settings.db is missing, and will be created
                self.settings_database_array = ["true", "5050", "db.json", "db.cryptodata", "placeholder", "placeholder"] # Default settings
                self._save_settings_database ()
            else: # If the settings database does exist, open it, and load the database from it
                settings_database_file = open(self.config_root + "/settings.db", "rb")
                self.settings_database_array = pickle.loads(settings_database_file.read())
                settings_database_file.close()
    def _save_settings_database (self):
        settings_database_file = open(self.config_root + "/settings.db", "wb")
        settings_database_file.write(pickle.dumps(self.settings_database_array, protocol=0)) # protocol = 0 forces pickle to use the original, human-readable serialization format
        settings_database_file.close()
    def settings (self):
        utils.clear()
        utils.pause_with_message ("Settings menu coming soon")

    def instructions (self):
        print("Please select a category you'd like to learn more about")
        print("0. Back to main menu")
        print("1. Connecting apps and devices to HealthBox")
        print("2. Changing the default port or database name")

        selection = int(input("Selection: "))

        utils.clear()

        if (selection == 0):
            pass
        elif (selection == 1):
            print("The connect a program or device to HealthBox, follow these instructions.")
            print("1. Open HealthBox")
            print("2. Open the 'Manage API keys' menu from the main menu.")
            print("3. Create a new API key, and give it a recognizable name by entering the following:")
            print("    c MyDeviceName")
            print("4. A new API key should appear at the top of the interface. Take note of it's number.")
            print("5. Edit the API key using the 'e #' command. Replace the '#' with the API key's number, like so.")
            print("    e 1")
            print("6. Set the API key type. If the API key will be used to submit data, set it's type as 'source' using this command: 't s'. If the API key will be used to read data, then set its type as 'app', using this command: 't a'.")
            print("7. Optionally, configure which metrics the API key can and can't access using the 'Security' and 'Filter' functions.")
            print("8. Input the API key, HealthBox server address, and port into the application or device you'd like to configure.")
        elif (selection == 2):
            print("To configure the default port number or database name of HealthBox, follow these instructions")
            print("1. Open `main.py` in the HealthBox folder in a text editor of your choice.")
            print("2. Locate the section at the top of the script labeled `----- Configuration -----`")
            print("3. Modify the values as desired")
            pritn("4. Save `main.py` and exit")
        else:
            utils.pause_with_message("Invalid selection")


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
        print ("If you've already created a database, use the previous encryption key.")
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
    def import_or_export_database (self):
        if self.db is None:
            utils.pause_with_message ("Initialize the database first! (option 4)")
            return
        while True:
            utils.clear ()
            print ("Commands:")
            print ("i|import: Import the contents of the database as a JSON string")
            print ("e|export: Export the contents of the database as a JSON string")
            print ("p|print: Pretty-print the contents of the database for easy inspection")
            print ("q|quit: Exit to main menu")

            command = input ("Enter your command: ")
            command_name, command_argument = utils.parse_command (command)
            command_name_resolution_success, command_name = utils.resolve_aliases (command_name, [["import", "i"], ["export", "e"], ["print", "p"], ["quit", "q"]])
            if not command_name_resolution_success:
                utils.pause_with_message ("Invalid command!")
                continue
            if command_name == "import":
                while True:
                    imported_db_string = input ("Paste the JSON string with the database contents (hit Enter to cancel): ")
                    if imported_db_string == "": break
                    try:
                        imported_db = json.loads (imported_db_string)
                    except json.decoder.JSONDecodeError:
                        print ("JSON decode error! Is that a valid JSON string? (Make sure there aren't newlines)")
                        continue
                    self.db._db = imported_db # write directly to the internal dictionary
                    utils.pause_with_message ("Database contents successfully imported!")
                    break
            elif command_name == "export":
                utils.pause_with_message ("On the following screen, the database contents will be visible; use the Select All function in your terminal emulator to copy them, then press Enter to continue.")
                utils.clear ()
                input (json.dumps (self.db._db))
                utils.pause_with_message ("Database contents successfully exported!")
            elif command_name == "print":
                utils.pause_with_message (json.dumps (self.db._db, indent = 4))
            elif command_name == "quit": break
    def list_health_metrics (self): # option 6 in main menu
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
    def manage_keys (self): # Option 7 in main menu
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
