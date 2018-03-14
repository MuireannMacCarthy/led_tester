"""
@author: Muireann
"""
import argparse
import re
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='input help')
# args = parser.parse_args()
from pprint import pprint
from led_tester import Grid

# filename = args.input
def parseFile(input):
    if input.startswith('http'):
        pass
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, getCommands(instructions, N)
            #, Grid.makeGrid(N)
    return

def getCommands(array, N):
    """
    function to get commands from list and numbers from list
    """
    check = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]"
                       "?\d+).*")
    instructions = []
    for line in array:

        mat = re.search(check, line)

        if mat:
            newArray = []
            newArray.append(mat.group(1))
            for i in range(2, 6):
                newArray.append(int(mat.group(i)))

            instructions.append(newArray)

    return instructions, Grid.checkSize(instructions, N)


if __name__ == "__main__":
    #main()
    pprint(parseFile("../../../data/test_data.txt"))


#References
#https://www.dotnetperls.com/re-python
#https://docs.python.org/3/howto/regex.html