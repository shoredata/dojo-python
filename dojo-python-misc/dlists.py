# (optional) 
# Doubly Linked Lists
# ============================================

# Objectives:
# ----------------

# What are the differences between singly linked lists and doubly linked lists?
# What are the pros and cons of each?
# Construct a doubly linked list using OOP

# Disclaimer: If you're ahead and have already finished all the mandatory assignments, 
# please work on this assignments before moving on to Flask.  
# Many students mention how they were expected to do linked list on the whiteboard 
# during their technical interviews.  
# If you're on schedule or not so ahead, you can skip this assignment and come back when you have more time.

# These exercises are designed to help you prepare for technical interviews and to reinforce concepts 
# you've learned about OOP. If you want to be better prepared for technical interviews, it's helpful to 
# know linked lists and how they are used. Some interesting puzzles can be solved using linked lists 
# (and you may be asked to solve problems using linked lists in technical interviews).

# In technical interviews, our alumni are commonly asked problems involving linked lists. 
# Learn about doubly-linked lists, also known as DLists. (You may already know singly-linked lists 
# (SLists), which are simpler and more common, but you'll learn more by researching doubly-linked lists.)

# http://en.wikipedia.org/wiki/Doubly_linked_list would be a great start.

# Once you have learned about linked lists, build a class in Python and demonstrate how you can
#     add a new node to the end of the list
#     delete an existing node
#     insert a node in between existing nodes(before and after node of given value)

# You should have two classes for this: 
#     DoublyLinkedList and 
#     Node. 
    
# Have DoublyLinkedList be the class that allows you to 
#     add a new node, 
#     delete an existing node, 
#     insert a new node between existing nodes, and 
#     print out the values in the linked list. 
    
# Have Node be the class that has the necessary properties for the node.

# Please also think about the following:
#     How would you know if you have a circular linked list?
#     How would you get to the middle of the linked list?
#     How would you remove duplicate values in the list?
#     How would you reverse the values in the list?

# Think hard about these puzzles and how you could potentially use multiple runners to tackle some of these tasks.

# You can spend up to 5 hours on this assignment.

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DList():
    def __init__(self):
        self.first = None
        self.last = None
        print("\n Init Empty")

    def deleteNode(self,value):
        print("\n Delete " + str(value))
        current = self.first
        buffer = None
        while current:
            if (current.value==value):
                if buffer:
                    buffer.next = current.next
                    if (current.next!=None): 
                        current.next.prev = current.prev
                    else:
                        print(" -- removing last item in list")
                        self.last = current.prev
                else:
                    if (self.first==self.last):
                        print(" -- removing ONLY item in list")
                        self.first = None
                        self.last = None
                    else:
                        print(" -- removing first item in list")
                        self.first = current.next
                        self.first.prev = None
                self.printAllNodes()
                return True
            else:
                buffer = current
                current = current.next
        print(" !! Unable to locate " + str(value))
        self.printAllNodes()
        return False 

    def appendNode(self, value):
        print("\n Append " + str(value))
        node = Node(value)
        node.prev = self.last
        if (self.last):
            self.last.next = node
        else:
            self.first = node
        self.last = node 
        self.printAllNodes()

    def prependNode(self, value):
        print("\n Prepend " + str(value))
        node = Node(value)
        node.next = self.first
        if self.first:
            self.first.prev = node
        else:
            self.last = node 
        self.first = node
        self.printAllNodes()

    def describeForPrint(self, mynode):
        if (mynode==None):
            return " {null} "
        else:
            return str(id(mynode))

    def printAllNodes(self):
        runner = self.first
        print("First: \t" + self.describeForPrint(self.first))
        print("Last: \t" + self.describeForPrint(self.last))
        print("List : ")
        print("  ID() \t       Value \t  Prev()   \t   Next()")
        while runner:
            print(self.describeForPrint(runner) + "\t" + str(runner.value) + "\t" + self.describeForPrint(runner.prev) + "\t" + self.describeForPrint(runner.next))
            runner = runner.next        
        # print(self.describeForPrint(runner) + "\t" + str(runner.value) + "\t" + self.describeForPrint(runner.prev) + "\t" + self.describeForPrint(runner.next))


if __name__ == "__main__":
    # print("the file is being executed directly")
    list = DList()
    list.appendNode(5)
    list.appendNode(7)
    list.appendNode(9)
    list.appendNode(1)
    list.deleteNode(9)
    list.deleteNode(5)
    list.deleteNode(1)
    list.deleteNode(7)
    list.prependNode(2)
    list.prependNode(4)
    list.prependNode(6)
    list.prependNode(8)
    list.appendNode(5)
    list.appendNode(7)
    list.deleteNode(4)
    list.deleteNode(9)
    list.deleteNode(5)

# OUTPUT:

# 18:47:52 bart ~/projects/cd/python/pyfun (master)
# $ python dlists.py

#  Init Empty

#  Append 5
# First: 	4454508584
# Last: 	4454508584
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508584	5	 {null} 	 {null}

#  Append 7
# First: 	4454508584
# Last: 	4454508640
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508584	5	 {null} 	4454508640
# 4454508640	7	4454508584	 {null}

#  Append 9
# First: 	4454508584
# Last: 	4454508696
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508584	5	 {null} 	4454508640
# 4454508640	7	4454508584	4454508696
# 4454508696	9	4454508640	 {null}

#  Append 1
# First: 	4454508584
# Last: 	4454508752
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508584	5	 {null} 	4454508640
# 4454508640	7	4454508584	4454508696
# 4454508696	9	4454508640	4454508752
# 4454508752	1	4454508696	 {null}

#  Delete 9
# First: 	4454508584
# Last: 	4454508752
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508584	5	 {null} 	4454508640
# 4454508640	7	4454508584	4454508752
# 4454508752	1	4454508640	 {null}

#  Delete 5
#  -- removing first item in list
# First: 	4454508640
# Last: 	4454508752
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508640	7	 {null} 	4454508752
# 4454508752	1	4454508640	 {null}

#  Delete 1
#  -- removing last item in list
# First: 	4454508640
# Last: 	4454508640
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508640	7	 {null} 	 {null}

#  Delete 7
#  -- removing ONLY item in list
# First: 	 {null}
# Last: 	 {null}
# List :
#   ID() 	       Value 	  Prev()   	   Next()

#  Prepend 2
# First: 	4454508640
# Last: 	4454508640
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508640	2	 {null} 	 {null}

#  Prepend 4
# First: 	4454508584
# Last: 	4454508640
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508584	4	 {null} 	4454508640
# 4454508640	2	4454508584	 {null}

#  Prepend 6
# First: 	4454508752
# Last: 	4454508640
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508752	6	 {null} 	4454508584
# 4454508584	4	4454508752	4454508640
# 4454508640	2	4454508584	 {null}

#  Prepend 8
# First: 	4454508696
# Last: 	4454508640
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508696	8	 {null} 	4454508752
# 4454508752	6	4454508696	4454508584
# 4454508584	4	4454508752	4454508640
# 4454508640	2	4454508584	 {null}

#  Append 5
# First: 	4454508696
# Last: 	4454508808
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508696	8	 {null} 	4454508752
# 4454508752	6	4454508696	4454508584
# 4454508584	4	4454508752	4454508640
# 4454508640	2	4454508584	4454508808
# 4454508808	5	4454508640	 {null}

#  Append 7
# First: 	4454508696
# Last: 	4454508864
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508696	8	 {null} 	4454508752
# 4454508752	6	4454508696	4454508584
# 4454508584	4	4454508752	4454508640
# 4454508640	2	4454508584	4454508808
# 4454508808	5	4454508640	4454508864
# 4454508864	7	4454508808	 {null}

#  Delete 4
# First: 	4454508696
# Last: 	4454508864
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508696	8	 {null} 	4454508752
# 4454508752	6	4454508696	4454508640
# 4454508640	2	4454508752	4454508808
# 4454508808	5	4454508640	4454508864
# 4454508864	7	4454508808	 {null}

#  Delete 9
#  !! Unable to locate 9
# First: 	4454508696
# Last: 	4454508864
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508696	8	 {null} 	4454508752
# 4454508752	6	4454508696	4454508640
# 4454508640	2	4454508752	4454508808
# 4454508808	5	4454508640	4454508864
# 4454508864	7	4454508808	 {null}

#  Delete 5
# First: 	4454508696
# Last: 	4454508864
# List :
#   ID() 	       Value 	  Prev()   	   Next()
# 4454508696	8	 {null} 	4454508752
# 4454508752	6	4454508696	4454508640
# 4454508640	2	4454508752	4454508864
# 4454508864	7	4454508640	 {null}
