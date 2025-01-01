#  Longest substring with distinct characters
# problem link: https://www.geeksforgeeks.org/problems/longest-distinct-characters-in-string5848/1
# Given a string s, find the length of the longest substring with all distinct characters. 
# Date: 01/01/2025
# Method 1:
def longestsubStr(s):
  i = 0
  j = 1
  n = len(s)
  current_sub = s[0]
  global_sub = ""
  while i<n and j<n:
    if s[j] not in current_sub:
      current_sub += s[j]
       j += 1
    else:
      i += 1
      current_sub = s[i]
      j = i+1
    if len(global_sub) <len(current_sub):
      global_sub = current_sub
      print("The length of longest substring is ",len(global_sub))
s="abcdefabcbb"
longestsubStr(s)
# Optimal Method: 

def longestUniqueSubstr(self, s):
        # code here
  max_len = 0
  c1 = defaultdict(int)
  count = 0
  j = 0
  for i in range(len(s)):
    c1[s[i]] += 1
    if c1[s[i]] > 1:
      count = 0
      while c1[s[i]] != 1:
        c1[s[j]] -= 1
        j += 1
        max_len = max(max_len, i-j + 1)
        print(max_len)
s="abcdefabcbb"
longestUniqueSubstr(s)        
        
