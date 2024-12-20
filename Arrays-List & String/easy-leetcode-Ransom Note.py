# Ransom Note
# Problem Link: https://leetcode.com/problems/ransom-note/description/
# Description: Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Date: 20/12/2024
# The Problem consist of two solution one using brute force: 
# Brute force solution

def canConstruct(ransomNote, magazine):
  maga_hash={}
  for i in magazine:
    maga_hash[i]=1 + maga_hash.get(i,0)
    for j in ransomNote:
      if j not in maga_hash or maga_hash[j] <=0:
        print("False Not a ransomNote string: ")
        maga_hash[j] -=1
      else:
        print("The given string is a ransomNote ")
ransomNote= "aa"
magazine= "ab"
canConstruct(ransomNote, magazine):
# Optimal Solution

def canConstruct(self, ransomNote, magazine):
  found = False
        # ransomNote from magazine
  for letter_a in ransomNote:
    for i,letter_b in enumerate(magazine):
      if letter_a==letter_b:
        magazine =
        found = True
        break
      if not found:
          print("False")
      else:
          found = False
      print("True")
            
ransomNote= "aa"
magazine= "aab"
canConstruct(ransomNote, magazine):  
