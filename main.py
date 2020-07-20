from os import system, name 
from time import sleep 
  
def clear(): # Function to clear the screen
    if name == 'nt':  # Use 'cls' command if host is Windows
        _ = system('cls') 
    else: # Use 'clear' command if host is Mac or Linux
        _ = system('clear')

class color: # Define various text styling elements
    WHITE = '\033[37m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


while True: # Run the program as an endless loop until terminated
    clear()
    print("1. Start HealthBox")
    print("2. Instructions")
    print("3. Settings")
    print("4. Initialize database")
    print("5. List supported health metrics")
    print("6. Manage Keys")
    print("7. Exit")
    selection = raw_input(color.WHITE + "Selection: " + color.END)

    clear()
    
    if selection == "1":
        print("This feature has not yet been implemented")
        raw_input("Press enter to coninue")
    elif selection == "2":
        print("This feature has not yet been implemented")
        raw_input("Press enter to coninue")
    elif selection == "3":
        print("This feature has not yet been implemented")
        raw_input("Press enter to coninue")
    elif selection == "4":
        print("This feature has not yet been implemented")
        raw_input("Press enter to coninue")
    elif selection == "5":
        print(color.BOLD + color.RED + "Activity" + color.END + color.END)
        print(color.RED + "A1. Steps" + color.END)
        print(color.RED + "A2. Active Calories" + color.END)
        print(color.RED + "A3. On Foot Distance" + color.END)
        print(color.RED + "A4. Resting Energy" + color.END)
        print(color.RED + "A5. Active Minutes" + color.END)
        print(color.RED + "A6. Standing Time" + color.END)
        print(color.RED + "A7. Stair Flights Climb" + color.END)
        print(color.RED + "A8. Cycling Distance" + color.END)
        print(color.RED + "A9. Swimming Distance" + color.END)
        print(color.RED + "A10. Wheelchair Distance" + color.END)
        print(color.RED + "A11. Workout" + color.END) # Any deliberate physical activity (running, walking, swimming, weight lifting, soccer, etc.

        print("\n")        

        print(color.BOLD + color.CYAN + "Mental Health" + color.END + color.END)
        print(color.CYAN + "B1. PHQ-9 Score (Depression Test)" + color.END)
        print(color.CYAN + "B2. Y-BOCS Score (OCD Test)" + color.END)
        print(color.CYAN + "B3. GAD-7 Score (Anxiety Test)" + color.END)
        print(color.CYAN + "B4. MDQ Score (Bipolar Test)" + color.END)
        print(color.CYAN + "B5. ASRS Score (ADHD Test)" + color.END)
        print(color.CYAN + "B6. Mindful Minutes" + color.END)
        print(color.CYAN + "B7. Mood" + color.END)
        print(color.CYAN + "B8. Sexual Activity" + color.END)

        print("\n")

        print(color.BOLD + color.GREEN + "Nutrition" + color.END + color.END)
        print(color.GREEN + "C1. Calories" + color.END)
        print(color.GREEN + "C2. Water" + color.END)
        print(color.GREEN + "C3. Sugar" + color.END)
        print(color.GREEN + "C4. Fiber" + color.END)
        print(color.GREEN + "C5. Protein" + color.END)
        print(color.GREEN + "C6. Saturated Fat" + color.END)
        print(color.GREEN + "C7. Trans Fat" + color.END)
        print(color.GREEN + "C8. Monosaturated Fat" + color.END)
        print(color.GREEN + "C9. Polysaturated Fat" + color.END)
        print(color.GREEN + "C10. Unspecified Fat" + color.END)
        print(color.GREEN + "C11. Calcium" + color.END)
        print(color.GREEN + "C12. Carbohydrates" + color.END)
        print(color.GREEN + "C13. Cholesterol" + color.END)
        print(color.GREEN + "C14. Iron" + color.END)
        print(color.GREEN + "C15. Sodium" + color.END)
        print(color.GREEN + "C16. Vitamin A" + color.END)
        print(color.GREEN + "C17. Vitamin B6" + color.END)
        print(color.GREEN + "C18. Vitamin B12" + color.END)
        print(color.GREEN + "C19. Vitamin C" + color.END)
        print(color.GREEN + "C20. Vitamin D" + color.END)
        print(color.GREEN + "C21. Vitamin E" + color.END)
        print(color.GREEN + "C22. Vitamin K" + color.END)
        print(color.GREEN + "C23. Zinc" + color.END)
        print(color.GREEN + "C24. Biotin" + color.END)
        print(color.GREEN + "C25. Caffeine" + color.END)
        print(color.GREEN + "C26. Chloride" + color.END)
        print(color.GREEN + "C27. Chromium" + color.END)
        print(color.GREEN + "C28. Copper" + color.END)
        print(color.GREEN + "C29. Folate" + color.END)
        print(color.GREEN + "C30. Iodine" + color.END)
        print(color.GREEN + "C31. Magnesium" + color.END)
        print(color.GREEN + "C32. Manganese" + color.END)
        print(color.GREEN + "C33. Molybdenum" + color.END)
        print(color.GREEN + "C34. Niacin" + color.END)
        print(color.GREEN + "C35. Pantothenic Acid" + color.END)
        print(color.GREEN + "C36. Phosphorus" + color.END)
        print(color.GREEN + "C37. Potassium" + color.END)
        print(color.GREEN + "C38. Riboflavin" + color.END)
        print(color.GREEN + "C39. Selenium" + color.END)
        print(color.GREEN + "C40. Thiamin" + color.END)

        print("\n")

        print(color.BOLD + color.YELLOW + "Measurements" + color.END + color.END)
        print(color.YELLOW + "D1. Weight" + color.END)
        print(color.YELLOW + "D2. Height" + color.END)
        print(color.YELLOW + "D3. Body Temperature" + color.END)
        print(color.YELLOW + "D4. Electrodermal Activity" + color.END)
        print(color.YELLOW + "D5. Waist Circumference" + color.END)
        print(color.YELLOW + "D6. Breathing Rate" + color.END)
        print(color.YELLOW + "D7. Oxygen Saturation" + color.END)
        print(color.YELLOW + "D8. Heart Rate" + color.END)
        print(color.YELLOW + "D9. Resting Heart Rate" + color.END)
        print(color.YELLOW + "D10. Walking Heart Rate" + color.END)
        print(color.YELLOW + "D11. Running Heart Rate" + color.END)
        print(color.YELLOW + "D12. Heart Rate Variability" + color.END)
        print(color.YELLOW + "D13. Peripheral Perfusion Index" + color.END)
        print(color.YELLOW + "D14. Lung Capacity" + color.END)
        print(color.YELLOW + "D15. VO2 Max" + color.END)
        print(color.YELLOW + "D16. Blood Pressure" + color.END)
        print(color.YELLOW + "D17. Blood Sugar" + color.END)
        print(color.YELLOW + "D18. Blood Alcohol Content" + color.END)
        print(color.YELLOW + "D19. Sound Exposure" + color.END)
        print(color.YELLOW + "D20. Sleep" + color.END)
        print(color.YELLOW + "D21. Atypical Pulse" + color.END)
        print(color.YELLOW + "D22. Audiogram" + color.END)

        print("\n")

        print(color.WHITE + "Q. Return to menu" + color.END)
        selection = raw_input(color.WHITE + "Selection: " + color.END)

        if selection.lower() == "a1":
            pass
        elif selection.lower() == "b1":
            pass
        elif selection.lower() == "c1":
            pass
        elif selection.lower() == "q":
            pass
        else:
            print("Unknown option")
            raw_input("Press enter to coninue")


    elif selection == "6":
        break # Terminate program
    
    else:
        print("Unknown option")
        raw_input("Press enter to continue")
