# SLists
# ======

# Objectives:
# -----------
# Understand how Singly Linked List works
# Understand how pointers work
# Understand how to traverse and add node to the linked list

# Implementation
# --------------
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
    
# class SList:
#     def __init__(self, value):
#         node = Node(value)
#         self.head = node
    
#     def addNode(self, value):
#         node = Node(value)
#         runner = self.head
#         while(runner.next != None):
#             runner = runner.next
#         runner.next = node
     
#     def printAllValues(self, msg=""):
#         runner = self.head          # create a runner     
#         print("\n\nhead points to ", id(self.head))
#         print("Printing the values in the list ---", msg,"---")
#         while(runner.next != None):
#             print(id(runner), runner.value, id(runner.next))
#             runner = runner.next        
#         print(id(runner), runner.value, id(runner.next))
      
# print("\n\n\n\n================== START OF THE PROGRAM ================")       
# list = SList(5)
# list.addNode(7)
# list.addNode(9)
# list.addNode(1)
     
# list.printAllValues("Attempt 1")

# Assignment
# ----------
# Part 1 - recreate SList and Node.  
# Recreate addNode and printAllValues methods.
#
# Singly Linked List is one of the most fundamental data structures you'll be using.  
# Using the concepts here, you'll learn how to create other data structure such as Stacks, 
# Queues, Doubly Linked List, Binary Search Trees, Tries, Graphs, etc.  
# As it's such a critical concept, please re-create the codes demonstrated above 
# without looking at the platform.  Make sure you feel very comfortable with adding 
# a new Node, traversing through the linked list, etc.  Once you can create both SList 
# and Node without looking at the codes above, then proceed with Part 2.

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class SList():
    def __init__(self, value):
        node = Node(value)
        self.head = node
    
    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def insertNodeAtIndex(self, value, index):
        node = Node(value)
        if (index<0):
            return -1  # return error index to small
        if (index==0):
            # head
            node.next = self.head
            self.head = node
            return 0  # return new index
        else:
            previous = self.head
            current = self.head.next 
            count = 0
            while current:
                count +=1
                # current comes in as valid next from previous, 
                #  count is now the actual index position, 
                #  previous is how we got here
                if (index==count):
                    node.next = current
                    previous.next = node
                    return index
                else:
                    previous = current
                    current = current.next 
            # if we get here our index may be too large ...
            # if count+1=index then put it at the end, 
            # otherwise return error
            if (count+1==index):
                previous.next = node
                return index 
            return -1 #-1=error index too large (or negative)

    def removeNode(self,value):
        previous = None
        current = self.head
        while current:
            if current.value == value:
                if previous:
                    previous.next = current.next 
                else:
                    self.head = current.next
                print("Node " + str(value) + " deleted")
                return True
                    
            previous = current
            current = current.next
        print("Unable to delete Node " + str(value))
        return False

    def printAllValues(self, msg=""):
        runner = self.head
        print("Head: \t" + str(id(self.head)))
        print("List : " + msg)
        print("  ID() \t       Value \t  Next() ")
        while(runner.next != None):
            print(str(id(runner)) + "\t" + str(runner.value) + "\t" + str(id(runner.next)))
            runner = runner.next        
        print(str(id(runner)) + "\t" + str(runner.value) + "\t" + str(id(runner.next)))

list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
     
list.printAllValues("Add 4, Print All")



# Part 2 - implement removeNode(val)
# Implement removeNode(val) where it removes a node with the value val.  
# For example list.removeNode(5) will see if there's a node with the value of 5.  
# If it is, it will remove that from the linked list.  

# When you do this, you'll need to consider the following cases:
# when the node you want to remove is in the beginning of the linked list
# when the node you want to remove is in the middle of the linked list
# when the node you want to remove is at the end of the linked list

# For each of these cases, you will probably need to have different logics to handle the removal.

# list = Slist(5)
# list.addNode(7)
# list.addNode(9)
# list.addNode(1)
# list.removeNode(9) # removes 9, which is one of the middle nodes in the list
# list.removeNode(5) # removes 5, which is the first value in the list
# list.removeNode(1) # removes 1, which is the last node in the list
# list.printAllValues("Add 4, Remove 3, Print All")

list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9) # removes 9, which is one of the middle nodes in the list
list.removeNode(5) # removes 5, which is the first value in the list
list.removeNode(1) # removes 1, which is the last node in the list
list.printAllValues("Add 4, Remove 3, Print All")


# As this assignment is quite challenging, if you're struggling, please see 
# if you can pair up with someone else in your cohort and do this together.


# Part 3 (optional) - Implement insertNode(val, index)
# Implement InsertNode(val, index), which insert a new node of value 
# 'val' on the specified index.  For example, for a linked list with 
# the value of 5 -> 3 -> 1, performing insertNode(7, 2) would insert a Node 
# of value 7 at its 2nd index, making the node 5 -> 3 -> 7 -> 2.

print("=" * 60)


liste = SList(1)
liste.addNode(2)
liste.addNode(3)
print("\n\nInsert: " + str(liste.insertNodeAtIndex(100,0)))
liste.printAllValues("Add 1,2,3; Insert 100,0; Print All")

lista = SList(1)
lista.addNode(2)
lista.addNode(3)
print("\n\nInsert: " + str(lista.insertNodeAtIndex(100,1)))
lista.printAllValues("Add 1,2,3; Insert 100,1; Print All")

listb = SList(1)
listb.addNode(2)
listb.addNode(3)
print("\n\nInsert: " + str(listb.insertNodeAtIndex(100,2)))
listb.printAllValues("Add 1,2,3; Insert 100,2; Print All")

listc = SList(1)
listc.addNode(2)
listc.addNode(3)
print("\n\nInsert: " + str(listc.insertNodeAtIndex(100,3)))
listc.printAllValues("Add 1,2,3; Insert 100,3; Print All")

listd = SList(1)
listd.addNode(2)
listd.addNode(3)
print("\n\nInsert: " + str(listd.insertNodeAtIndex(100,99)))
listd.printAllValues("Add 1,2,3; Insert 100,99; Print All")

listf = SList(1)
listf.addNode(2)
listf.addNode(3)
print("\n\nInsert: " + str(listf.insertNodeAtIndex(100,-1)))
listf.printAllValues("Add 1,2,3; Insert 100,-1; Print All")


# Please make sure that this method allows you to insert a new node as 
# the first node in the list (if index is 0), anywhere in the middle of the 
# list, or at the end of the list (if the specified index is at the end of the list).




# OUTPUT:

# 08:52:49 bart ~/projects/cd/python/pyfun (master)
# $ python slists.py
# Head: 	4320418224
# List : Add 4, Print All
#   ID() 	       Value 	  Next()
# 4320418224	5	4320418280
# 4320418280	7	4320418336
# 4320418336	9	4320418392
# 4320418392	1	4312235896
# Node 9 deleted
# Node 5 deleted
# Node 1 deleted
# Head: 	4320418168
# List : Add 4, Remove 3, Print All
#   ID() 	       Value 	  Next()
# 4320418168	7	4312235896
# ============================================================


# Insert: 0
# Head: 	4320418336
# List : Add 1,2,3; Insert 100,0; Print All
#   ID() 	       Value 	  Next()
# 4320418336	100	4320418280
# 4320418280	1	4320418448
# 4320418448	2	4320418224
# 4320418224	3	4312235896


# Insert: 1
# Head: 	4320418560
# List : Add 1,2,3; Insert 100,1; Print All
#   ID() 	       Value 	  Next()
# 4320418560	1	4320418784
# 4320418784	100	4320418672
# 4320418672	2	4320418728
# 4320418728	3	4312235896


# Insert: 2
# Head: 	4320418840
# List : Add 1,2,3; Insert 100,2; Print All
#   ID() 	       Value 	  Next()
# 4320418840	1	4320418952
# 4320418952	2	4320419064
# 4320419064	100	4320419008
# 4320419008	3	4312235896


# Insert: 3
# Head: 	4320419120
# List : Add 1,2,3; Insert 100,3; Print All
#   ID() 	       Value 	  Next()
# 4320419120	1	4320419232
# 4320419232	2	4320419288
# 4320419288	3	4320419344
# 4320419344	100	4312235896


# Insert: -1
# Head: 	4320419400
# List : Add 1,2,3; Insert 100,99; Print All
#   ID() 	       Value 	  Next()
# 4320419400	1	4320419512
# 4320419512	2	4320419568
# 4320419568	3	4312235896


# Insert: -1
# Head: 	4320419624
# List : Add 1,2,3; Insert 100,-1; Print All
#   ID() 	       Value 	  Next()
# 4320419624	1	4320419736
# 4320419736	2	4320419792
# 4320419792	3	4312235896
