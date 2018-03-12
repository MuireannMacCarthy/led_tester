"""
@author: Muireann
"""
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='input help')
args = parser.parse_args()

filename = args.input
def parseFile(input):
    if input.startswith('http'):
        pass
        #return None, None
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
        #return None, None
    return