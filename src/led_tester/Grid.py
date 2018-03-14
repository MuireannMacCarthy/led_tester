from pprint import pprint
import utils

counter = 0

def makeGrid(size):
    a2d = [[0] * size for _ in range(size)]
    return a2d

def checkSize(array, size):
    limit = int(len(array))
    for i in range(1, limit - 1):
        ls = int(array[i])
        if ls > 0 or ls < size:
            print("too big")
            pass
        else:
            checkCommand(array)

def checkCommand(array, a2d):
    for line in array:
        print(line[0])
        if line[0] == "turn on":
            line.remove("turn on")
            return turnOn(line, a2d)
        if line[0] == "turn off":
            line.remove("turn off")
            return turnOff(line)
        if line[0] == "switch":
            line.remove("switch")
            return switch(line)
        print("test one")



def turnOn(array, a2d):
    x1 = int(array[0])
    y1 = int(array[1])
    x2 = int(array[2])
    y2 = int(array[3])
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            a2d[i][j] = 1
    print("test two")
    return a2d


def turnOff(a2d):
    x1 = int(array[0])
    y1 = int(array[1])
    x2 = int(array[2])
    y2 = int(array[3])
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            a2d[i][j] = 0
    print(x1, y1)
    return a2d

def switch(a2d):
    x1 = int(array[0])
    y1 = int(array[1])
    x2 = int(array[2])
    y2 = int(array[3])
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            if a2d[i][j] == 1:
                a2d[i][j] = 0
            if a2d[i][j] == 0:
                a2d[i][j] = 1
    return a2d

def countLights(a2d, counter):
    x1 = int(array[0])
    y1 = int(array[1])
    x2 = int(array[2])
    y2 = int(array[3])
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            if a2d[i][j] == 1:
                counter += 1
    return counter
    print("the counter is", counter)

if __name__ == "__main__":
    pprint(makeGrid(10))
 #   makeGrid(size)
  #  checkSize(array, size)


