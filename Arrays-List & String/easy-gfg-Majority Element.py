# Majority Element in Array 
# Given an array. The task is to find the majority elements in array if present .
# Date: 23/10/2024
# the probelm link https://www.geeksforgeeks.org/problems/majority-element-1587115620/1 
# The Problem Consist of three solution. A brute force Solution, a better solution and a optimal Solution. 
# Metod1:
from collections import Counter
def majorityElement(arr):
  n=len(arr)//2
  for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
      if arr[j]==arr[i]:
        count+=1
      if count>n:
        print("the majority element is:",arr[i],"and it's count is:",count)
      else:
        print("No majority elements!!!")
arr=[1,1, 8, 7, 9,56, 90,99,99,99]
majorityElement(arr)

# method 2: using counter
def majorityelem(A):
  N=len(A)//2
  counter=counter(A)
  for num, c in counter.items():
    if c>N:
      print("the majority element is:",num,"and it's count is:",c)
            return 
  print("No majority elements!!!")
  return
A=[1,1, 8,7,9,56, 90,99,99,99,99,99,99,99,99,99]
majorityelem(A)

# method 3: using Mooze voting algo
def majority_elem(Array):
  elem=none
  cnt=0
  l=len(Array)
  for i range(l):
    if cnt==0:
      cnt=1
      Array[i]=elem
    elif elem=Array[i]:
      cnt+=1
    else:
      cnt-=1
  cnt1=0
  for i in range(l):
    if elem==Array[i]:
      cnt1 +=1
      print(elem)
        return 
  print(-1)
Array=[1,1, 8,7,9,56, 90,99,99,99,99,99,99,99,99,99]
majority_elem(Array)
