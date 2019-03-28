# Assignment: MathDojo

# Objectives:
#     Practice creating a class and creating new instances
#     Practice chaining methods
#     Practice writing flexible functions that can take a variable number of arguments

# HINT: To do this exercise, you will probably have to use 'return self'. 
# If the method returns itself (an instance of itself), we can chain methods.

# Create a Python class called MathDojo that has the methods add and subtract. 
# Have these 2 functions take at least 1 parameter.

# Then create a new instance called md. 

# It should be able to do the following task:
#     md.add(2).add(2,5,1).subtract(3,2).result
#     which should perform 0+2+(2+5+1)-(3+2) and return 5.

class MathDojo():
    def __init__(self, name):
        self.myresult = 0
        self.name = name
    def add(self, *value):
        for i in value:
            self.myresult += i
        return self
    def subtract(self, *value):
        for i in value:
            self.myresult -= i
        return self
    def result(self):
        return self.myresult

# Then create a new instance called md. 
# It should be able to do the following task:
#     md.add(2).add(2,5,1).subtract(3,2).result
#     which should perform 0+2+(2+5+1)-(3+2) and return 5.
print("md.add(2).add(2,5,1).subtract(3,2).result should perform 0+2+(2+5+1)-(3+2) and return 5:")
md = MathDojo("math boye")
print(md.add(2).add(2,5,1).subtract(3,2).result())


# OUTPUT
# 12:14:26 bart ~/projects/cd/python/pyfun (master)
# $ python clsMathDojo.py
# md.add(2).add(2,5,1).subtract(3,2).result should perform 0+2+(2+5+1)-(3+2) and return 5:
# 5

