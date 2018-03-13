import sys
sys.path.append('.')
import pytest
from click.testing import CliRunner
import led_tester
from led_tester import cli
from led_tester import utils

def test_command_line_interface():
    ifile = "data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N is not None

def test_read_file():
    ifile = "data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    assert N == 10
    assert instructions == [['turn', 'on', '0,0', 'through', '9,9'], ['turn', 'off', '0,0', 'through', '9,9'], ['switch', '0,0',
                            'through', '9,9'], ['turn', 'off', '0,0', 'through', '9,9'], ['turn', 'on', '2,2', 'through',
                            '7,7'], []]
