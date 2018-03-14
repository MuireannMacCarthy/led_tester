import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
import led_tester
from led_tester import cli
from led_tester import utils
from led_tester import main

def test_command_line_interface():
    ifile = "data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def test_read_file():
    ifile = "data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == [['turn on', 0, 0, 9, 9],
                              ['turn off', 0, 0, 9, 9],
                              ['switch', 0, 0, 9, 9],
                              ['turn off', 0, 0, 9, 9],
                              ['turn on', 2, 2, 7, 7]]
           #['turn', 'on', '0,0', 'through', '9,9\n', 'turn', 'off', '0,0', 'through', '9,9\n', 'switch',
            #                '0,0', 'through', '9,9\n', 'turn', 'off', '0,0', 'through', '9,9\n', 'turn', 'on', '2,2',
             #               'through', '7,7\n', '\n']
           #





# def test_get_commands():
#     ifile = "data/test_data.txt"
#     newArray = main.getCommands(ifile)
#     #newArray = main.getCommands([['turn', 'on', '0,0', 'through', '9,9'], ['turn', 'off', '0,0', 'through', '9,9'],
#      #                            ['switch', '0,0', 'through', '9,9'], ['turn', 'off', '0,0', 'through', '9,9'],
#       #                           ['turn', 'on', '2,2', 'through', '7,7'], []])
#     assert newArray == [['turn on', '0', '0', '9', '9'], ['turn off', '0', '0', '9', '9'], ['switch', '0', '0', '9', '9'],
#                         ['turn off', '0', '0', '9', '9'], ['turn on', '2', '2', '7', '7']]