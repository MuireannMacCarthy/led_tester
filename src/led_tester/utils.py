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
    else:
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                values = line.strip().split()
                instructions.append(values)
        return N, instructions
    return