# Coding Dojo Basic 13 - Python
# June 4, 2018

# print 1-255
def pr1to255():
    # for i in range(256):
    #     print(i)
    retn = [i for i in range(256)]
    print(f"Print 1-255:: \n {retn}")
    return
pr1to255()


# print odds 1-255
def prodds():
    # retn = []
    # for i in range(1,256,2):
    #     retn.append
    #     print(i)
    retn = [i for i in range(1,256,2) ]
    print("Print Odds 1-255:")
    print(retn)
    return
prodds()


# print ints and sum 0-255
def printintsum():
    retn = []
    sum = 0
    for i in range(0,256):
        tempret = []
        sum += i
        # print(str(i) + "," + str(sum))
        tempret.append(i)
        tempret.append(sum)
        retn.append(tempret)
    print(f"Print ints and sum 0-255::\n {retn}")
    # print(retn)
    return
printintsum()


# print array values
def printarr(arr):
    print(f"Print array Values:: {arr}")
    for i in range(len(arr)):
        print(arr[i])
    # print(f"Print array Values::\n {arr}")
    return
arr1 = [1, 2, 3, 4, 5]    
printarr(arr1)


# print max of array
def maxarr(arr):
    max=arr[0]
    for i in range(1,len(arr)):
        if max<arr[i]:
            max = arr[i]
    # print(max)
    print(f"Array max::\n {arr} --> Max:{max}")
    return
maxarr(arr1)


# print avg of array
def avgarr(arr):
    if (len(arr)==0):
        return False
    avg=arr[0]
    for i in range(1,len(arr)):
        avg+=arr[i]
    avg=avg/len(arr)
    # print(avg)
    print(f"Array Average::\n {arr} --> Avg:{avg}")
    return
avgarr(arr1)


# return odds array 1-255
def retodds():
    retn = []
    for i in range(1,256,2):
        retn.append(i)
    return retn
arodds = retodds()
print(f"Odds Array::\n {arodds}")


# square array values
def sqarray(arr):
    retn = []
    for i in arr:
        retn.append(i**i)
    return retn 
arr1a = sqarray(arr1)
print("Squares:: " + str(arr1) + " --> " + str(arr1a))


# return array count gty 
def acgty(arr,y):
    count = 0
    for i in arr:
        if(i>y):
            count+=1
    print(f"ArrayCount {arr} GreaterThan {y} = {count}")
    return count
acgty(arr1,2)


# zero out array negative numbers
def znav(arr):
    newarr = []
    for i in arr:
        topop = i
        if i < 0:
            topop = 0
        newarr.append(topop)
    return newarr
arr2=[0,-1,2,-3,4,-5]
arr2a = znav(arr2)
print("Zero out:: " + str(arr2) + "-->" + str(arr2a))


# print max min avg array values
def prmmaarr(arr):
    min=arr[0]
    max=arr[0]
    sum=arr[0]
    for i in range(1,len(arr)):
        if max<arr[i]:
            max = arr[i]
        if min>arr[i]:
            min = arr[i]
        sum += arr[i]
    sum = sum/len(arr)
    # print("source:" + str(arr))
    # print("  max:" + str(max))
    # print("  min:" + str(min))
    # print("  avg:" + str(sum))
    # print("{} --> Min:{}, Max:{}, Avg:{}".format(arr,min,max,sum))
    print(f"{arr} --> Min:{min}, Max:{max}, Avg:{sum}")
    return
prmmaarr(arr2)


# shift array values left
def lshftarr(arr):
    newarr = []
    for i in range(1,len(arr)):
        newarr.append(arr[i])
    newarr.append(0)
    return newarr 
arr3 = lshftarr(arr2)
print("Shift Array Left:: " + str(arr2) + " --> " + str(arr3))


# swap string for negative values
def swapnegs(arr):
    newarr = []
    for i in arr:
        if i < 0:
            newarr.append('Dojo')
        else:
            newarr.append(i)
    arr=newarr
    return newarr
arr4 = swapnegs(list(arr2))
print("SwapStrForNegs:: " + str(arr2) + "-->" + str(arr4))
