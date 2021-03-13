# HealthBox

An open source platform to centralize health information

![HealthBox Logo](https://v0lttech.com/assets/img/healthboxlogo.png)


## Download

Since HealthBox is written in Python, and Python is an interpreted language, the source code serves as the executable. To obtain the source code, you can either clone this repository to your computer's disk, or download it as a compressed file at <https://v0lttech.com/healthbox.php>


## Developer Instructions

Are you looking to write an application that uses the HealthBox API? Detailed documentation on how the API works is available in [DOCUMENTATION.md](DOCUMENTATION.md).


## Features

### Modular Design

HealthBox is very open and modular, which encourages developers to build software for it that fits their needs. You aren't forced to take any specific approach to managing your health information. If you don't like any of the existing methods, you can even create one completely from scratch yourself!

### Privacy Respecting

With HealthBox, you don't have to worry about your information being recorded, tracked, and collected. You remain in full control of your health data, and you can fully review the code to ensure nothing questionable is happening behind the scenes.

### Easy

The programming interface to interact with HealthBox is very simple and straight forward, allowing even inexperienced programmers to develop for the platform.

### Centralization

Instead of having to use several, or even dozens of external programs, HealthBox gives the potential for developers to store health information in one central place. This improves convenience for both users and developers.

### Secure

HealthBox uses encryption to make sure badly behaving programs can't access your health information without asking for permission.


## Usage

To use HealthBox, download the latest version, then run `main.py` using Python 3. These instructions explain how to do that using the command line on GNU/Linux, MacOS, and Android. On Windows, the process is similar, but may require tweaking many of the commands.

1. `git clone https://github.com/connervieira/HealthBox --recurse-submodules`
2. `cd HealthBox`
3. `pip3 install pycryptodomex`
4. `python3 main.py`

It should be noted that you may need to install other Python modules using the `pip3` command, in the event that HealthBox depends on them but your OS doesn't come with them pre-installed. If this is the case, the 3rd command above will fail, and specify which modules need to be installed.

Another fact to keep note of is that HealthBox will create it's database in whatever folder you run the `main.py` script from. That is to say, if you run `pwd` just before entering `python3 /path/to/main.py`, the database will be created in the folder specified by `pwd`, not necessarily the folder that `main.py` is located in.


## Credits

Special thanks to [https://github.com/An0nDev](An0nDev) on GitHub for developing the server backend that HealthBox depends on!
