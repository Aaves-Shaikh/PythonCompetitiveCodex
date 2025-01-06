# Two Sum
# problem link: https://leetcode.com/problems/two-sum/description/
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# Date 06/01/2025
# This problem can be solved via two solution one is brute force and naive solution while the other is the optimal solution 
# Brute force solution 
def twosums(arr,target):
  for i in range(len(arr)):
    for j in range(len(arr)):
      if i == j :
        continue
      elif arr[i] + arr[j] == target:
        print("The two sum that adds upto the index value are",i , j)

arr=[2,7,11,15]
target = 9
twosums(arr,target)

# Optimal Solution 
def twoSums(array,tar):
  hashset= set()
  pair=[]
  for num in (array):
    j = num -target
    if j in hashset:
      pair.append((num,j))
    hashset.add(num)
  print(pair)
array=[2,7,11,15]
tar = 9
twoSums(array,tar)
