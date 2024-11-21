# 3Sum
# Link to the https://leetcode.com/problems/3sum/description/ 
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Date: 21/11/2024
# The Problem Consist of two solutions. Brute force solution,and a optimal Solution. 
# ==================== Brute force Solution ====================
def threesum(arr):
  st=set()
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      for k in range(j+1,len(arr)):
        if arr[i] + arr[j] + arr[k] == 0:
          temp = [arr[i], arr[j], arr[k]]
          temp.sort()
          st.add(tuple(temp))
  ans = [list(item) for item in st]
  print(ans)
arr=[-1,0,1,2,-1,-4]
threesum(arr)
# ==================== Better Solution ====================
def threeSum(a):
  for i in range(len(a)):
    hashset=set()
    for j in range(i,len(a)):
      third=-(a[i] + a[j])
      if third in hashset:
        temp = [a[i], a[j], third]
        temp.sort()
        st.add(tuple(temp))
      hashset.add(a[j])
    ans=list(st)
a=[-1,0,1,2,-1,-4]
threeSum(a)
