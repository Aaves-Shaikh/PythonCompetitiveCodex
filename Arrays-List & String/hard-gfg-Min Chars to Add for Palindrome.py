# Min Chars to Add for Palindrome
# problem link: https://www.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/1
# Given a string s, the task is to find the minimum characters to be added at the front to make the string palindrome.
# Date 12/3/2024
# This problem consist of two solution also know as two different algorithm 
# 1st lps Algorithm
def minChar(s):
  rev_s=s[::-1]
  combined = s + "#"+rev_s
  n=len(combined)
  lps=[0]*n
  for i in range(1,n):
    j=lps[i-1]
    while j>0 and combined[i]!=combined[j]:
      j=lps[j-1]
    if combined[i] == combined[j]:
      j+=1
    lps[i]=j
  return len(s)-lps[-1]
s="abc"
minChar(s)
