# Largest subarray of 0's and 1's
# problem link: https://www.geeksforgeeks.org/problems/largest-subarray-of-0s-and-1s/1
# description: Given an array arr of 0s and 1s. Find and return the length of the longest subarray with equal number of 0s and 1s.
# Date: 16/1/2025
#  This problem have two solution 
# Brute force approch 
def maxlen(arr):
  n = len(arr)
  for i in range(n):
    if arr[i]==0:
      arr[i] - -1
  maxi = 0 
  map = {}
  sum = 0
  for i in range(n):
    sum += arr[i]
    if sum == 0:
      maxi = i+1
    else:
      if sum in map:
        maxi = max(maxi, i-map[sum])
      else:
        map[sum] = i
  print("The amximum length of Largest subarray of 0's and 1's is: ", maxi)
arr=[1, 0, 1, 1, 1, 0, 0]
maxlen(arr)
      
# Better Solution
 def maximumLen(array):
   n = len(array)
   preSum = {0:-1}
   currSum = 0
   ans = 0
   for i in range(n):
     currSum+= (1 if arr[i] else -1)
     if currSum in preSum:
       ans=max(ans,i-preSum[currSum])
    if currSum not in preSum:
      preSum[currSum]=i
  print("The amximum length of Largest subarray of 0's and 1's is: ", ans)
array = [0, 0, 1, 1, 0]
maximumLen(array)
