# Insertion Sort

# Objectives:
# Execute insertion sort
# Build an algorithm for insertion sort. 
# Please watch the video here to understand how insertion sort works and implement the code. 
# The following gif also shows how insertion sort is done.

# Again, write your plan in a non-programming language first and test your 
# base cases before you build your code next.

# Please refrain from checking other people's code. 
# If your code does NOT work as intended make sure (1) that you're writing
# up your plan first, (2) that your plan solves your base case, and 
# (3) that your plan solves other base cases you have specified.

# Sometimes, if you are stuck for too long, you need to just 
# start all over as this can be more efficient to do than dwelling on 
# old code with bugs that are hard to trace.

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1, -1, -1):
            if (arr[j+1]<arr[j]):
                arr[j+1],arr[j]=arr[j],arr[j+1]
    print(arr)
    return None
istart = [1,7,8,9,-1,4,2,0,3,-10]
insertion_sort(istart)
    