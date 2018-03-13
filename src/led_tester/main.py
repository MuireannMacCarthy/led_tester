import led_tester
from led_tester import utils
import re
from led_tester import Grid

def getCommands(array):
    """
    function to get commands from list and numbers from list
    """
    for i in array:
        #numbers = re.match("(.*)(\d+),(\d+) through (\d+),(\d+)", elem)
        #cmd = re.findall(".*(turn on|turn off|switch).*", i)
        check = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?"
                         "\d+).*")
        mat = re.search(check, i)
        #newArray = []
        if mat:
            newArray = []
            newArray.append(mat.group(1))
            newArray.append(int(mat.group(2)))
            newArray.append(int(mat.group(3)))
            newArray.append(int(mat.group(4)))
            newArray.append(int(mat.group(5)))
            newArray.strip().split()


            return newArray
    return
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