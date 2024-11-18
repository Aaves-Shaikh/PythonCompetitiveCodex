# Merge Without Extra Space
# Problem link: https://www.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1
# Given two sorted arrays a[] and b[] in non-decreasing order. Merge them in sorted order without using any extra space. Modify a so that it contains the first n elements and modify b so that it contains the last m elements.
# Date: 18/11/2024
# for this problem we have three solution one brute force solution and two optimal solution[two pointer approach] [gap method]
def merge(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    arr3=[0]*(n+m)
    left = 0
    right = 0
    index = 0 
    while left < n and right < m:
        if arr1[left] <=arr2[right]:
            arr3[index]=arr1[left]
            left+=1
            index+=1
        else:
            arr3[index]=arr2[right]
            right+=1
            index+=1
    while left < n:
        arr3[index] = arr1[left]
        left +=1
        index +=1
    while right < m:
        arr3[index] = arr2[right]
        right +=1
        index +=1
    for i in range(n+m):
        if i <n:
            arr1[i]=arr3[i]
        else:
            arr2[i-n]=arr3[i]
    print(arr1)
    print(arr2)
arr1=[1, 5, 9, 10, 15, 20]
arr2=[2, 3, 6, 7, 8, 13]
merge(arr1,arr2)
