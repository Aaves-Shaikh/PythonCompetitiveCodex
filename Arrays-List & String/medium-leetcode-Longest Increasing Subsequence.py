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

# Optimal Solution
def longestOfList(arr):
  res=[]
  def binarysearch(res, n):
    left = 0
    right = len(res)-1
    while left <= right:
      mid= (left+right)//2
      if res[mid] == n:
        return mid
      elif res[mid] > n:
        right = mid- 1
      else:
        left = mid + 1
      return left

  for n in nums:
    if not res or res[-1] < n:
      res.append(n)
    else:
      ids = binarysearch(res, n)
      res[ids] = n
  print(len(res))
arr= [0,1,0,3,2,3]
longestOfList(arr)
