# Kth Largest Element in an Array
# Problem Link: https://leetcode.com/problems/kth-largest-element-in-an-array/description/
# Description: Given an integer array nums and an integer k, return the kth largest element in the array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Date: 23/01/2025
# The problem will  have three solution 1 Brute Force(Max Heap) 2 Better Solution(Min Heap) 3 Using quick sort
# Brute Force
import heapq
def find_Kth_Largest(arr, k):
  for i in range(len(arr)):
    arr[i] = -arr[i]
  heapq.heapify(arr)
  for j in range(k-1):
    heapq.heappop(arr)
  print("kth largest element in the array is: ",-heapq.heappop(arr))
arr = [3,2,1,5,6,4]
k = 2 #output = 5
find_Kth_Largest(arr, k)

# Better Solution
def findkthlargest(array, L):
  min_heap = []
  for num in array:
    if len(min_heap) < L:
      heapq.heappush(min_heap, num)
    else:
      heapq.heappushpop(min_heap, num)
  print("kth largest element in the array is: ",min_heap[0])
array= [3,2,3,1,2,4,5,5,6]
L = 4
findkthlargest(array, L)
