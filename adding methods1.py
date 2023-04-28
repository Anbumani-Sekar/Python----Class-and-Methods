#adding another method to class
'''Note that the getX method simply returns the value of the instance variable x
from the object self. In other words, the implementation of the method is to go
to the state of the object itself and get the value of x. Likewise, the getY
method looks almost the same.
Let’s add another method, distanceFromOrigin, to see better how methods work.
This method will again not need any additional information to do its work,
beyond the data stored in the instance variables.
It will perform a more complex task'''
class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5


p = Point(7,6)
print(p.distanceFromOrigin())
