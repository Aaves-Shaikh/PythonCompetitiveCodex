#  subsequence with sum K
# Link to the problem https://www.geeksforgeeks.org/problems/check-if-there-exists-a-subsequence-with-sum-k/1
# Given an array arr and target sum k, check whether there exists a subsequence such that the sum of all elements in the subsequence equals the given target sum(k).
# Date: 9/11/2024
# The Problem Consist of three  Solution.
# Method 1 Brute Force
def maxsubarray_sum(arr):
    maxi= -sys.maxsize -1
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            sum=0
            for k in range(i,j+1):
                sum+= arr[k]
            maxi=max(maxi,sum)
            if maxi<0:
                maxi=0
    print(maxi)
arr=[-2,-1,-3,-1,-5,-4] 
maxsubarray_sum(arr)  
