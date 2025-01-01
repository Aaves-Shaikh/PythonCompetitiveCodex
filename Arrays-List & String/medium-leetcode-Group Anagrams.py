# Group Anagrams
# problem link: https://leetcode.com/problems/group-anagrams/description/
# Given an array of strings, return all groups of strings that are anagrams. The groups must be created in order of their appearance in the original array. 
# Date: 01/01/2025
# Method 1 :
def angramGroup(arr):
  hashmap={}
  for i in range(len(arr)):
    new_arr=sorted(arr)
    ele=",".join(new_arr)
    if new_arr not in hashmap:
      hashmap[ele]=[]
    hashmap[ele].append(arr[i])
  return [x for x in hashmap.values()]
arr=  ["act", "god", "cat", "dog", "tac"]
angramGroup(arr)
