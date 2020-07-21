import metrics, utils # metrics.py, utils.py
import traceback

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

    if selection in ["1", "2", "3", "4", "6"]:
        print("This feature has not yet been implemented")
        input("Press enter to coninue")
    elif selection == "5":
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
            continue # Skips the rest of the current iteration, checks the condition, and starts a new iteration

        matched_category = None # Assume we don't have a category that matches
        for category in metrics.metric_categories: # Iterate over the categories until we find one that matches
            if selection.startswith (category ["id"].lower ()): # e.g. 'a1'.startswith ('a')
                matched_category = category
        if matched_category is None:
            print ("Unknown category selector")
            input ("Press enter to continue")
            continue
        metric_number_string = selection.replace (matched_category ["id"].lower (), "") # 'a1' -> '1'
        try:
            metric_number = int (metric_number_string) # fails if not integer
            assert metric_number >= 1 and metric_number <= len (matched_category ["metrics"]) # fails if integer isn't a metric number
        except (ValueError, AssertionError):
            traceback.print_exc ()
            print ("Metric number isn't a number or isn't valid")
            input ("Press enter to continue")
            continue

        metric = matched_category ["metrics"] [metric_number]
        utils.clear ()
        print (f"Metric category: {matched_category ['name']}")
        print (f"Metric name: {metric ['name']}")
        print (f"Metric description: {metric ['description']}")

        print ("\n")

        input("Press enter to coninue")


    elif selection == "7":
        break # Terminate program

    else:
        print("Unknown option")
        input("Press enter to continue")
