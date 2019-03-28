# (optional) TDD 2

# Objectives:
# Practice using setUp()
# Gain familiarity with how to set up tests for our code
# Understanding how to use TDD is extremely helpful, especially if 
# you're interested in joining a large company where TDD is used very heavily.  
# Get more practice using TDD by re-doing the MathDojo assignment but with TDD this time.  
# Make sure you use the setUp() method this time 
# (to create an instance of the MathDojo before the tests are run).

# Then create a new instance called md. 
# It should be able to do the following task:
#     md.add(2).add(2,5,1).subtract(3,2).result
#     which should perform 0+2+(2+5+1)-(3+2) and return 5.
# print("md.add(2).add(2,5,1).subtract(3,2).result should perform 0+2+(2+5+1)-(3+2) and return 5:")
# md = MathDojo("math boye")
# print(md.add(2).add(2,5,1).subtract(3,2).result())

import unittest
# import math 

class MathDojo():
    def __init__(self):
        self.myresult = 0
    def clear(self):
        self.myresult = 0
        return self
    def add(self, *value):
        for i in value:
            self.myresult += i
        return self
    def subtract(self, *value):
        for i in value:
            self.myresult -= i
        return self
    def result(self):
        temp = self.myresult
        self.myresult = 0
        return temp


class math_dojo_tests(unittest.TestCase):
    def setUp(self):
        # add the setUp tasks
        # print("running setUp")
        self.md1 = MathDojo()

    def testmda(self):
        return self.assertEqual(self.md1.add(5,18).result(),23)
    def testmdb(self):
        return self.assertEqual(self.md1.add(2).add(2,5,1).subtract(3,2).result(),5)
    def testmdc(self):
        return self.assertEqual(self.md1.add(0,2,(2+5+1),-(3+2)).result(),5)


    # any task you want run before any method above is executed, put them in the setUp method
    # # any task you want run after the tests are executed, put them in the tearDown method
    # def tearDown(self):
    #     add the tearDown tasks
    #     print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests


# output:
# 16:37:40 bart ~/projects/cd/python/pyfun (master)
# $ python math_dojo_tdd.py
# ...
# ----------------------------------------------------------------------
# Ran 3 tests in 0.000s


