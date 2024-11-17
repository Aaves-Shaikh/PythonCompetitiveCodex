# Reverse Array
# problem link https://www.geeksforgeeks.org/problems/reverse-an-array/1
# Date 11/172024
# You are given an array of integers arr[]. Your task is to reverse the given array.
# In this problem we have two solution divide and proceed and using two pointes 
# Two pointers 
def reversearray(arr):
  n=len(arr)
  l=0
  r=n-1
  while (l<=r):
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
    print("The reversed arrya is", arr)
arr=[1,2,3,4,5]
reversearray(arr)
