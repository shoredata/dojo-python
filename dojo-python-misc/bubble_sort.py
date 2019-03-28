# Bubble Sort
# Objectives:
# Execute the famous Bubble Sort
# "What is the most efficient way to sort a million 32-bit integers?" - Google CEO Eric Schmidt
# "I think the bubble sort would be the wrong way to go." - Senator Barack Obama
#                                                                                                                          
# -- November 2007
# Poor Bubble Sort. It gets teased a lot, but it's fundamental to know! Besides, it still has its use cases.
# Build an algorithm for bubble sort. The gif below demonstrates how bubble sort works.
# Demonstration

def bubble_sort(arr):
    print(arr)
    iswapped = 0
    for i in range(len(arr)):
        itarget = len(arr)-iswapped-1
        for j in range(itarget):
            if (arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                iswapped = 1
    print(arr)
    return None
istart = [1,7,8,9,-1,4,2,0,3,-10]
bubble_sort(istart)
