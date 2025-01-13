# Find the Duplicate Number
# Problem Link: https://leetcode.com/problems/find-the-duplicate-number/description/
# Description: Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive. There is only one repeated number in nums, return this repeated number.
# Date: 12/1/2025
# Very optimal solution using Floyd’s Cycle Finding Algorithm
def findduplicate(nums):
  slow,fast = 0,0
  check = 0
  while True:
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast:
      break
  while True:
    slow = nums[slow]
    check = nums[fast]
    if slow == fast:
      break
  print("The duplicate number in the array is: ",check)
nums = [3,1,3,4,2]
findduplicate(nums)
