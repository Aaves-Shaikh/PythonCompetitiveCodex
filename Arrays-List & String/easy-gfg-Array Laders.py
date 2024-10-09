# Array Laders
# Link to the problem https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1
# Given an array, arr. if the left array is greater than right array.
# Date: 09/10/2024
# The Problem Consist of two solutions. A brute force Solution, and A optimal Solution. 
# ==================== Brute force Solution ====================
def arrayladers(arr):
  ans=[]
  laders=True
  for i in range(len(arr)):
    for j in range(i,len(arr)):
      if arr[j]>arr[i]:
        laders=False
        break
    ans.append(arr[i])
    print(ans)
    print(ans)
    ans.sort()   #if the interviewer ask for the sorted order 
    print(ans)
    ans.reverse() #if the interviewer ask for the reverse order
    print(ans)
arr=[23,30,34,60,20,10,11,16]
arrayladers(arr)
# ==================== Optimal Solution ====================
def array_Laders(Array):
  answer=[]
  max_elem=Array[-1]
  answer.append(Array[-1])
  for i in range(len(Array)-1,-1,-1):
    if Array[i]>max_elem:
      answer.append(Array[i])
    print(answer)
    answer.reverse()  #if the interviewer ask for the reverse order
    print("from left to right ",answer)
    answer.sort()  #if the interviewer ask for the sorted order
    print("In sorted order ", answer)
Array=[23,30,34,60,20,10,11,16]
array_leaders(Array)
