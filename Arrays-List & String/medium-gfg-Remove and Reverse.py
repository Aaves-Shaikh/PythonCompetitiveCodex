# Remove and Reverse
# Link to the https://www.geeksforgeeks.org/problems/remove-and-reverse--170634/0 
Given a string S which consists of only lowercase English alphabets, you have to perform the below operations:
# If the string S contains any repeating character, 
# remove the first repeating character and reverse the string and again perform the above operation on the modified string, otherwise, you stop.
# Date: 14/11/2024
# The Problem Consist of two solutions. Brute force solution,and a optimal Solution. 
# ==================== Brute force Solution ====================
from typing import List
from array import array
#User function Template for python3
def removeReverse(s): 
  counter = array('I', [0] * 128)
  s_len = len(s)
  included = [True] * s_len
  for c in s:
      counter[ord(c)] += 1
      left = 0
      right = s_len - 1
      rev = False
      while left <= right:
          first = s[left]
          last = s[right]
          if not rev:
              if counter[ord(first)] > 1:
                  counter[ord(first)] -= 1
                  rev = not rev
                  included[left] = False
              left += 1
          else:
              if counter[ord(last)] > 1:
                counter[ord(last)] -= 1
                rev = not rev
                included[right] = False
              right -= 1
          res = ''
      for i in range(s_len):
        if included[i]:
          res += s[i]        
        if rev:
          res = res[::-1]
  print(res)
