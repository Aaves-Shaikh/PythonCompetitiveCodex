# Second Largest Element in Array 
# Link to the problem https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/1 
# Given an array, arr. The task is to find the largest element in it.
# Date: 04/10/2024
# The Problem Consist of only the optimal Solution. But will add the brute force method and a better solution shortly 

# Note use formula d=d%n to find out how many rotation needs to be done 
def leftrotate(arr,d):
    n=len(arr)
    d=d%n
    for i in range (d):
        temp=arr[0]
        for j in range(len(arr)-1):
            arr[j]=arr[j+1]
        arr[-1]=temp
    print(arr)
arr=[1,2,3,4,5,6,7]
d=5
leftrotate(arr,d)
