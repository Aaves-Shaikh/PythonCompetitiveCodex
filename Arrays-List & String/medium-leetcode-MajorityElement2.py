# Majority Element n/3 
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
# Date: 10/11/2024
# the probelm link https://leetcode.com/problems/majority-element-ii/description/ 
# The Problem Consist of three solution. A brute force Solution, a better solution and a optimal Solution. 
# Metod1:
from typing import List
def majorityElement(arr):
  n=len(arr)
  ls=[]
  for i in range(n):
    if len(ls)==0 or len(ls)!=arr[i]:
      cnt=0
      for j in range(n):
        if arr[i]==arr[j]:
          cnt+=1
      if cnt>(n//3):
        ls.append(arr[i])
  return ls
arr=[1,1,2,2,3,3,3,3,1,1]
majorityElement(arr)
