# 4Sum
# problem Link https://leetcode.com/problems/4sum/description/
# Date: 22/11/2024
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
# The Problem Consist of two solutions. Brute force solution,and a optimal Solution. 
# ==================== Brute force Solution ====================
from typing import List
from collections import deque
import itertools

def quads(arr,target):
   n = len(nums) # size of the array
   st = set()
   for i in range(n):
     for j in range(i + 1, n):
       for k in range(j + 1, n):
         for l in range(k + 1, n):
           sum = nums[i] + nums[j]
           sum += nums[k]
           sum += nums[l]
    if sum == target:
      temp = [nums[i], nums[j], nums[k], nums[l]]
      temp.sort()
      st.add(tuple(temp))
    ans = [list(x) for x in st]
    print(ans)
arr = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
quads(qrr,target)
# ==================== Better Solution ====================
def fourSum(nums, target):
    n = len(nums)
    st = set()
    for i in range(n):
        for j in range(i+1, n):
            hashset = set()
            for k in range(j+1, n):
                sum_ = nums[i] + nums[j] + nums[k]
                fourth = target - sum_
                if fourth in hashset:
                    temp = [nums[i], nums[j], nums[k], fourth]
                    temp.sort()
                    st.add(tuple(temp))
                hashset.add(nums[k])
    ans = [list(t) for t in st]
    print(ans)
nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
fourSum(nums, target)
