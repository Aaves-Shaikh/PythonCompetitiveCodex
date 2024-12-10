# Non-overlapping Intervals
# Link to the problem https://www.geeksforgeeks.org/problems/non-overlapping-intervals/1
# Given an array. The task is to return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping
# Date: 10/12/2024
# The Problem Consist of two solution. 
# Method 1 the  Brute Force Method 
def minremove(arr):
  arr.sort()
  cnt=0
  l=len(arr)-2
  curr=interval[-1]
  while i> 0:
    if curr[0]<arr[i][1]:
      cnt+=1
    else:
      curr = arr[i]
    i-=1
  print("The minimum number of intervals needs to remove: ",cnt)
arr=[[1, 2], [2, 3], [3, 4], [1, 3]]
minremove(arr)
