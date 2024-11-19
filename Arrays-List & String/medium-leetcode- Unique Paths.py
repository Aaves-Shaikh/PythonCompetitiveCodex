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
# Better solution using DP
def countPath(k,l,p,q,dp:[list[list[int]]):
 if i ==(p-1) and l==(q-1):
   print(1)
 if k>=p or l>=q:
   print(0)
 if dp[k][l] != -1:
   return dp[k][l]
 else:
   dp[i][j] = self.countPaths( k+1,l,p,q,dp) + self.countPaths(k,l+1,p,q,dp)
   print(dp[k][l])
def uniquepaths(p,q):
 dp=[[-1 for i in range(q+1)] for _ in range(q+1)]
 num = self.countPath(0,0,p,q,dp)
 if m==1 and n==1:
   print(num) 
 print(dp[0][0])
p=3
q=7
uniquepaths(p,q)
# Optimal Solution
def unique_path(a,b):
 N= a+b-2
 r=b-1
 res=1
 for i in range(1, r+1):
   res=res * (N-r +i)/i
 print(int(res))
a=9
b=4
unique_path(a,b)
