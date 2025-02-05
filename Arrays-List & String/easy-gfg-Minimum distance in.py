# Minimum distance in an Array
# problem link: 
# Description: You are given an array, arr[]. Find the minimum index based distance between two distinct elements of the array, x and y. Return -1, if either x or y does not exist in the array.
# date 05/02/2025
# This can be solved in two ways
# 1 using brute Force

def mindist(arr, x, y):
  n = lne(arr)
  min_distance = float('inf')
  for i in range(n):
     if arr[i] == x:
        for j in range(n):
          if arr[j] == y:
            min_distance = min(min_distance, abs(i -j))
  if min_distance != float('inf')
    print("the minimum distance between two array is", min_distance)
  else:
    print(-1)
arr = [1, 2, 3, 2]
x = 1
y = 2
mindist(arr,x,y)

# Brute Force

def minDist(array, num1, num2):
  n = len(arr)
  p = -1
  q = -1
  min_dist = float('inf')
  for i in range(n):
    if arr[i]==num1:
      p = x
      if q!= -1:
        min_dist = min(min_dist, abs(p-q))
    elif p!= -1:
      q = num2
      if p != -1:
        min_dist = min(min_dist, abs(p-q))
  if  p == -1 or q == -1:
    return - 1
  if min_dist != float('inf')
    print("the minimum distance between two array is", min_dist)
  else:
    print(-1)
array = [86, 39, 90, 67, 84, 66, 62]
num1 = 42
num2 = 12
minDist(array, num1, num2)

