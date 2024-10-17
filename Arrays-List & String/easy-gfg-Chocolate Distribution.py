# Chocolate Distribution Problem
# Given an array. task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet. 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.
# Date: 17/10/2024
# The Problem https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1
# Metod1: using the for loop we check if the element is present in the list is yes to print it
def min_diff(A,N,M): #easy level
    if (N==0 or M==0):
        print(0)
    if M>N:
        print(-1)
    A.sort() #sort the list/array
    min_d = A[N-1]-A[0] 
    for i in range(len(A)-M+1): #take on the 
        min_d=min(min_d,A[i+M-1]-A[i])
    print(min_d)
N=int(input())
A=list(map(int,input().split()))
M=int(input())
min_diff(A,N,M)
