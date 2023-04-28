#adding parameter to the constructor
'''Create a class called NumberSet that accepts 2 integers as input, and defines
two instance variables: num1 and num2, which hold each of the input integers.
Then, create an instance of NumberSet where its num1 is 6 and its num2 is 10.
Save this instance to a variable t.'''

class NumberSet():
    def __init__(self,initnum1,initnum2):
        self.num1 = initnum1
        self.num2 = initnum2


t = NumberSet(6,10)
