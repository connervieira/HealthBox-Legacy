# Usage

Note: This document is for users looking to run HealthBox. If you're a developer looking to develop a piece of software or hardware for HealthBox, please see [DOCUMENTATION.md](DOCUMENTATION.md)

For a quick start guide, jump to the 'Running' section of this document.

Be sure to also read [SECURITY.md](SECURITY.md) to learn about the security features and limitations of HealthBox.


## Supported Platforms

HealthBox is written in Python, which is an interpreted language, meaning it will run on practically any device.

Requires minimal tweaking:
- GNU/Linux
    - Raspberry Pi included
- BSD
- MacOS
- Windows

Requires a bit of tweaking:
- Android

Requires significant tweaking:
- iOS

While not recommended for sake of battery life, it is entirely possible to run the HealthBox server on a mobile device. However, depending on how locked down your hardware vendor is, you may have a considerably harder time doing it. If you're running Android on your mobile device, it should be relatively easy to install a terminal emulator like Termux, and run HealthBox. If you're on iOS, you'll be able to run HealthBox, but it will almost certainly require a jailbreak. It should be noted for sake of clarity that mobile devices are perfectly capable of running software that connects with a remote HealthBox server running on a device more suited to the task. If you'd like to run the HealthBox server but only have a mobile device, it's highly recommended that you purchase an inexpensive single-board computer like a Raspberry Pi. HealthBox is designed to be extremely lightweight, so even inexpensive hardware should be able to run it without any issues.

- Android
- iOS


## Running

To use HealthBox, download the latest version, then run `main.py` using Python 3. These instructions explain how to do that using the command line on GNU/Linux, MacOS, and Android. On Windows, the process is similar, but may require tweaking many of the commands.

1. Download and install Python3 if it doesn't come with your system for some reason. This step is not necessary on most devices. Run this command to install Python3 on a Debian based GNU/Linux computer:
    - `sudo apt-get install python3`
2. Download HealthBox and all of its submodules:
    - `git clone https://github.com/connervieira/HealthBox --recurse-submodules`
3. Change into the newly downloaded HealthBox directory:
    - `cd HealthBox`
4. Install Python3 modules that HealthBox depends on:
    - `pip3 install pycryptodomex`
5. Run HealthBox using Python3:
    - `python3 main.py`
6. HealthBox should now be up and running. Next you should initialize the HealthBox database, and start the HealthBox server from the main menu.

It should be noted that you may need to install other Python modules using the `pip3` command, in the event that HealthBox depends on them but your OS doesn't come with them pre-installed. If this is the case, the 5th command above will fail, and specify which modules need to be installed. Simply install them using `pip3`.

Another fact to keep note of is that HealthBox will create it's database in whatever folder you run the `main.py` script from. That is to say, if you run `pwd` just before entering `python3 /path/to/main.py`, the database will be created in the folder specified by `pwd`, not necessarily the folder that `main.py` is located in. If you run HealthBox a second time, and suddenly your database appears to be empty, this is very likely the reason why.
