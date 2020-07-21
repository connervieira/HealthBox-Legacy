import metrics, utils, database, crypto # metrics.py, utils.py, database.py, crypto.py

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
    def main_menu (self):
        while True: # Run the program as an endless loop until terminated
            utils.clear()
            print("1. Start HealthBox")
            print("2. Instructions")
            print("3. Settings")
            print("4. Initialize database")
            print("5. List supported health metrics")
            print("6. Manage Keys")
            print("7. Exit")
            selection = input (utils.color.WHITE + "Selection: " + utils.color.END)

            utils.clear()

            if selection in ["2", "3", "6"]:
                print("This feature has not yet been implemented")
                input("Press enter to coninue")
            elif selection == "1":
                self.start ()
            elif selection == "4":
                self.initialize_database ()
            elif selection == "5":
                self.list_health_metrics ()
            elif selection == "7":
                break # Terminate program
            else:
                print("Unknown option")
                input("Press enter to continue")
    def start (self): # option 1 in main menu
        utils.clear ()

        if self.db is None:
            print ("Initialize the database first! (option 4)")
            input ("Press enter to continue")
            return
        print ("Database looks good")
        # TODO: start up the web server here
        input ("Press enter to continue")
    def initialize_database (self):
        utils.clear ()

        if self.db is not None:
            print ("The database is already initialized!")
            input ("Press enter to continue")
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
        print (f"You may want to write down your encryption key \"{string_key}\" for future reference.")
        input ("Press enter to continue")
    def list_health_metrics (self): # option 5 in main menu
        utils.clear ()

        for category in metrics.metric_categories:
            print (f"{utils.color.BOLD}{category ['color']}{category ['name']}{utils.color.END * 2}")
            metric_number = 1
            for metric in category ["metrics"]:
                print (f"{category ['color']}{category ['id']}{metric_number}. {metric ['name']}{utils.color.END}")
                metric_number += 1
            print ("\n")

        print(utils.color.WHITE + "Q. Return to menu" + utils.color.END)

        selection = input(utils.color.WHITE + "Selection: " + utils.color.END)
        selection = selection.lower () # accept lowercase selections

        if selection == "q":
            return

        matched_category = None # Assume we don't have a category that matches
        for category in metrics.metric_categories: # Iterate over the categories until we find one that matches
            if selection.startswith (category ["id"].lower ()): # e.g. 'a1'.startswith ('a')
                matched_category = category
        if matched_category is None:
            print ("Unknown category selector")
            input ("Press enter to continue")
            return
        metric_number_string = selection.replace (matched_category ["id"].lower (), "") # 'a1' -> '1'
        try:
            metric_number = int (metric_number_string) # fails if not integer
            assert metric_number >= 1 and metric_number <= len (matched_category ["metrics"]) # fails if integer isn't a metric number
        except (ValueError, AssertionError):
            print ("Metric number isn't a number or isn't valid")
            input ("Press enter to continue")
            return

        metric = matched_category ["metrics"] [metric_number]
        utils.clear ()
        print (f"Metric category: {matched_category ['name']}")
        print (f"Metric name: {metric ['name']}")
        print (f"Metric description: {metric ['description']}")

        print ("\n")

        input("Press enter to continue")

if __name__ == "__main__":
    HealthBoxTerminalWrapper ().main_menu ()
