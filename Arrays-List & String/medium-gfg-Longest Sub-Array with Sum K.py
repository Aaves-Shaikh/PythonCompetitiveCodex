# Longest Sub-Array with Sum K
# Link to the problem https://www.geeksforgeeks.org/problems/longest-sub-array-with-sum-k0809/1
# Given an array arr[] containing integers and an integer k,
# your task is to find the length of the longest subarray where the sum of its elements is equal to the given value k. It is guaranteed that a valid subarray exists.
# The Problem Consist of three solutions, two Brute force methods one better solution and optimal solution 
# Method 1 the  Brute Force Method
def longestsubarray(arr, k):
  n=len(arr)
  longest=0
  for i in range(n):
    for j in range(i,n):
      s=0
      for k in range(i,j+1): # this for loop can be removed to improve the time complexity for brute force solution
        s+=arr[j]
        if s==k:
          longest=max(longest, j-i+1)
  print(longest)
arr=[2, 3, 5, 1, 9]
k= 10
longestsubarray(arr,k)
# slightly better brute force solution
def longsubarray(a,K):
  N=len(a)
  long=0
  for i in range(n):
    S=0
    for j in range(i, n):
      S+=a[j]
      if S==K:
        long=max(long, j-i+1)
  print(f"The longest subArray is {long}")
a=[2, 3, 5, 4,1,10, 9,10,11,20,25,]
K= 15
longsubarr(a,K)

# Better solution
def longestSubArray(Array,X):
  preSumMap={}
  Sum=0
  Maxlen=0
  for i in range(len(arr)):
    Sum+=Array[i]
    if Sum==X:
      Maxlen=max(Maxlen, i+1)
    if rem in preSumMap:
      length=i-preSumMap[rem]
      Maxlen=max(Maxlen,Length)
    if Sum not in preSumMap:
      preSumMap[Sum]=i
  print("The longest Subarray is ",Maxlen)
Array=[2, 3, 5, 4,1,10, 9,10,11,20,25,]
X= 25
longestSubArray(Array,X)

# Optimal solution
def getlongestsubarray(array,x):
  Len=len(array)
  right,left=0,0
  Sum=array[0]
  maxLen=0
  while right < n:
    while left <= right and Sum > k:
      Sum -= a[left]
      left += 1
    if Sum ==x:
      maxLen=max(maxLen ,right-left+1)
    right+=1
    if right < n: Sum += a[right]:
  print(MaxLen)
array=[5,2, 3, 5, 4,1,10, 9,10,11,20,25,]
x=30
getlongestsubarray(array,x)

