# Assignment: Product
# ==================

# Objectives:
# -----------
# Practice creating a class and making instances from it
# Practice accessing the methods and attributes of different instances
# Practice altering an instance's attributes

# The owner of a store wants a program to track products. 
# Create a product class to fill the following requirements.

# Product Class:

# Attributes:
# -----------
# Price
# Item Name
# Weight
# Brand

# Status: default "for sale"

# Methods:
# ---------
# Sell: changes status to "sold"

# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax

# Return Item: takes reason_for_return as a parameter and changes status accordingly. 
# If the item is being returned because it is defective, change status to "defective" and change price to 0. 
# If it is being returned in the box, like new, mark it "for sale". 
# If the box has been opened, set the status to "used" and apply a 20% discount.  
# (use "defective", "like_new", or "opened" as three possible value for reason_for_return).

# Display Info: show all product details.

# Every method that doesn't have to return something should return self so methods can be chained.

class Product:
    def __init__(self, price, name, weight, brand):
	# instance attributes 
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"
    # show the current info
    def display_info(self):
        print("Pr:" + str(self.price) + " N:" +  self.name + " Wt:" + str(self.weight) + " Br: " + self.brand + " St:" + self.status )
        return self
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax_to_add):
        self.price += tax_to_add
        self.name += ", taxed"
        return self.price
    def return_item(self, reason_for_return):
        if (reason_for_return=="defective"):
            self.status = "defective"
            self.price = 0.0
        elif (reason_for_return=='like_new'):
            self.status = "for sale"
        elif (reason_for_return=="opened"):
            self.status = "used"
            self.price *= 0.80
        return self

products = [
    Product(2.15, "banana", 0.7, 'Chiquita'),
    Product(3.00, "bread", 0.7, 'Wonder'),
    Product(279.95, "tv", 87, 'RCA'),
    Product(9.95, "burger", 1, "Dick\'s Deluxe"),
    Product(.05, "eraser", 0.01, 'yellow')
]

products[0].display_info()
products[0].add_tax(.25)
products[0].display_info()

products[1].display_info()
products[1].add_tax(.25)
products[1].sell().display_info()

products[2].display_info()
products[2].add_tax(25)
products[2].sell().display_info()
products[2].return_item("like_new").display_info()
products[2].sell().display_info()

products[3].display_info()
products[3].sell().display_info()
products[3].return_item("opened").display_info()
products[3].sell().display_info()
products[3].return_item("defective").display_info()

products[4].display_info()
products[4].add_tax(1)
products[4].display_info()


# OUTPUT:
# 08:18:48 bart ~/projects/cd/python/pyfun (master)
# $ python clsProduct.py
# Pr:2.15 N:banana Wt:0.7 Br: Chiquita St:for sale
# Pr:2.4 N:banana, taxed Wt:0.7 Br: Chiquita St:for sale
# Pr:3.0 N:bread Wt:0.7 Br: Wonder St:for sale
# Pr:3.25 N:bread, taxed Wt:0.7 Br: Wonder St:sold
# Pr:279.95 N:tv Wt:87 Br: RCA St:for sale
# Pr:304.95 N:tv, taxed Wt:87 Br: RCA St:sold
# Pr:304.95 N:tv, taxed Wt:87 Br: RCA St:for sale
# Pr:304.95 N:tv, taxed Wt:87 Br: RCA St:sold
# Pr:9.95 N:burger Wt:1 Br: Dick's Deluxe St:for sale
# Pr:9.95 N:burger Wt:1 Br: Dick's Deluxe St:sold
# Pr:7.96 N:burger Wt:1 Br: Dick's Deluxe St:used
# Pr:7.96 N:burger Wt:1 Br: Dick's Deluxe St:sold
# Pr:0.0 N:burger Wt:1 Br: Dick's Deluxe St:defective
# Pr:0.05 N:eraser Wt:0.01 Br: yellow St:for sale
# Pr:1.05 N:eraser, taxed Wt:0.01 Br: yellow St:for sale