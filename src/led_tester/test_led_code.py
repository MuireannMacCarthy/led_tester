import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
import led_tester
from led_tester import cli
from led_tester import utils
from led_tester import Grid
from led_tester import main

def test_get_size():
    ifile = "data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def test_parse_file():
    ifile = "data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == [['turn on', 0, 0, 9, 9],
                              ['turn off', 0, 0, 9, 9],
                              ['switch', 0, 0, 9, 9],
                              ['turn off', 0, 0, 9, 9],
                              ['turn on', 2, 2, 7, 7]]

def test_output():
    ifile = "data/test_data.txt"
    N, instructions, counter = Grid.makeGrid(ifile)
    assert counter == 9