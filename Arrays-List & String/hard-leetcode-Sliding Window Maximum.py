# Sliding Window Maximum
# Problem link: https://leetcode.com/problems/sliding-window-maximum/description/
# Description: You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
# Date: 21/01/2025
# The problem have two solution as of now :
# Brute force very naive solution
def maxslidingwindow(arr,k):
  n = len(arr)
  res = []
  for i in range(n-k+1): # The outer loop will iterate from i = 0 to i = n - k = 8 - 3 = 5. This means i will take values 0, 1, 2, 3, 4, and 5
    maxi = float('-inf') # reset the value of maximun so that we can get the required output
    for j in range(i, i+k):
      if arr[j] > maxi:
        maxi = arr[j]
    res.append(maxi)
  print("The maximun in a sliding window of size k which is moving from the very left of the array to the very right are: ", res)
arr  = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3 #output [3, 3, 5, 5, 6] 
maxslidingwindow(arr,k):
# This is not a good solution as it takes two loops and have a large time complexity 

#Better approch
def maxSliding_Window(array, X):
  Len = len(array)
  result  = []
  q = deque()
  for ind, nums in enumerate(array):
    while q and q[-1]  < nums:
      q.pop()
    q.append(nums)
    if ind >= X and nums[ind - X] == q[0]:
      q.popleft()
    if ind >= X -1:
      result.append(q[0])
  print(result)
array = [1, 3, -1, -3, 5, 3, 6, 7]
X = 3
maxSliding_Window(array, X)
