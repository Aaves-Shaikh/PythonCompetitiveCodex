# Search a 2D Matrix
# Link to the problem https://leetcode.com/problems/search-a-2d-matrix/description/
# Given an array, arr. The task is to find if the target element if present in a 2d matrix 
# Date: 08/10/2024
# The Problem Consist of three solution. Brute force solution, better Solution, and A optimal Solution. 
# Method 1 the  Brute Force Method 
def searchmatrix(matrix,target):
    a=len(matrix)
    b=len(matrix[0])
    for i in range(a):
        for j in range(b):
            if matrix[i][j]==target:
                print("Traget found ")
                return
    print("Target not found!!! ")
    
matrix= [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target= 60
searchmatrix(matrix,target)
