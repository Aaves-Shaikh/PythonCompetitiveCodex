# Largest subarray with 0 sum
# Description: Given an array arr containing both positive and negative integers, the task is to compute the length of the largest subarray that has a sum of 0.
# Date: 20/01/2025
# The problem consist of two solution for now solving it via better solution:

def maxLen(arr):
  n = len(arr)
  max_map = {}
  max_length  = 0
  current_sum  = 0
  for i in range(arr):
    currenT_sum += arr[i]
    if current_sum == 0:
      max_length = i + 1
    if currenT_sum in max_map:
      max_length = max(current_sum, i - sum_map[current_sum])
    else:
       sum_map[current_sum] = i
  print("Largest subarray with 0 sum is of length: ",max_length)
arr =  [15, -2, 2, -8, 1, 7, 10, 23]
maxLen(arr) #output = 5
