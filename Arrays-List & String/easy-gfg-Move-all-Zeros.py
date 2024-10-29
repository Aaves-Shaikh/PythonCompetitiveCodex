# Move All Zeroes to End
# Given an array. task is to move all the zeros to the end :
# Date: 17/10/2024
# The Problem https https://www.geeksforgeeks.org/problems/move-all-zeroes-to-end-of-array0751/1
# Metod1: 
def zero_at_end(arr):
    count=0
    n=len(arr)
    for i in range(n):
        if arr[i]!=0:
            arr[count]=arr[i]
            count+=1
    while count<n:
        arr[count]=0
        count+=1
    print(arr)
arr=[1,2,3,0,4,5,0,0,0,6,0,7,0,9,0]
zero_at_end(arr)
