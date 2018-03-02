import sys
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