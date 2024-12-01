# Non Repeating Character
# Problem Link:https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/1
# Given a string s consisting of lowercase Latin Letters. Return the first non-repeating character in s. If there is no non-repeating character, return -1.
# Date:01/12/2024
# This prob,em consist of two solutions
# brute Force Method
def nonrepeatchar(s):
  dic = {}
  l = []
  for i in s:
    if i in dic:
      dic[i]+=1
    else:
      dic[i]= 1          
  for i in s:
    if (dic[i]==1):
      print(f"The non repeating number is {i}")
    else:
      print("All the char are repeating in the given string")
      print(-1)
s="Nitin"
nonrepeatchar(s)

# Optimal Solution in this we are using "from collections import Counter" to keep the count and return the single element 
def nonRepeatChar(str):
  a=Counter(s)
  for i,j in a.items():
    if j==1:
      print(i)
      break
    else:
      print(-1)
str="aabbccc"  
nonRepeatChar(str)
