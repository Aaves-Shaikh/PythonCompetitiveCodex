# First Missing Positive
# Problem Link: https://leetcode.com/problems/first-missing-positive/description/
# Description: Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
# Date: 29/01/2025
# This problem have two solutions 1. Brute force method and 2. Optimla solution
# Brute force method

def firstmissing(arr):
  target = 1
  arr.sort()
  n = len(nums)
  for n in arr:
    if n > 0 and n == target:
      target += 1
    else:
      print("The first missing positive number is: ", target)
      return
   print("The first missing positive number is: ", target)
arr = [3,4,-1,1]
firstmissing(arr) # output = 2

def firstMissing(nums):
  for n in nums:
    idx = abs(n) - 1
    if idx < len(nums) and nums[idx] > 0:
      nums[idx] *= -1
  for i in range(len(nums)):
    if nums[i] > 0:
      print(i +1)
      return
  print(len(nums) + 1)
nums = [1,2,4,0]
firstMissing(nums) # output = 3
