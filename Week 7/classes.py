from math import *
class Point:
    def __init__(self, a = 0, b = 0):
        self.r = sqrt(a*a + b*b)
        if a == 0:
            self.theta = 0
        else:
            self.theta = atan(b/a)
    def odistance(self):
        return(self.r):

    def translate(self, deltax, deltay):
        pass
        # convert (r, theta) to (x,y) and return

