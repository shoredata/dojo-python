# Outline
# # Create beCheerful().  Within it, print string "good morning!" 98 times.
# print("*"*80)
# def beCheerful(name='', repeat=1):
# 	print(f"good morning {name}\n"*repeat)
# beCheerful()
# beCheerful(name="john")
# beCheerful(name="michael", repeat=5)
# beCheerful(repeat=5, name="kb")
# beCheerful(name="aa")
# # helpful tips for the next assignment
# import random
# print(random.random()) # returns a random floating number between 0.000 to 1.000
# print(random.random()*50) # returns a float between 0.000 to 50.000
# int( 3.654 ) # returns 3
# round( 3.654 ) # returns 4

# As part of this assignment, please create a function randInt() where
# randInt() returns a random integer between 0 to 100
# randInt(max=50) returns a random integer between 0 to 50
# randInt(min=50) returns a random integer between 50 to 100
# randInt(min=50, max=500) returns a random integer between 50 and 500
# Create this function without using random.randInt() but you are allowed to use random.random().

import random
def randint(min=0, max=100):
    return round((random.random() * (max-min) ) + min)

def dotest(count,min,max):
    lmin=0
    lmax=0
    lsum=0
    for i in range(count):
        val = randint(min,max)
        if (i==1):
            lmin=val
            lmax=val
            lsum=val
        else:
            if (lmin>val):
                lmin=val
            if (lmax<val):
                lmax=val
            lsum += val
    print(f"{count} tries: {min}, {lmin}, {lsum/count}, {lmax}, {max}")

dotest(10000,1,100)
dotest(5,1,100)                
dotest(10000,1,10)
dotest(5,1,10)                

dotest(5,6,18)                
dotest(5,2,40)                
dotest(5,-7,9)                
