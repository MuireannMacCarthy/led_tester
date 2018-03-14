import led_tester
import sys
from led_tester import utils
import re
from led_tester import Grid


#if 'turn' in elem:
         #   elem.remove('turn')
        #a, b, c, d = elem.strip().split()



#References
#https://www.dotnetperls.com/re-python
#https://docs.python.org/3/howto/regex.html

# coordinates = re.findall("\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*", i)
# x1 = coordinates[0]
# y1 = coordinates[1]
# x2 = coordinates[2]
# y2 = coordinates[3]
# command = re.match(".*(turn on|turn off|switch).*", elem)
# if command:
#   cmd = array[0]

if __name__ == "__main__":

    print(sys.argv)
    file_name = sys.argv[2]
    print(utils.parseFile(file_name))