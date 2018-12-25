class Point:
    def __init__(self, xPos = 0, yPos = 0):
        self.x = xPos
        self.y = yPos

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

import math

class Line:
    def __init__(self, Point1, Point2):
        self.p1 = Point1
        self.p2 = Point2

    def length(self):
        # p1 = start, p2 = end
        return math.sqrt(math.pow(self.p1.x - self.p2.x, 2) + math.pow(self.p1.y - self.p2.y, 2))

    def __str__(self):
        return str(self.p1) + " to " + str(self.p2)

def main():
    p1 = Point()
    print(p1)
    p2 = Point(3, 4)
    print(p2)
    p3 = Point(-8, -6)
    print(p3)
    line1 = Line(p1, p2)
    print(line1)
    print(line1.length())
    line2 = Line(p1, p3)
    print(line2)
    print(line2.length())

if __name__ == "__main__":
    main()