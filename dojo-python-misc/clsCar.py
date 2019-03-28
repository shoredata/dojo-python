# Assignment: Car

# Objectives:
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances

# Create a class called  Car. 

# In the __init__(), allow the user to specify the following attributes: 
# price, speed, fuel, mileage. 

# If the price is greater than 10,000, set the tax to be 15%. 
# Otherwise, set the tax to be 12%.


# Create six different instances of the class Car. 

# In the class have a method called display_all() that returns 
# all the information about the car as a string. 

# In your __init__(), call this display_all() method to display information 
# about the car once the attributes have been defined.

# A sample output would be like this:

# Price: 2000
# Speed: 35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12

# Price: 2000
# Speed: 5mph
# Fuel: Not Full
# Mileage: 105mpg
# Tax: 0.12

# Price: 2000
# Speed: 15mph
# Fuel: Kind of Full
# Mileage: 95mpg
# Tax: 0.12

# Price: 2000
# Speed: 25mph
# Fuel: Full
# Mileage: 25mpg
# Tax: 0.12

# Price: 2000
# Speed: 45mph
# Fuel: Empty
# Mileage: 25mpg
# Tax: 0.12

# Price: 20000000
# Speed: 35mph
# Fuel: Empty
# Mileage: 15mpg
# Tax: 0.15

class Car:
    def __init__(self, price, speed, fuel, mileage):
	# instance attributes 
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        self.tax = "0.12"
        if (self.price>10000):
            self.tax = "0.15"
        self.display_all()
    # show the current info
    def display_all(self):
        self.logged = True
        print("\nPrice: " + str(self.price) + "\nSpeed:" +  self.speed + "\nFuel: " + self.fuel + "\nMileage: " + self.mileage + "\nTax: " + self.tax )
        return self

cars = [
    Car(2000, '35mph', 'Full', '15mpg'),
    Car(2000, '5mph', 'Not Full', '105mpg'),
    Car(2000, '15mph', 'Kind of Full', '95mpg'),
    Car(2000, '25mph', 'Full', '25mpg'),
    Car(2000, '45mph', 'Empty', '25mpg'),
    Car(2000000, '35mph', 'Empty', '15mpg'),
]


# OUTPUT:
# 07:50:03 bart ~/projects/cd/python/pyfun (master)
# $ python clsCar.py

# Price: 2000
# Speed:35mph
# Fuel: Full
# Mileage: 15mpg
# Tax: 0.12

# Price: 2000
# Speed:5mph
# Fuel: Not Full
# Mileage: 105mpg
# Tax: 0.12

# Price: 2000
# Speed:15mph
# Fuel: Kind of Full
# Mileage: 95mpg
# Tax: 0.12

# Price: 2000
# Speed:25mph
# Fuel: Full
# Mileage: 25mpg
# Tax: 0.12

# Price: 2000
# Speed:45mph
# Fuel: Empty
# Mileage: 25mpg
# Tax: 0.12

# Price: 2000000
# Speed:35mph
# Fuel: Empty
# Mileage: 15mpg
# Tax: 0.15
