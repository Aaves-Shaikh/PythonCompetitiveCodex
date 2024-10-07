# Largest Element in Array 
# Link to the problem https://www.geeksforgeeks.org/problems/largest-element-in-array4009/0
# Given an array, arr. The task is to find the largest element in it.
# Date: 02/10/2024
# The Problem Consist of two solution. A better Solution and A optimal Solution. 
# Method 1 the better Soln using Brute Force Method 
def max_array_brt(arr):
    max_element=arr[0]
    for i in range(len(arr)):
        if arr[i]>max_element:
            max_element=arr[i]        
    print("The maximum element is: ",max_element)
arr=[1, 8, 7, 56, 90]
max_array(arr)

# Method 2 Most optimal Soln. using the Max function
def max_arr(arr1):
    print(max(arr1))
arr1=[1, 8, 7, 56, 90]
max_arr(arr1)

# taking Dynamic input and using the exeception to check if the value of n is equal to  len(arr)
def max_arr(n,arr):  
    if len(arr)!=n:
        raise Exception ("Length of array does not match the given number")
    max_element=arr[0]
    for i in arr:
        if  i>max_element:
            max_element=i
    print(max_element)
n=int(input("Enter the number of unsorted array: "))
arr=list(map(int,input("Enter the numbers: ").strip().split()))
max_arr(n,arr)
# The maximum subarray sum is: 6
