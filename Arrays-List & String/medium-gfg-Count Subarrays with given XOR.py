# Count Subarrays with given XOR
# Problem Link: https://www.geeksforgeeks.org/problems/count-subarray-with-given-xor/1
# Given an array of integers arr[] and a number k, count the number of subarrays having XOR of their elements as k.
# Date 03/01/2025
# Method 1: Brute force solution.
from collections import defaultdict

def subarraywithxork(a ,k):
  n = len(a)
  c = 0
  for i in range(n):
    for j in range(i, n):
      xorr  = 0
      for K in range(i, j+1):
        xorr = xorr ^ a[K]
      if (xorr == k):
        c += 1
  print("The total number of xor element with subarray K is", c) 
a=   [4, 2, 2, 6, 4]
k = 6
subarraywithxork(a ,k)
