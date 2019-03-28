# Optional Assignment: Underscore

# Objectives:
# Create a custom Python module using OOP
# Your own custom Python Module!

# Did you know that you can actually create your own custom python module similar to the 
# Underscore library in JavaScript? That may be hard to believe, as the things you've 
# learned might seem simple (again, we try to make it look simple... (-: ), but in truth, 
# you know how to create significant Python modules of your own. To create a custom Python 
# module, you will simply add methods to a Python class!

# You will create the following methods from the underscore library as methods of the 
# "_" object. Pay attention to what you have to change, in terms of parameters for 
# each method as well as implementation.

# class Underscore:
#     def map(self):
#         # your code here
#     def reduce(self):
#         # your code here
#     def find(self):
#         # your code here
#     def filter(self):
#         # your code
#     def reject(self):
#         # your code
# # you just created a library with 5 methods!
# # let's create an instance of our class

# _ = Underscore() # yes we are setting our instance to a variable that is an underscore
# evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# # should return [2, 4, 6] after you finish implementing the code above

# In the code above, you just created your own custom Python module/library that others 
# can use! How can others use the methods in your library? By calling the properties 
# stored in the class you defined (e.g. _.map(), _. reduce(), _.find(), etc).

# Your assignment is to implement the 5 methods above using delegating callbacks. 
# You will have to modify the 5 methods to take in an array and a callback. 
# Use what you learned in the previous chapter about callbacks to complete the assignment.

# One important concept that we want you to learn through this assignment is how to pass data to 
# and from callbacks. You pass data to a callback with a parameter and you pass data from the 
# callback back to the parent function with a return. While you are going through this assignment 
# pay close attention to this relationship.

# To understand what each method does, please refer to the underscore library. 
# Note that your method does not have to be as robust as underscore's; you just 
# need to get the base functionality working. Therefore for most methods you will only have 
# the list and a lambda as parameters, and for the lambda you will pass in each element and 
# potentially a "memo" also known as a "collector".

# Note that some of these functions already exist in Python. 
# We want you to explore how you might implement these yourself. 
# Be aware that these tools exist to help work in a design idiom known as 
# "functional programming". It's not something that we cover here, but is a topic 
# you may want to explore on your own. It is mainly used in data science in recent years.

# refer to this for functions:
# http://underscorejs.org/

import datetime 

class Underscore:
    def __init__(self):
        self.created_at = datetime.datetime.now()

    def map(self, list, callback):
        # Produces a new array of values by mapping each value in list 
        # through a transformation function (iteratee). 
        new = []
        for i in list:
            new.append(callback(i))
        print(new)
        return new
        
    def reduce(self, list, callback, memo=0):
        # Also known as inject and fold, reduce boils down a list of values into a single value. 
        # Memo is the initial state of the reduction, and each successive step of it should be returned by iteratee. 
        # The iteratee is passed four arguments: the memo, then the value and index (or key) of the iteration, 
        # and finally a reference to the entire list.
        # If no memo is passed to the initial invocation of reduce, the iteratee is not invoked on the first 
        # element of the list. The first element is instead passed as the memo in the invocation of the 
        # iteratee on the next element in the list.
        if memo==0:
            reduced = list[0]
        else:
            reduced = callback(memo,list[0])
        for i in list[1:]:
            reduced = callback(reduced, i)
        print(reduced)
        return reduced

    def find(self, list, callback):
        # Looks through each value in the list, returning the first one that passes a truth test (predicate), 
        # or undefined if no value passes the test. The function returns as soon as it finds an acceptable element, 
        # and doesn't traverse the entire list. predicate is transformed through iteratee to facilitate shorthand syntaxes.
       for i in list:
            if callback(i):
                print(i)
                return i

    def filter(self, list, callback):
        # Looks through each value in the list, returning an array of all the values that pass a truth test 
        # (predicate). predicate is transformed through iteratee to facilitate shorthand syntaxes.
        new = []
        for i in list:
            if callback(i):
                new.append(i) 
        print(new)
        return new
            
    def reject(self, list, callback):
        # Returns the values in list without the elements that the truth test (predicate) passes. 
        # The opposite of filter. predicate is transformed through iteratee to facilitate shorthand syntaxes.
        new = []
        for i in list:
            if not callback(i):
                new.append(i) 
        print(new)
        return new


# you just created a library with 5 methods!
# let's create an instance of our class

_ = Underscore()
print("\nMAP: Transfrom Evens ==> True:\n  _.map([1, 2, 4, 6, 8], lambda x: x % 2 == 0)")
maps = _.map([1, 2, 4, 6, 8], lambda x: x % 2 == 0)

print("\nMAP: Multiply by 3: \n  _.map([1, 2, 3, 4, 5, 6], lambda x: x*3)")
multiplyBy3 = _.map([1, 2, 3, 4, 5, 6], lambda x: x*3)


print("\nFILTER: Return Multiples of 3: \n  _.filter([1, 2, 4, 6, 8], lambda x: x % 3 == 0)")
evens = _.filter([1, 2, 4, 6, 8], lambda x: x % 3 == 0)

print("\nREJECT: Reject Multiples of 10: \n  _.reject([1, 2, 4, 3, 6, 8, 10], lambda x: x % 10 == 0)")
odds = _.reject([1, 2, 4, 3, 6, 8, 10], lambda x: x % 10 == 0)

print("\nREJECT: Reject evens: \n  _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)")
odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)

print("\nFIND: Return First Odd: \n  _.find([2, 4, 6, 7, 8], lambda x: x % 2 == 1)")
findItem = _.find([2, 4, 6, 7, 8], lambda x: x % 2 == 1)

print("\nREDUCE: Return::Sum: \n  _.reduce([47,11,42,13], lambda x,y: x+y) ?? 113")
reduceItem = _.reduce([47,11,42,13], lambda x,y: x+y)

print("\nREDUCE: Return::Product: \n  _.reduce([47,11,42,102,13], lambda a,b: a if (a > b) else b) ?? 102")
multiplyAll = _.reduce([47,11,42,102,13], lambda a,b: a if (a > b) else b)

print("\nREDUCE: Return::X^Y: \n  _.reduce([2, 2, 3], lambda x,y: x**y)")
multiplyAll = _.reduce([2, 2, 3], lambda x,y: x**y)

print("\nREDUCE: Return::Sum: \n  _.reduce(range(1,101), lambda x, y: x+y) ?? sum(1:101)")
multiplyAll = _.reduce(range(1,101), lambda x, y: x+y)


# The function reduce(func, seq) continually applies the function func() to the sequence seq. It returns a single value. 
# If seq = [ s1, s2, s3, ... , sn ], calling reduce(func, seq) works like this:
# At first the first two elements of seq will be applied to func, i.e. func(s1,s2) The list on which reduce() works looks now like this: [ func(s1, s2), s3, ... , sn ]
# In the next step func will be applied on the previous result and the third element of the list, i.e. func(func(s1, s2),s3)
# The list looks like this now: [ func(func(s1, s2),s3), ... , sn ]
# Continue like this until just one element is left and return this element as the result of reduce()
# We illustrate this process in the following example:
# >>> reduce(lambda x,y: x+y, [47,11,42,13])
# 113
# Determining the maximum of a list of numerical values by using reduce:
# >>> f = lambda a,b: a if (a > b) else b
# >>> reduce(f, [47,11,42,102,13])
# 102
# >>> 
# Calculating the sum of the numbers from 1 to 100:
# >>> reduce(lambda x, y: x+y, range(1,101))
# 5050




# OUTPUT:

# 14:15:52 bart ~/projects/cd/python/pyfun (master)
# $ python underscore.py

# MAP: Transfrom Evens ==> True:
#   _.map([1, 2, 4, 6, 8], lambda x: x % 2 == 0)
# [False, True, True, True, True]

# MAP: Multiply by 3:
#   _.map([1, 2, 3, 4, 5, 6], lambda x: x*3)
# [3, 6, 9, 12, 15, 18]

# FILTER: Return Multiples of 3:
#   _.filter([1, 2, 4, 6, 8], lambda x: x % 3 == 0)
# [6]

# REJECT: Reject Multiples of 10:
#   _.reject([1, 2, 4, 3, 6, 8, 10], lambda x: x % 10 == 0)
# [1, 2, 4, 3, 6, 8]

# REJECT: Reject evens:
#   _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
# [1, 3, 5]

# FIND: Return First Odd:
#   _.find([2, 4, 6, 7, 8], lambda x: x % 2 == 1)
# 7

# REDUCE: Return::Sum:
#   _.reduce([47,11,42,13], lambda x,y: x+y) ?? 113
# 113

# REDUCE: Return::Product:
#   _.reduce([47,11,42,102,13], lambda a,b: a if (a > b) else b) ?? 102
# 102

# REDUCE: Return::X^Y:
#   _.reduce([2, 2, 3], lambda x,y: x**y)
# 64

# REDUCE: Return::Sum:
#   _.reduce(range(1,101), lambda x, y: x+y) ?? sum(1:101)
# 5050

