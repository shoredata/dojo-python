# Intro to TDD assignment
# =======================

import unittest
import math 

# Objectives:
# Write a function and tests to determine whether it works as expected

# Now that you've learned how to use unittest, let's have you do the following:

# reverseList - Write a function that reverses the values in the list 
# (without creating a temporary array).  
# For example, reverseList([1,3,5]) should return [5,3,1].  
# In other words assertEqual( reverseList[1,3,5], [5,3,1] ).  
# Create at least 3 other test cases before you implement the functionality.
def reverselist(arr):
    for i in range(math.floor(len(arr)/2)):
        arr[i],arr[len(arr)-1-i] = arr[len(arr)-1-i],arr[i]
    return arr

# isPalindrome - Write a function that checks whether the given word is a 
# palindrome (a word that spells the same backward).  
# For example, isPalindrome("racecar") should return true.  
# Another way to say this is assertEqual( isPalindrome("racecar"), True ) or 
# assertTrue( isPalindrome("racecar")).  
# Similarly, assertFalse( isPalindrome("rabcr") ).  
# Add at least 5 other test cases before you implement the functionality.  
# Remember that you need to write the tests first, make sure the tests 
# fail, and then write the functionality within the function, to now make 
# all the tests pass.  
# (also remember that if a = "hello", a[0] returns 'h' and a[1] returns 'e').
def stringreverse(string):
    # 'hello world'[::-1]
    # 'dlrow olleh'
    # This is extended slice syntax. 
    # It works by doing [begin:end:step] - by leaving begin and end off and specifying a step of -1, it reverses a string.    
    return string[::-1]
def ispalindrome(word):
    return word==stringreverse(word)

# removeNegatives - Write a function that removes all the negative value 
# in the given list without creating a temporary array and only using pop() 
# (and a for loop).  
# For example, removeNegatives([1,3,-5,-7]) should return [1,3].  
# In other words, assertEqual( removeNegatives[1,3,-5,-7], [1,3]).  
# Add other test cases as well and make sure all the tests fail before you 
# start writing any codes within removeNegatives.
def removenagatives(arr):    
    iremoved = 0
    for i in range(len(arr)):
        if (arr[i]<0):
            for j in range(0,len(arr)-i-1):
                arr[i+j]=arr[i+j+1]
            iremoved += 1
    for i in range(1, iremoved+1, 1):
        arr.pop()
    return arr

# coins - Write a function that determines how many quarters, dimes, 
# nickels, and pennies to give to a customer for a change where you 
# minimize the number of coins you give out.  For example, if you need 
# to give the customer 87 cents, you can give 3 quarters, 1 dime, 0 nickel 
# and 2 pennies.  If you need to give the customer 92 cents, you can give 
# 3 quarters, 1 dime, 1 nickel, and 2 pennies.  
# Write the function such that for example, coin(87) returns [3,1,0,2].  
# coin(92) should return [3,1,1,2].  
# Add at least 5 other test cases first, before you fill in the codes inside function coin().
def coins(change):
    retn = []
    q = math.floor(change/25)
    change -= q*25
    d = math.floor(change/10)
    change -= d*10
    n = math.floor(change/5)
    change -= n*5
    p = math.floor(change)
    change -= p    
    retn.append(q)
    retn.append(d)
    retn.append(n)
    retn.append(p)    
    return retn

# Factorial (hacker challenge).  
# Write a function factorial() that returns the factorial of the given number.  
# For example, factorial(5) should return 120.  Do this using recursion; 
# remember that factorial(n) = n * factorial(n-1).
def factorial(num):
    if num==1:
        return 1
    else:
        return num * factorial(num-1)

# Fib (hacker challenge). Write a function fib() in Python that returns the 
# appropriate Fibonacci number.  Do this using recursion.  
# Let's say that the first two Fibonacci numbers are 0 and 1.  
# Remember that fib(n) = fib(n-2) + fib(n-1).
# n 	f(n)
# ---------
# 0  	0
# 1  	1
# 2 	1
# 3 	2
# 4 	3
# 5	    5
# 10	55
# 15	610
# 27	196418
def fibonacci(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibonacci(num-2) + fibonacci(num-1)


# Implement the insert_val_at function
def insert_val_at(arr,idx,val):
    arr.append(0)
    # print('\n',arr)
    for i in range(len(arr)-1, idx, -1):
        # print(i, arr[i], arr[i-1])
        arr[i]=arr[i-1]
        # print(arr)
    arr[idx]=val
    # print(arr)
    return arr

# For the purpose of this assignment, do all of these in a single Python file.  
# If you had your tests in allTests.py but all your functions say in myHomework.py, 
# you could import all the functions from your file by doing something like this.

# allTests.py::
# =================================================================
# import unittest
# from myHomework import reverseList, isPalindrome, removeNegatives
# class reverseListTest(unittest.TestCase):
#     def test1(self):
#         return self.assertEqual(reverseList([1,3,5]), [5,3,1])
#     def test2(self):
#         return self.assertEqual(reverseList(2,4,-3), [-3,4,2])
# class isPalindromeTest(unittest.TestCase):
#     def test1(self):
#        return self.assertEqual(isPalindrome("racecar"), True)
#     def test2(self):
#        return self.assertEqual(isPalindrome("rabbit", False))
# if __name__ == "__main__":
#     unittest.main()


class rev_list_tests(unittest.TestCase):
    # each method in this class is a test to be run

    def testfac1(self):
        return self.assertEqual(factorial(5),120)
    def testfac2(self):
        return self.assertEqual(factorial(10),3628800)
    def testfac3(self):
        return self.assertEqual(factorial(1),1)
    def testfac4(self):
        return self.assertEqual(factorial(2),2)

    def testfib1(self):
        return self.assertEqual(fibonacci(1),1)
    def testfib2(self):
        return self.assertEqual(fibonacci(5),5)
    def testfib3(self):
        return self.assertEqual(fibonacci(10),55)
    def testfib4(self):
        return self.assertEqual(fibonacci(27),196418)

    def testrevl1(self):
        return self.assertEqual(reverselist([1,3,5]), [5,3,1])
    def testrevl2(self):
        return self.assertEqual(reverselist([-1,0,1]), [1,0,-1])
    def testrevl3(self):
        return self.assertEqual(reverselist(['dojo',0,'coding',5]), [5,'coding',0,'dojo'])
    def testrevl4(self):
        return self.assertEqual(reverselist([1]), [1])
    def testrevl5(self):
        return self.assertEqual(reverselist([]), [])

    def testpal1(self):
        return self.assertEqual(ispalindrome("racecar"), True)
    def testpal2(self):
        return self.assertEqual(ispalindrome("rabbit"), False)
    def testpal3(self):
        return self.assertEqual(ispalindrome(""), True)

    def testsr1(self):
        return self.assertEqual(stringreverse("racecar"), "racecar")
    def testsr2(self):
        return self.assertEqual(stringreverse("rabbit"), "tibbar")
    def testsr3(self):
        return self.assertEqual(stringreverse(""), "")

    def testrn1(self):
        return self.assertEqual(removenagatives([1,3,-5,-7]), [1,3])
    def testrn2(self):
        return self.assertEqual(removenagatives([-5,-7]), [])

    def testcoin1(self):
        return self.assertEqual(coins(92), [3,1,1,2])
    def testcoin2(self):
        return self.assertEqual(coins(87), [3,1,0,2])
    def testcoin3(self):
        return self.assertEqual(coins(126), [5,0,0,1])
    def testcoin4(self):
        return self.assertEqual(coins(10), [0,1,0,0])
    def testcoin5(self):
        return self.assertEqual(coins(1), [0,0,0,1])
    def testcoin6(self):
        return self.assertEqual(coins(17476), [699,0,0,1])

    def testiva1(self):
        return self.assertEqual(insert_val_at([0,1,2],1,187), [0,187,1,2])
    def testiva2(self):
        return self.assertEqual(insert_val_at([0,1,2],0,187), [187,0,1,2])
    def testiva3(self):
        return self.assertEqual(insert_val_at([0,1,2],2,187), [0,1,187,2])
    def testiva4(self):
        return self.assertEqual(insert_val_at([0,1,2],3,187), [0,1,2,187])



    # any task you want run before any method above is executed, put them in the setUp method
    # def setUp(self):
    #     # add the setUp tasks
    #     print("running setUp")
    # # any task you want run after the tests are executed, put them in the tearDown method
    # def tearDown(self):
    #     add the tearDown tasks
    #     print("running tearDown tasks")
if __name__ == '__main__':
    unittest.main() # this runs our tests


# OUTPUT:
# $ python intro_to_tdd.py
# ...............................
# ----------------------------------------------------------------------
# Ran 31 tests in 0.090s
# OK


# Additional Information about import
# Difference between "import" vs "from ___ import":
# https://stackoverflow.com/questions/9439480/from-import-vs-import

# Later when your file contains a lot of functions: 
# https://stackoverflow.com/questions/6761825/importing-multiple-functions-from-a-python-module

