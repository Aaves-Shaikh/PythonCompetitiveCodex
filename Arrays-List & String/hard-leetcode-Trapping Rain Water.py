# Trapping Rain Water
# Problem Link: https://leetcode.com/problems/trapping-rain-water/description/
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
#  Date: 7/1/2025
# Method 1:
def trappingrainwater(arr):
  left = 0 
  right = len(arr)-1
  left_max = 0
  right_max = 0
  cnt = 0 
  while left < right:
    if arr[left] < arr[right]:
      if arr[left]> left_max:
        left_max = arr[left]
      else:
        cnt += left_max - arr[left]
      left += 1
    else:
      if arr[right] > right_max :
        right_max = right_max
      else:
        cnt += right_max - arr[right]
      right -= 1
  print("The maximux rain water that can be trapped is: ",cnt)
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
trappingrainwater(arr)
