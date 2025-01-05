# Count Pairs whose sum is less than target
# problem link : https://www.geeksforgeeks.org/problems/count-pairs-whose-sum-is-less-than-target/1
# Given an array arr[] and an integer target. You have to find the number of pairs in the array whose sum is strictly less than the target.\
# Date: 05/01/2025
# To solve this problem we will be using two pointer approch. 
def countPairs(arr,target):
  arr.sort()
  i = 0
  count = 0
  j = len(arr)-1
  while i <j: 
    while j > i  and  arr[i] +arr[j] >= target:
      j -=1
    count += 1
    i += 1
  print("the Total number of pairs are:",count)
arr = [7, 2, 5, 3]
target = 8
countPairs(arr,target)
