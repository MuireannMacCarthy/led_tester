from led_tester import utils
counter = 0
# class LED:
#     def __init__(self, size):
#         self.size = size
#
#     def makeGrid(self, self.size):
#         self.size = N
#         a2d = [[0] * N for _ in range(N)]
#         return a2d, checkCommand(a2d)

def makeGrid(size):
    size = N
    a2d = [[0] * N for _ in range(N)]
    return a2d, checkCommand(a2d)

def checkCommand(a2d):
    for line in a2d:
        if line[0] == "turn on":
            line.remove("turn on")
            return turnOn(a2d)
        if line[0] == "turn off":
            line.remove("turn off")
            return turnOff(a2d)
        if line[0] == "switch":
            line.remove("switch")
            return switch(a2d)


def turnOn(a2d):
    x1 = a2d[0]
    y1 = a2d[1]
    x2 = a2d[2]
    y2 = a2d[3]
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            a2d[i][j] = 1
    return a2d


def turnOff(a2d):
    x1 = a2d[0]
    y1 = a2d[1]
    x2 = a2d[2]
    y2 = a2d[3]
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            a2d[i][j] = 0
    return a2d

def switch(a2d):
    x1 = a2d[0]
    y1 = a2d[1]
    x2 = a2d[2]
    y2 = a2d[3]
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
    x1 = a2d[0]
    y1 = a2d[1]
    x2 = a2d[2]
    y2 = a2d[3]
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)
    for i in range(xmin, xmax + 1):
        for j in range(ymin, ymax + 1):
            if a2d[i][j] == 1:
                counter += 1
    return counter

    if __name__ == "__main__":
        pprint(makeGrid(N))
