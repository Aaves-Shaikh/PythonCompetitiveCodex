# Duplicate Elements
# Given an array. The task is to find the duplicate elements and print them.
# Date: 14/10/2024
# The Problem Consist of three solution. A brute force Solution, a better solution, and a optimal Solution. 
# Metod1: using the for loop we check if the element is present in the list is yes to print it
from collections import Counter
def sortedDuplicate(n,arr):
  d=Counter(arr)
  new=[]
  for i in range(n):
    if d[i]>1:
      i.append(new)
     if new:
       new.sort()
       for j in new:
         print(j, end=" ")
    else:
      print(-1)
n=9
arr= [3, 4, 5, 7, 8, 1, 2, 1, 3]
# Method 2: Better approach using freq of the array 
def sorted_duplicate(N,Array):
  freq=[0]*(N+1)
  for i in range(N):
    if freq[Array[i]]==0:
      freq[Array[i]]+=1
    else:
      print(Array[i],end=" ")
   print(-1)
N=5
Array=[5,5,3,1,2]
