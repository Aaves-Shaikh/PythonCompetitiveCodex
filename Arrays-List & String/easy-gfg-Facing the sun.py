# Facing the sun
# Link to the problem = https://www.geeksforgeeks.org/problems/facing-the-sun2126/1 
# Given an array, arr. find the maximun number of building that are facing the sun. for more info check the question on gfg
# Date: 11/10/2024
# The Problem Consist of one easy solutions.
# ==================== Brute force Solution ====================
 def height(arr):
    count=1
    curheight=arr[0]
    if len(arr)==1:
        return count
    else:
        for i in range(1,len(arr)):
            if curheight<arr[i]:
                curheight=arr[i]
                count+=1
    print(count)
arr=list(map(int,input().split()))
height(arr)
