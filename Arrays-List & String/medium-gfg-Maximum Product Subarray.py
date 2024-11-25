# Maximun sub array product or also know as Kadane's Algorithm but for using kadaen's Algorithm there needs to be done some modification
# Link to the problem https://www.geeksforgeeks.org/problems/maximum-product-subarray3604/1
# Given an array. The task is to find the maximum sub array product of the element in it.
# Date: 25/11/2024
# The Problem Consist of three solution. Brute force solution, better Solution, and two optimal Solution. 
# Method 1 the  Brute Force Method 
def maxproductarray(nums):
  result=float(-inf')
  for i in range(len(nums)-1):
    for j in range(i+1, len(num)):
      prod=1
      for k in range(len(i,j+1)):
        prod *=nums[k]
      result = max(result,prod)
   print(result)
nums = [1, 2, -3, 0, -4, -5]
maxproductarray(nums)

