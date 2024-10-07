# Kadane's Algorithm also known as Maximun sub array sum
# Link to the problem https://www.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1
# Given an array, arr. The task is to find the sub array of the element in it.
# Date: 07/10/2024
# The Problem Consist of three solution. Brute force solution, better Solution, and A optimal Solution. 
# Method 1 the  Brute Force Method 
import sys
def maxsubarray_sum(arr):
    maxi= -sys.maxsize -1
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum+= arr[k]
            maxi=max(maxi,sum)
            if maxi<0:
                maxi=0
    print(maxi)
arr=[-2,-1,-3,-1,-5,-4] 
maxsubarray_sum(arr)  

#Method2 the better Soln here we optimize the code by removing the 3 for loop
def max_subaaraysum(A):
    maxi= -sys.maxsize -1
    for i in range( len(arr)):
        sum=0
        for j in range(i,len(arr)):
            sum+=arr[j]
        maxi=max(maxi,sum)
        if maxi<0:
            maxi=0
    print(maxi)
A=[-2,-1.-3,4,-1,2,1,-5,-4] 
maxsubarray_sum(A)

# Method 3: here we use the Kadaen's algorithm
def maxSubarraySum(array):
    maxi = sys.maxsize -1
    sum=0
    for i in range(len(arrary)):
        sum+=array[i]
        if sum>maxi:
            maxi=sum
        if sum <0:
            sum=0
        if maxi<0:
            maxi=0
    print(maxi)
array=[-2,-1.-3,4,-1,2,1,-5,-4] 
maxSubarraySum(array):
