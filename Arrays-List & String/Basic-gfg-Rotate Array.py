# Description there will be two different DSA problems below 1st will to left rotate the array and second will to right rotate the array 
# Rotate Array 
# Link to the problem # https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/0
# Given an array, arr. Rotate the array by one play in clock wise and anticlock wise. 
# Date: 05/10/2024
# The Problem Consist of two solution first is brute force and second will optimal Solution.
# ========================Left Rotate(Anti Clock wise rotation)======================== #
# Brute Force Method
def leftrotate(arr):
    temp=arr[0]
    for i in range(len(arr)-1):
        arr[i]=arr[i+1]
    arr[-1]=temp
    print(arr)
arr=[1,2,3,4,5]
leftrotate(arr)
# ========================Right Rotate(Clock wise rotation)======================== #
# Brute Force Method
def rightrotate(arr):
  arr[0]=temp
  for i in range(len(arr)-1,0,-1):
    arr[i]=arr[i-1]
  temp=arr[-1]
  print(arr)
arr=[1,2,3,4,5,6,7]
rightrotate(arr)
# --------------------------------------------------Optimal Solution --------------------------------------------------#
def rightrotate(arr):
  last_item = arr[-1]
  arr.pop()
  # Appending that element in the first index
  arr.insert(0, last_item)
  print(arr)
arr=[1,2,3,4,5,6,7]
rightrotate(arr)
