# Container With Most Water
# Problem Link: https://leetcode.com/problems/container-with-most-water/description/
# description: You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water
# Date 08/01/2025
# Method 1
def maxArea(arr):
  left,right=0,len(arr)-1
  area_max = 0 
  while left < right:
    area_max = max(area_max, (right - left ) * min(arr[left], arr[right]))
    if arr[left] < arr[right]:
      left += 1
    else:
      right -= 1
    print("The maximum water that can be stored is",area_max)
arr= [1,8,6,2,5,4,8,3,7]
maxArea(arr)
