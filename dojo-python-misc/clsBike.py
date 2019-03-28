# Assignment: Bike

# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# Create a new class called Bike with the following properties/attributes:

# price
# max_speed
# miles
# Create 3 instances of the Bike class.

# Use the __init__() method to specify the price and max_speed of each instance 
# (e.g. bike1 = Bike(200, "25mph"); 
# 
# In the __init__(), also write the code so that the initial miles is set to be 0 whenever a new instance is created.

# Add the following methods to this class:

# displayInfo() - have this method display the bike's price, maximum speed, and the total miles.
# ride() - have it display "Riding" on the screen and increase the total miles ridden by 10
# reverse() - have it display "Reversing" on the screen and decrease the total miles ridden by 5...

# Have the first instance ride three times, reverse once and have it displayInfo(). 
# Have the second instance ride twice, reverse twice and have it displayInfo(). 
# Have the third instance reverse three times and displayInfo().

# What would you do to prevent the instance from having negative miles?

# Which methods can return self in order to allow chaining methods?



# define class Bike
class Bike:
    # this method to run every time a new object is instantiated
    def __init__(self, price, max_speed):
	# instance attributes 
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    # show the current info
    def displayInfo(self):
        self.logged = True
        print("Price:" + str(self.price) + ", Max Speed:" +  self.max_speed + ", Miles:" + str(self.miles) )
        return self
    # increase miles
    def ride(self):
        self.miles += 10
        print("Riding ...")
        return self
    # decrease miles but dont go below 0
    def reverse(self):
        self.miles -= 5
        if (self.miles<0):
            self.miles=0
        print("Reversing ...")
        return self


bike1 = Bike(1200,"45mph")
bike1.ride().ride().ride().reverse().displayInfo()

bike2 = Bike(500,"30mph")
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(1000,"60mph")
bike2.reverse().reverse().reverse().displayInfo()


# OUTPUT:
# 07:36:03 bart ~/projects/cd/python/pyfun (master)
# $ python clsBike.py
# Riding ...
# Riding ...
# Riding ...
# Reversing ...
# Price:1200, Max Speed:45mph, Miles:25
# Riding ...
# Riding ...
# Reversing ...
# Reversing ...
# Price:500, Max Speed:30mph, Miles:10
# Reversing ...
# Reversing ...
# Reversing ...
# Price:500, Max Speed:30mph, Miles:0
# (py3Env)