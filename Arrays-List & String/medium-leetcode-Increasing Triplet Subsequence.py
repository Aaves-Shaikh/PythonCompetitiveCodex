# Increasing Triplet Subsequence
# Problem Link: https://leetcode.com/problems/increasing-triplet-subsequence/
# Description: Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.
# Date: 12/02/2025
# Better Solution
def increasingTriplet(nums):
  first = float('inf')
  second = float('inf')
  for i in nums:
    if i <= first:
        first = i
    elif i <= second:
        second = i
    else:
        return True
  return False
nums = [2,1,5,0,4,6]
increasingTriplet(nums)
