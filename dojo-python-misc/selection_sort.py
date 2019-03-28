# Selection Sort
# Objectives:
# Execute selection sort
# If you're given a list with a bunch of numbers and you're supposed to sort the numbers 
# (with the smallest number on the left and the largest number on the right), 
# how would you do this? There are numerous sorting algorithms to sort numbers in the list. 

# We'll introduce one of the simplest sorting algorithm called selection sort.

# According to Wikipedia, selection sort
# ... divides the input list into two parts: the sublist of items already sorted, 
# which is built up from left to right at the front (left) of the list, and the sublist of 
# items remaining to be sorted that occupy the rest of the list. Initially, the sorted sublist 
# is empty and the unsorted sublist is the entire input list. The algorithm proceeds by 
# finding the smallest (or largest, depending on sorting order) element in the unsorted sublist, 
# exchanging it with the leftmost unsorted element (putting it in sorted order), and moving 
# the sublist boundaries one element to the right.
# Please watch this video and check out the gif below to better understand how selection sort is done.

def selection_sort(arr):
    for i in range(len(arr)-1):
        imin=i
        for j in range(i+1, len(arr)):
            if (arr[j]<arr[imin]):
                imin = j
        arr[i], arr[imin] = arr[imin], arr[i]
    print(arr)
    return None
istart = [1,7,8,9,-1,4,2,0,3,-10]
selection_sort(istart)

