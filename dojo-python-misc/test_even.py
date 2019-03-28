# import the python testing framework
import unittest
# our "unit"
# this is what we are running our test on
def isEven(n):
    if n % 2 == 0:
       return True
    else:
       return False
# our "unit tests"
# initialized by creating a class that inherits from unittest.TestCase
class IsEvenTests(unittest.TestCase):
    # each method in this class is a test to be run
    def testTwo(self):
        self.assertEqual(isEven(2), True)
        # another way to write above is
        self.assertTrue(isEven(2))
    def testThree(self):
        self.assertEqual(isEven(3), False)
        # another way to write above is
        self.assertFalse(isEven(3))
    # any task you want run before any method above is executed, put them in the setUp method
    def setUp(self):
        # add the setUp tasks
        print("running setUp")
    # any task you want run after the tests are executed, put them in the tearDown method
    def tearDown(self):
        # add the tearDown tasks
        print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests




# In the example, above we used assertTrue() and assertFalse(), which introduce the first couple of 
# many functions/assertions available in the unittest framework. We will touch on a handful of 
# these as we progress, but here is a good reference: unittest functions

# Running unittest
# Before anything else, let's examine how we run our tests:

# if __name__ == '__main__':
#     unittest.main()


# By including these two lines, we can run our test code by executing our python file. 
# Running it with no options results in a simple output but running this file with the -v 
# flag will give you the verbose output with information on each test that was run:

# https://s3.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/Screen_Shot_2018-03-23_at_10.33.14_AM.png


# Test Outcomes
# When we run our tests, there are 3 possible outcomes:

# OK - all tests have passed
# FAIL - one or more of the tests have failed, and raises an AssertionError exception
# ERROR - the test raises an exception other than AssertionError

# In the typical TDD workflow:

# Think of Feature->Write Tests->Run & Fail->Code->Run & Pass->Refactor->Repeat

# Other Useful Assertions
# If you understood the code above, implementing the other assertions are quite straight 
# forward. Here is a list of some of the other useful assertions directly from the Python doc:

# https://s3.amazonaws.com/General_V88/boomyeah2015/codingdojo/curriculum/content/chapter/Screen_Shot_2018-03-23_at_10.37.08_AM.png

# Although this list is not exhaustive, keep an eye out for some of these as we continue along. 
# If you're curious about the above or want to see all available assertions, you can check out the 
# python doc - Test Cases & Assertions
# https://docs.python.org/3.6/library/unittest.html#test-cases


