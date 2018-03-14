import led_tester
import sys
from led_tester import utils
from led_tester import Grid






if __name__ == "__main__":

    print(sys.argv)
    file_name = sys.argv[2]
    print(utils.parseFile(file_name))