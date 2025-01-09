# Search in Rotated Sorted Array
# Problem Link: https://leetcode.com/problems/search-in-rotated-sorted-array/description/
# Description: Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# Date: 01/09/2025
# This problem consist of two solutions 1. Brute force and 2. Optimal solution
# Brute force solution
def searchArr(arr, target):
  n = len(arr)
  for i in range(n):
    if arr[i] == target:
      print("The number in the rotated array found at the index" , i)
    else:
      print(f"The number {target}, is no where to be found  in the arr")
arr = [7, 8, 9, 1, 2, 3, 4, 5, 6]
target = 2
searchArr(arr, target)

# Optimal Solution

def searcharr(array, tar):
  N = len(array)
  low = 0 
  high =  N - 1
  while low <= high:
    mid = (low + high)//2
    if array[mid] == tar:
      print("The number in the rotated array found at the index" ,mid)
    elif array[low] <= array[mid] :
      if array[low] <= tar and tar <= array[mid]:
        high = mid - 1
      else:
        low  = mid + 1
    elif array[mid] <= array[high]:
      if array[low] <= tar and tar <= array[high]:
        low = mid + 1
      else:
        high = mid - 1
    else:
       print(f"The number {target}, is no where to be found  in the arr")
array = [4,5,6,7,0,1,2]
tar = 3
searcharr(array, tar)
