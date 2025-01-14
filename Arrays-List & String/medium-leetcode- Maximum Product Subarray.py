#  Maximum Product Subarray
# Problem Link: https://leetcode.com/problems/maximum-product-subarray/description/
# Description: Given an integer array nums, find a subarray that has the largest product, and return the product.
# Date: 14/01/2025
# To solve this roblem we have a better solution 
def maxprod(arr):
  res = max(arr)
  curr_max =  curr_min = 1
  for n in arr:
    temp = curr_max * n
    curr_max  = max(temp , curr_min * n, n)
    curr_min  = min(temp , curr_min * n, n)
    res = max(curr_max, res)
  print("The maximum product of the array is: ", res)
arr = [2,3,-2,4]
maxprod(arr)
