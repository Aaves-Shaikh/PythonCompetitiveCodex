# Rotate the array in the anti-clockwise direction
# Link to the https://www.geeksforgeeks.org/problems/rotate-a-2d-array-without-using-extra-space1004/1 
# Given an array. The task is to rotate the array by 90 degrees in an anticlockwise direction.
# Date: 15/10/2024
# The Problem Consist of two solutions. Brute force solution,and a optimal Solution. 
# ==================== Brute force Solution ====================
from typing import List
def rotateMatrix(mat):
    n=int(len(mat)**0.5)
    rotated=[]
    rotated = [[0 for _ in range(n)] for _ in range(n)] #adds xero to all the values of the matrix
    for i in range(n):
        for j in range(n):
            rotated[j][n-i-1]=mat[j*n+i] #here we rotate the array
    print(rotated ,end=" ")
mat=[[7, 4, 1], 
     [8, 5, 2],
     [9, 6, 3]]
rotateMatrix(mat)

# ==================== Optimal Solution ====================
def rotate_Matrix(Matrix):
    n=len(Matrix)
    for i in range(n):
        for j in range(i):
            Matrix[i][j],Matrix[j][i]=Matrix[j][i],Matrix[i][j]
    Matrix.reverse()
    for row in Matrix:
        print(row)
if __name__ == "__main__":
    Matrix=[[7, 4, 1], 
        [8, 5, 2],
        [9, 6, 3]]
    rotate_Matrix(Matrix)   
    
