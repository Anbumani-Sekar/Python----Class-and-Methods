'''20.8. Instances as Return Values
Functions and methods can return objects.
This is actually nothing new since everything in Python is an object and
we have been returning values for quite some time. (You can also have lists or
tuples of object instances, etc.) The difference here is that we want to have
the method create an object using the constructor and then return it as the
value of the method.

Suppose you have a point object and wish to find the midpoint halfway between
it and some other target point. We would like to write a method, let’s call it
halfway, which takes another Point as a parameter and returns the Point that is
halfway between the point and the target point it accepts as input.'''

class Point:

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)

p = Point(3,4)
q = Point(5,12)
mid = p.halfway(q)
# note that you would have exactly the same result if you instead wrote
# mid = q.halfway(p)
# because they are both Point objects, and the middle is the same no matter what

print(mid)
print(mid.getX())
print(mid.getY())
