# K-th element of two Arrays
# Link of the problem https://www.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
# Given two sorted arrays a[] and b[] and an element k, the task is to find the element that would be at the kth position of the combined sorted array. 
# Date 16/12/2024
# Method1 using Merge Sort
def kthElement(a, b, k):
  n,m =len(a),len(b)
  i=j=count=0
  while i<n and j<m:
    if a[i]<b[j]:
      count+=1
      if count==k:
        return a[i]
        i+=1
      else:
        count +=1
        if count ==k:
          return b[j]
          j+=1
   while i <n:
    count +=1
    if count ==k:
      return a[i]
      i+=1
   while j<m:
     count +=1
     if count == k:
       return b[j]
       j+=1     
   return -1 #if the K is not there
a= [2, 3, 6, 7, 9]
b= [1, 4, 8, 10]
k = 5
kthElement(a,b,k)

# Method 2
def kth_element(arr1, arr2, X):
  c = a+b
  c = sorted(c)
  # print(c)
  return c[k-1]
arr1== [100, 112, 256, 349, 770]
arr2= [72, 86, 113, 119, 265, 445, 892] 
X = 7
kth_element(arr1, arr2, X)
