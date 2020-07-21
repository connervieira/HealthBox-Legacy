import os, time

def clear (): # Function to clear the screen
	if os.name == "nt": # Use 'cls' command if host is Windows
		os.system ("cls")
	else: # Use 'clear' command if host is Mac os Linux
		os.system ("clear")

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
