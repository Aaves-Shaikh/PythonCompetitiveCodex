# Link of the problem https://www.geeksforgeeks.org/problems/longest-consecutive-subsequence2449/1
# Given an array.  Find the length of the longest sub-sequence such that elements in the subsequence are consecutive integers, the consecutive numbers can be in any order.
# Date: 12/11/2024
# The Problem Consist of three Brute force solution, better solution and optimal solution 
# Method 1 the  Brute Force Method 
def linearsearch(a,num):
  n=len(a)
  for i in range(n):
    if a[i]==num:
      return True
  return False
def longsubsequence(a):
  n=len(a)
  longest=1
  for i in range(n):
    x=a[i]
    cnt=1
    while linearsearch(a,x+1):
      x+=1
      cnt+=1
    longest=max(logest,cnt)
    print(longest)
a = [100, 200, 1, 2, 3, 4]
longsubsequence(a)
