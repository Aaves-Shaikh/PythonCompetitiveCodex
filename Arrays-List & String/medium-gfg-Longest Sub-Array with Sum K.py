# Longest Sub-Array with Sum K
# Link to the problem https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
# Given an array arr[] containing integers and an integer k,
# your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. It is guaranteed that a valid subarray exists.
# The Problem Consist of three solutions, two Brute force methods one better solution and optimal solution 
# Method 1 the  Brute Force Method
def longestsubarray(arr, k):
  n=len(arr)
  longest=0
  for i in range(n):
    for j in range(i,n):
      s=0
      for k in range(i,j+1):
        s+=arr[j]
        if s==k:
          longest=max(longest, j-i+1)
  print(longest)
arr=[2, 3, 5, 1, 9]
k= 10
longestsubarray(arr,k)
