# Overlapping-intervals
# Link to the problem https://www.geeksforgeeks.org/problems/overlapping-intervals--170633/1
# Given an array. The task is to merge all of the overlapping Intervals.
# Date: 11/11/2024
# The Problem Consist of two Brute force solution and optimal solution 
# Method 1 the  Brute Force Method 
def mergeoverlap(arr):
    n=len(arr)
    arr.sort()
    ans=[]
    for i in range(n):
        start,end=arr[i][0],arr[i][1]
        if ans and end<=ans[-1][1]:
            continue
        for j in range(i+1,n):
            if arr[j][0]<=end:
                end = max(end,arr[j][1])
            else:
                break
        ans.append([start,end])
    print(ans)
arr=[[1, 3], [8, 10], [2, 6], [15, 18]]
mergeoverlap(arr)

# Method 2 The Optimal Solution
def mergeOverLap(array):
    answer=[]
    array.sort()
    l=len(array)
    for i in range(l):
        if not answer or array[i][0]>answer[-1][1]:
            answer.append(array[i])
        else:
            answer[-1][1]=max(answer[-1][1],array[i][1])
    print(answer)
array=[[1, 3], [8, 10], [2, 6], [15, 18],[20,26]]
mergeOverLap(array)
