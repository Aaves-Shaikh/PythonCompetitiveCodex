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
  print(ls)
arr=[1,1,2,2,3,3,3,3,1,1]
majorityElement(arr)

# Better Solution
def majority_element(num):
  v=len(num)
  counter=counter(arr)
  for nums,count in counter.items():
    if count>v//3:
      print(num)
    else:
      print("No majority Element")
num=[1,1,2,2,3,3,3,3,1,1]
majority_element(num)

# optimal solution: this is similar as the majorityelement with n/2 using the Mooze voting  Algo.
def majorityelement(array):
  l=len(array)
  cnt1,cnt2=0,0
  ele1,ele2=float('-inf'), float('-inf')
  for i in range(n):
    if cn1==0 and el2!=array[i]:
      cnt1=1
      ele1=array[i]
    elif array[i]==ele1:
      cnt1+=1
    elif array[i]==ele2:
      cnt2+=1
    else:
      cnt1-=1
      cnt2-=1
  ls = []
  cnt1, cnt2 = 0, 0
    for i in range(n):
        if array[i] == ele1:
            cnt1 += 1
        if array[i] == ele2:
            cnt2 += 1
    mini = int(n / 3) + 1
    if cnt1 >= mini:
        ls.append(ele1)
    if cnt2 >= mini:
        ls.append(ele2)
array=[11, 33, 33, 11, 33, 11]
majorityelement(array)
