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
# ==================== Better Solution ====================
def binarySearch(nums,tar):
    n=len(nums)
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==tar:
            return True
        elif nums[mid]<tar:
            low=mid+1
        else:
            high=mid-1
    return False
def searchMatrix(mat,tar):
    n=len(mat)
    m=len(mat[0])
    for i in range(len(mat)):
        if mat[i][0]<= tar <= mat[i][m-1]:
            return binarySearch(mat[i],tar)
    return False
mat=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
tar= 1
result=searchMatrix(mat,tar)
print("Element found!!! " if result else "Element not found")

# ==================== Better Solution ====================
def search_matrix(M,T):
    p=len(M)
    q=len(M[0])
    low,high=0,p*q-1
    while low<=high:
        mid=(low+high)//2
        row=mid//q
        col=mid%q
        if M[row][col]==T:
            return True
        elif M[row][col]<T:
            low =mid+1
        else:
            high=mid-1
    return False
M=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
T=16
result=search_matrix(M,T)
print("Element found!!! " if result else "Element not found")
