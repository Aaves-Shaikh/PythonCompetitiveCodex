# Missing Element in Array 
# Link to the problem https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1
# Given an array, arr. The task is to find the largest element in it.
# Date: 02/10/2024
# The Problem Consist of two solution. A better Solution and A optimal Solution. 
# the Better Soln
def missingNumber(n,arr): #better soln 
    num_set=set(arr)
    for i in range(1, n+1):
        if i not in num_set:
            print(i)
n=int(input())
arr=list(map(int,input().split()))
missingNumber(n,arr)

# optimal soln 
def missingNumberOpt(n1,arr1): 
    num_set=sum(arr1)
    s2=n1*(n1+1)//2
    print(abs(num_set-s1))
n1=int(input())
arr1=list(map(int,input().split()))
missingNumberOpt(n1,arr1)
