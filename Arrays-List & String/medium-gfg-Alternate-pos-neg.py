# Alternate positive and negative numbers
# Link to the problem https://www.geeksforgeeks.org/problems/array-of-alternate-ve-and-ve-nos1401/1
# Given an array. The task is to place positive and negative numbers alternate
# Date: 21/10/2024
# The Problem Consist of Brute force solution
# Method 1 the  Brute Force Method 
# if numbers of positive elements are not equal to number of negative elements 
def rearragnge(arr):
    pos=[]
    neg=[]
    for i in range(len(arr)):
        if arr[i]>=0:
            pos.append(arr[i])
        else:
            neg.append(arr[i])
    if len(pos)<len(neg):
        for i in range(len(pos)):
            arr[i*2]=pos[i]
            arr[i*2+1]=neg[i]
        index=len(pos)*2
        for i in range(len(neg)-len(pos)):
            arr[index]=neg[len(pos)+i]
            index +=1
    else:
        for i in range(len(neg)):
            arr[i*2]=pos[i]
            arr[i*2+1]=neg[i]
        index=len(neg)*2
        for i in range(len(pos)-len(neg)):
            arr[index]=pos[len(neg)+i]
            index +=1
    print(arr)
arr=[9, 4, -2, -1, 5, 0, -5, -3, 2]
rearragnge(arr)

# if numbers of positive elements are equal to number of negative elements 
def alternatePos_Neg(arr1):
    pos=[]
    neg=[]
    for i in range(len(arr1)):
        if arr1[i]>=0:
            pos.append(arr1[i])
        else:
            neg.append(arr1[i])
    for i in range(len(pos)):
        arr1[2*i]=pos[i]
    for i in range(len(neg)):
        arr1[2*i+1]=neg[i]
    print(arr1)
arr1=[9, 4, -2, -1, 5, 0, -5, -3, 2]
alternatePos_Neg(arr1)
