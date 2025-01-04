# Count all triplets with given sum
# problem link: https://www.geeksforgeeks.org/problems/count-all-triplets-with-given-sum-in-sorted-array/1
# Given a sorted array arr[] and a target value, the task is to count triplets (i, j, k) of valid indices, such that arr[i] + arr[j] + arr[k] = target and i < j < k
# Date: 04/01/2025
# Method 1 Brute force method: 
def countTriplets(arr, target):
  c=0
  # n = len(arr)
  for i in range(len(arr)-2):
    j =  i+1
    k = len(arr)-1
    while j<k:
      if arr[j] + arr[k] == target- arr[i]:
        c +=1
        temp = j+1
        while temp<k and arr[temp] == arr[temp-1] :
          c += 1
          temp += 1
          k -= 1
      elif arr[j] + arr[k] < target-arr[i]:
        j+=1
      else:
          k -= 1
   print("There are total ", c ,"values of i j and k that equal to sum")
arr=  [-3, -1, -1, 0, 1, 2]
target=  -2
countTriplets(arr, target)

# Better solution: 
 def counttriplets(array, tar):
   sm1={}
   sm2={}
   ret=0
   for ve in array:
      ret+=sm2.get(tar-ve,0)
      for v in sm1:
          sm2[v+ve]=sm2.get(v+ve,0)+sm1.get(v,0)
          sm1[ve]=sm1.get(ve,0)+1
  print("There are total ", ret,"values of i j and k that equal to sum")
array= [-2, 0, 1, 1, 5]
tar = 1
counttriplets(array, tar)
