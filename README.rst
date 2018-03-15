==========
led_tester
==========


This project creates a grid of lights and counts how many lights
are turned on when a file from the data directory is run with the
main.py file.


Description
===========

This project can be run with files that follow the format and structure of the files in the data directory
of this project.
To run this project enter the following command into the command line:
pip install git+https://github.com/MuireannMacCarthy/led_tester.git

To run with a file from the data directory such as for example to run with the test_data.txt use the following
commands in the command line:
python main.py --input ./data/test_data.txt

The output of running main.py with an input files will be the number of lights that are turned on.

Note
====

This project has been set up using PyScaffold 3.0.1. For details and usage
information on PyScaffold see http://pyscaffold.org/.
