# String Duplicates Removal
# Problem link: https://www.geeksforgeeks.org/problems/remove-all-duplicates-from-a-given-string4321/1?
# Given a string s which may contain lowercase and uppercase characters. The task is to remove all duplicate characters from the string and find the resultant string
# The order of remaining characters in the output should be same as in the original string.
# Date: 02/01/2025
# Method 1: 
def removeDuplicates(str):
  a=[]
  seen=set()
  for char in str:
    if char not in seen:
      a.ppend(char)
      seen.add(char)
  print("The string after removal of duplicate elements is:", "".join(a))
str = "HaPpyNewYear"
removeDuplicates(str)
