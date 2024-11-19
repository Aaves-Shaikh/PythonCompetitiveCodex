 # Unique Paths
# link to the problem https://leetcode.com/problems/unique-paths/description/
# Given a matrix m X n, count paths from left-top to the right bottom of a matrix with the constraints that from each cell you can either only move to the rightward direction or the downward direction.
# Date 11/19/20
# This problem have three solutions brute force, better solution and optimal solution
# Brute force method
def uniquepath(m,n):
  def countPaths(i,j,n,m)
    if i==(n-1) and j ==(m-1):
      return 1
    if i >= n or j >=m:
      return 0
    else:
      print(countPaths(i+1,j,n,m)+ countPaths(i,j+1,n,m))
  print(countPaths(0,0,m,n))
m=3
n=7
uniquepath(m,n)
