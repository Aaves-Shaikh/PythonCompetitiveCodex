# Longest Increasing Subsequence
# Problem link: https://leetcode.com/problems/longest-increasing-subsequence/description/
# Description: Given an integer array nums, return the length of the longest strictly increasing subsequence
# Date: 13/1/2025
# For this problem we have two solutions, 1 brute force solution 2 Optimal Solution using binary search
def longestoflis(nums):
  n=len(nums)
  dp = [1] * n
  maxi = -sys.maxsize -1
  for i in range(n):
    for j in range(i):
      if nums[i] > nums[j]:
        dp[i] = max(dp[i], dp[j] + 1)
  print("The longest increasing subsequence is: ",max(dp))
nums = [10,9,2,5,3,7,101,18]
longestoflis(nums)
