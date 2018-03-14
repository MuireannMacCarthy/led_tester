"""
@author: Muireann
"""
import argparse
import re
# parser = argparse.ArgumentParser()
# parser.add_argument('--input', help='input help')
# args = parser.parse_args()
from pprint import pprint

# filename = args.input
def parseFile(input):
    if input.startswith('http'):
        pass
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                #values = line.strip().split()
                instructions.append(line)
        return N, getCommands(instructions)
    return

def getCommands(array):
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
            # newArray.append(int(mat.group(2)))
            # newArray.append(int(mat.group(3)))
            # newArray.append(int(mat.group(4)))
            # newArray.append(int(mat.group(5)))
            # newArray.strip().split()

            instructions.append(newArray)

    return instructions

if __name__ == "__main__":
    pprint(parseFile("../../../data/test_data.txt"))