# Majority Element in Array 
# Given an array. The task is to find the majority elements in array if present .
# Date: 23/10/2024
# the probelm link https://www.geeksforgeeks.org/problems/majority-element-1587115620/1 
# The Problem Consist of three solution. A brute force Solution, a better solution and a optimal Solution. 
# Metod1: using the for loop we check if the element is present in the list if no we append it else we move forward
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
