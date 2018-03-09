import sys
import led_tester
sys.path.append('.')
import pytest
from click.testing import CliRunner
from led_tester import led_tester
from led_tester import Cli
from led_tester import parse

def test_command_line_interface():
    ifile = "./data/test_data.txt"
    N, instructions = parse.parseFile(ifile)
    assert N is not None

def test_read_file():
    ifile = "./data/test_data.txt"
    N, instructions = parse.parseFile(ifile)
    assert N == 10
    assert instructions == ['turn on 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'switch 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn off 0,0 through 9,9\n', 'turn on 2,2 through 7,7\n']