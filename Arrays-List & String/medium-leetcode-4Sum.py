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

# ==================== Better Solution ====================
def four_Sum(nums, target):
    n = len(nums)
    ans = []
    nums.sort()
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            k = j + 1
            l = n - 1
            while k < l:
                _sum = nums[i] + nums[j] + nums[k] + nums[l]
                if _sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif _sum < target:
                    k += 1
                else:
                    l -= 1
    print(ans)
nums = [4, 3, 3, 4, 4, 2, 1, 2, 1, 1]
target = 9
ans = four_Sum(nums, target)
