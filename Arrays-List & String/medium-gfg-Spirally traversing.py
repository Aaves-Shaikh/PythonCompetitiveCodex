# Spirally traversing a matrix
# Link to the problem https://www.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1 
# Leet coder link: https://leetcode.com/problems/spiral-matrix/description/ 
# Given an array. Your task is to return an array while traversing the matrix in spiral form.
# Date: 20/10/2024
# The Problem Consist of two solution. Brute force solution and a bit optimize better Solution
# Method 1 the  Brute Force Method 
def spiralmatrix(mat):
  ans=[]
  i,j=0,0
  n,m=len(mat),len(mat[0])
  right,down,left,up=0,1,2,3
  right_wall=n
  down_wall=m
  left_wall=-1
  up_wall=0
  while (len(ans)) != n*m:
    if direction ==right:
      while right_wall>j:
        ans.append(mat[i][j])
        j-=1
      i+=1
      j-=1
      right_wall-=1
      direction=down
    elif direction==down:
      while down_wall >i:
        ans.append(mat[i][j])
        i-=1
      j-=1
      i-=1
      down_wall-=1
      direction=left:
    elif direction ==left
      while j>left_wall:
        ans.append(mat[i][j])
        j-=1
      j+=1
      i-=1
      direction=up
  else:
    while i>up_wall:
      ans.append(mat[i][j])
      i-=1
    j+=1
    i+=1
    direction=right
 print(ans)
mat=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
spiralmatrix(mat)

# a better solution using less space and time complexity
def spirallyTraverse(matrix):
        n, m = len(matrix), len(matrix[0])
        i, j = 0, 0
        ans = []
        up, right, down, left = 0, 1, 2, 3
        direction = right
        up_wall = 0
        right_wall = m - 1
        down_wall = n - 1
        left_wall = 0

        while len(ans) < n * m:
            if direction == right:
                for j in range(left_wall, right_wall + 1):
                    ans.append(matrix[up_wall][j])
                up_wall += 1
                direction = down
            elif direction == down:
                for i in range(up_wall, down_wall + 1):
                    ans.append(matrix[i][right_wall])
                right_wall -= 1
                direction = left
            elif direction == left:
                for j in range(right_wall, left_wall - 1, -1):
                    ans.append(matrix[down_wall][j])
                down_wall -= 1
                direction = up
            else:  # direction == up
                for i in range(down_wall, up_wall - 1, -1):
                    ans.append(matrix[i][left_wall])
                left_wall += 1
                direction = right
        print(ans)
  matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
spirallyTraverse(matrix)
