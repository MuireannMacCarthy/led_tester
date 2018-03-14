
def makeGrid(size):
    N = size
    a2d = [[0] * N for _ in range(N)]
    return a2d

def checkCommand(list, a2d):
for line in list:
    if line[0] == "turn on":
        line.remove("turn on")
        return turnOn(line, a2d)
    if line[0] == "turn off":
        line.remove("turn off")
        return turnOff(line, a2d)
    if line[0] == "switch":
        line.remove("switch")
        return switch(line, a2d)


def turnOn(line, a2d):
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]
    xmin = min(x1, x2)
    xmax = max(x1, x2)
    ymin = min(y1, y2)
    ymax = max(y1, y2)


def turnOff(line, a2d):
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]

def switch(line, a2d):
    x1 = line[0]
    y1 = line[1]
    x2 = line[2]
    y2 = line[3]




    #class LED:
    #def __init__(self, size):
     #   self.size = size
      #  self.command = self.command
   # def createGrid(self, self.size):
    #def checkCommand(self, self.command):
     #   if self.command == 'turn on':
#        if self.command == 'turn off':
 #       if self.command == 'switch':
  #  def turnOn(self)