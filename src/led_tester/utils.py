"""
@author: Muireann
"""

def parseFile(input):
    if input.startswith('http'):
        pass
    else:
        n, instructions = None, []
        with open(input, 'r') as f:
            n = int(f.readlines())
            for line in f.readlines():
                instructions.append(line)
        return n, instructions
    return