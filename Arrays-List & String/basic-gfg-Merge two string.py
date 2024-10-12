# Merge two strings in array
# Link to the problem https://www.geeksforgeeks.org/problems/merge-two-strings2736/1
# Given two string. The task is to merge both strings alternatively.
# Date: 10/12/2024
# The Problem Consist of two solution. A better Solution and A optimal Solution. 
# Method 1 the better Soln using Brute Force Method 
def merge(S1, S2):
  res=""
  for i in range(min(len(S1),len(S2))):
    res+=S1[i]+S2[i]  
    if len(S1)==len(S2):
      return res 
  return res+S1[i+1:] if len(S1)>len(S2) else res+S2[i+1:]

s1="hello"
s2="Bye"
merge(s1,s2)
