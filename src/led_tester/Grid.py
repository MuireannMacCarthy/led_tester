from pprint import pprint
from led_tester import utils

global counter
counter = 0

def checkSize(array, size):
    """
    function to check the the integers parsed through are positive numbers and not greater than the
    size of the grid
    """
    a2d = [[0] * size for _ in range(size)]
    for line in array:
        if line[0] == "turn on":
            line.remove("turn on")
        if line[0] == "turn off":
            line.remove("turn off")
        if line[0] == "switch":
            line.remove("switch")
        limit = int(len(line))
        for i in range(0, limit - 1):
            ls = int(line[i])
            if ls < 0 or ls > size:
                print("too big")
                pass
            else:
                checkCommand(array, a2d)
    return countLights(a2d, counter)

def checkCommand(array, a2d):
    """
    function to check the command in the array and call the relevent function corresponding to each
    command
    """
    for line in array:
        if line[0] == "turn on":
            line.remove("turn on")
            return turnOn(line, a2d)
        if line[0] == "turn off":
            line.remove("turn off")
            return turnOff(line, a2d)
        if line[0] == "switch":
            line.remove("switch")
            return switch(line, a2d)
    #return countLights(a2d, counter)


def turnOn(array, a2d):
    """
    function to turn on lights, i.e. change 0's to 1's for the given coordinates
    """
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
    return a2d
        #, countLights(a2d, array, counter)


def turnOff(array, a2d):
    """
    function to turn off lights with given coordinates from array
    """
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
    return a2d
        #, countLights(a2d, array, counter)

def switch(array, a2d):
    """
    function to switch lights that are on off, and switch lights that are off on with given coordinates
    from array
    """
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
        #, countLights(a2d, array, counter)


def countLights(a2d, counter):
    """
    function to iterate through the grid and count how many lights are turned 
    """
    # x1 = int(array[0])
    # y1 = int(array[1])
    # x2 = int(array[2])
    # y2 = int(array[3])
    # xmin = min(x1, x2)
    # xmax = max(x1, x2)
    # ymin = min(y1, y2)
    # ymax = max(y1, y2)
    for i in range(0, len(a2d)):
        for j in range(0, len(a2d)):
            if a2d[i][j] == 1:
                counter += 1
    # for i in range(xmin, xmax + 1):
    #     for j in range(ymin, ymax + 1):
    #         if a2d[i][j] == 1:
    #             counter += 1
    print("the counter is", counter)
    return counter


#print("the counter is", counter)

#if __name__ == "__main__":
    #pprint(makeGrid(10))
 #   makeGrid(size)
  #  checkSize(array, size)


