# Subarray Sum Equals K
# Problem link: https://leetcode.com/problems/subarray-sum-equals-k/description/
# Description : Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k. A subarray is a contiguous non-empty sequence of elements within an array.
# Date: 10/01/2025
# This problem consist of three solution, Brute force, better solution and optimal solution
# brute force method

def subarraysum(arr, tar):
  n = len(arr)
  c = 0
  for i in range(n):
    for j in range(i, n):
      sub_arraysum = sum(arr[i: j+1])
      if sub_arraysum == tar:
        cnt += 1
  print(" The total number of subarrays whose sum equals to k are: ", 
arr = [1,1,1]
tar = 2
subarraysum(arr, tar)
