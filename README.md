# HealthBox Legacy

An open source platform to centralize health information

![HealthBox Logo](https://v0lttech.com/assets/img/healthboxlogo.png)


## Discontinued

This version of HealthBox has been discontinued in favor of completely redeveloped platform to make future development easier and more organized. The re-developed version will take the name "HealthBox", while this original version will take the name "HealthBox Legacy". Ideally, these two versions will retain compatibility with each-other, such that any programs developed for the original HealthBox will be compatible with the redesign. However, the redesign is still very early in development, so everything is subject to change.


## Download

Since HealthBox is written in Python, and Python is an interpreted language, the source code serves as the executable. To obtain the source code, you can either clone this repository to your computer's disk using the `git clone https://github.com/connervieira/HealthBox --recurse-submodules` command, or download it as a compressed file at <https://v0lttech.com/healthbox.php>


## User Instructions

If you're a user looking to try out HealthBox, check out [USAGE.md](USAGE.md)


## Developer Instructions

Are you looking to write an application that uses the HealthBox API? Detailed documentation on how the API works is available in [DOCUMENTATION.md](DOCUMENTATION.md).


## Features

### Modular Design

HealthBox is very open and modular, which encourages developers to build software for it that fits their needs. You aren't forced to take any specific approach to managing your health information. If you don't like any of the existing methods, you can even create one completely from scratch yourself!

### Privacy Respecting

With HealthBox, you don't have to worry about your information being recorded, tracked, and collected. You remain in full control of your health data, and you can fully review the code to ensure nothing questionable is happening behind the scenes. HealthBox also forces programs to respect your privacy by controlling what they can and can't access from your data.

### Easy

The programming interface to interact with HealthBox is very simple and straight forward, allowing even inexperienced programmers to develop for the platform.

### Centralization

Instead of having to use several, or even dozens of external programs, HealthBox gives the potential for developers to store health information in one central place. This improves convenience for both users and developers.

### Secure

HealthBox uses encryption to make sure badly behaving programs can't access your health information without asking for permission. The only way for a program to read or write data is using an API key that you grant them.

### Lightweight

HealthBox is designed to be as lightweight as possible, meaning it is easy to run on a lightweight computer like a Raspberry Pi. It's also easy to run in the background on your computer without disrupting other tasks.

### Extensible

HealthBox is designed to be as easy as possible to extend with additional features using external programs.


## Credits

Special thanks to [https://github.com/An0nDev](https://github.com/An0nDev) on GitHub for developing the server back-end that HealthBox depends on!
