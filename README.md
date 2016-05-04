# ccKufi-Name-Finder
Find out which part of ccKufi's name comes from your username.

**All downloads can be found [here](https://github.com/Iwuh/ccKufi-Name-Finder/releases/tag/v1.1).**

# How to use

## Executable

### Windows

Download the latest version of the windows executable. Use 7zip or another tool to extract the files, then run ccKufi-Name-Finder.exe

### 64 Bit Linux

Download the latest version of the x64 Linux executable. Extract the contents by running `tar xvfz "ccKufi-Name-Finder-Linux-x64.tar.gz`.

**NOTE: The downloaded executable will only work with glibc version 2.23 (the latest version as of 19/02/2016) or later. If you are using an older version of glibc or an alternate implementation of the C standard library you will need to build the executable yourself or run it from source. You can view your current glibc version by running `ldd --version`.**

### Other

There are no downloads for other operating systems. Either run it from source or build it yourself (covered elsewhere in this readme).

## From Source

### Windows

Have the dependencies listed under Building -> Windows installed.

Download the latest version of the source code and extract the contents. In a command prompt, run `python finder.py` in the same directory as the files.

### Linux

Have the dependencies listed under Building -> Linux installed. Download the latest version of the source code and extract the contents. In a terminal either run `python3 finder.py` or `./finder.py` in the same directory as the files.

### Mac

Have the dependencies listed under Building -> Mac installed. Download the latest version of the source code and extract the contents. In a terminal, run `finder.py`. I don't use a Mac and have no idea how they work. I assume it's something similar to Linux.

## Building

### Windows

Install the following programs:

* Python 3.5.1
* Pip-Win (optional)

Install the following dependencies using pip:

* Update pip (`pip install -U pip`)
* Install Colorama, Wheel, PyInstaller (`pip install requirements.txt`)

Build the script by running `windowsbuild.bat`. The executable will be located in dist\ccKufi-Name-Finder-Windows.

### Linux

Install the following packages:

* python3
* python3-pip

Install Wheel, Colorama, and PyInstaller by running `pip3 install requirements.txt`.

### Mac

I don't know how installing packages on Mac works. Unless somebody updates this with a guide, you're probably better off running from source. If you really want to build the executable, here are the basic steps.

Install:

Python 3.5.1
Pip

Install Wheel, Colorama, and PyInstaller with pip. It will likely be `pip3 install requirements.txt`.
