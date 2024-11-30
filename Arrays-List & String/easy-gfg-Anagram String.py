# Anagram String
# problem Link: https://www.geeksforgeeks.org/problems/anagram-1587115620/1
# Given two strings s1 and s2 consisting of lowercase characters. The task is to check whether two given strings are an anagram of each other or not.
# An anagram of a string is another string that contains the same characters, only the order of characters can be different
# Date 30/11/2024
# the problem cotains of 3 solutions 
def areAnagrams(s1, s2):
  s1=list(s1)
  s2=list(s2)
  s1.sort()
  s2.sort()
  if len(s1)!=len(s2):
    print(False)
  for i in range(len(s1)):
    if s1[i]!=s2[i]:
      print(False)
    else:
      print(True)
s1=Nitin
s2=Tinnin
areAnagrams(s1,s2)
