# For Loop Basic II

# Objectives
# Get comfortable writing functions only using basic building blocks of Python 
# (we want you to gain confidence in your ability to write custom functions 
# instead of relying too heavily on advanced built in python functions
# Get comfortable using for loops, functions, lists, and other data types

# Biggie Size - Given an array, write a function that changes all positive 
# numbers in the array to "big". Example: makeItBig([-1, 3, 5, -5]) returns 
# that same array, changed to [-1, "big", "big", -5].
def makeitbig(arr):
    for i in range(len(arr)):
        if (arr[i]>0):
            arr[i]="big"
    return arr
print(f"makeitbig([-1,3,5,-5]): {makeitbig([-1,3,5,-5])}")

# Count Positives - Given an array of numbers, create a function to replace 
# last value with number of positive values. Example, countPositives([-1,1,1,1]) 
# changes array to [-1,1,1,3] and returns it.  (Note that zero is not considered to b a positive number).
def countpositives(arr):
    count = 0
    for i in range(len(arr)):
        if (arr[i]>0):
            count+=1
    arr[-1]=count
    return arr
print(f"countpositives([-1,1,1,1]): {countpositives([-1,1,1,1])}")

# SumTotal - Create a function that takes an array as an argument and returns 
# the sum of all the values in the array.  For example sumTotal([1,2,3,4]) should return 10
def sumtotal(arr):
    sum=0
    for i in arr:
        sum+=i
    return sum
print(f"sumtotal([1,2,3,4]?=10): {sumtotal([1,2,3,4])}")

# Average - Create a function that takes an array as an argument and returns 
# the average of all the values in the array.  For example multiples([1,2,3,4]) should return 2.5
def averagearray(arr):
    sum=0
    for i in arr :
        sum += i
    return sum / len(arr )
print(f"averagearray([1,2,3,4]?=2.5): {averagearray([1,2,3,4])}")

# Length - Create a function that takes an array as an argument and returns 
# the length of the array.  For example length([1,2,3,4]) should return 4
def lengtharray(arr):
    count=0
    for i in arr :
        count += 1
    return count 
print(f"lengtharray([1,2,3,4]?=4): {lengtharray([1,2,3,4])}")

# Minimum - Create a function that takes an array as an argument and returns 
# the minimum value in the array.  If the passed array is empty, have the
# function return false.  For example minimum([1,2,3,4]) should return 1; minimum([-1,-2,-3]) should return -3.
def minarray(arr):
    min=arr[0]
    for i in arr:
        if (i<min):
            min = i
    return min
print(f"minarray([1,2,3,4]?=1): {minarray([1,2,3,4])}")
print(f"minarray([-1,-2,-3]?=-3): {minarray([-1,-2,-3])}")

# Maximum - Create a function that takes an array as an argument and returns 
# the maximum value in the array.  If the passed array is empty, have the 
# function return false.  For example maximum([1,2,3,4]) should return 4; maximum([-1,-2,-3]) should return -3.
def maxarray(arr):
    max=arr[0]
    for i in arr:
        if (i>max):
            max = i
    return max
print(f"maxarray([1,2,3,4]?=4): {maxarray([1,2,3,4])}")
print(f"maxarray([-1,-2,-3]?=-1): {maxarray([-1,-2,-3])}")

# UltimateAnalyze - Create a function that takes an array as an argument and 
# returns a dictionary that has the sumTotal, average, minimum, maximum and length of the array.
def ultimateanalyze(arr):
    ret = {}
    ret['sumtotal']=sumtotal(arr)
    ret['average']=averagearray(arr)
    ret['minimum']=minarray(arr)
    ret['maximum']=maxarray(arr)
    ret['length']=lengtharray(arr)
    return ret
print(f"ultimateanalyze([1,2,3,4]): {ultimateanalyze([1,2,3,4])}")
print(f"ultimateanalyze([-1,-2,-3]): {ultimateanalyze([-1,-2,-3])}")

# ReverseList - Create a function that takes an array as an argument and return 
# an array in a reversed order.  Do this without creating an empty temporary array.  
# For example reverse([1,2,3,4]) should return [4,3,2,1]. 
# This challenge is known to appear during basic technical interviews.
import math
def revarray(arr):
    # for i in range(math.floor(len(arr)/2)):
    #     temp = arr[i]
    #     arr[i]=arr[len(arr)-i-1]
    #     arr[len(arr)-i-1] = temp
    # return arr 
    # return "".join(reversed(arr))   
    return arr[::-1]
print(f"revarray([1,2,3,4]): {revarray([1,2,3,4])}")
print(f"revarray([-1,-2,-3]): {revarray([-1,-2,-3])}")
