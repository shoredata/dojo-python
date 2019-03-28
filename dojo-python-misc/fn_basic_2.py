# Functions Basic II
# ====================
# Objectives
# --------------------
# Learn how to create basic functions in Python
# Get comfortable using lists
# Get comfortable having the function return an expression/value

# Countdown - Create a function that accepts a number as an input.  
# Return a new array that counts down by one, from the number (as arrays 'zero'th element) down to 0 (as the last element).  
# For example countDown(5) should return [5,4,3,2,1,0].
def countdown(num):
    newarr = []
    for i in range(num,-1,-1):
        newarr.append(i)
    return newarr
count1 = 5
print(countdown(count1))
    

# Print and Return - Your function will receive an array with two numbers. 
# Print the first value, and return the second.
def printandreturn(num1, num2):
    print(num1)
    return num2
val1 = 101
val2 = 2012
print(printandreturn(val1,val2))

# First Plus Length - Given an array, return the sum of the first value in 
# the array, plus the array's length.
def firstpluslength(arr):
    return len(arr) + arr[0]
arr1=[12,0,-18,-9,3,-4,5,-909,1212]
print(firstpluslength(arr1))

# Values Greater than Second - Write a function that accepts any array, and 
# returns a new array with the array values that are greater than its 2nd value.  
# Print how many values this is.  
# If the array is only element long, have the function return False
def vgts(arr):
    newarr = []
    if (len(arr)<2):
        return False
    else:
        for i in range(len(arr)):
            if arr[i]>arr[1]:
                newarr.append(arr[i])
    print(len(newarr))    
    return newarr
arr1a = vgts(arr1)
print(f"{arr1} --> {arr1a}")

# This Length, That Value - Given two numbers, return array of length num1 
# with each value num2.  
# Print "Jinx!" if they are same.
def tltv(num1,num2):
    retn = []
    if (num1==num2):
        print("Jinx!")
    else:
        retn = [num2 for i in range(num1)]
    return retn
print(f"(6,6) = {tltv(6,6)} (should have printed Jinx! above  here ^^")
print(f"(2,4) = {tltv(2,4)}")
print(f"(5,-18) = {tltv(5,-18)}")





