# Merge intervals 
# Link to the problem :https://leetcode.com/problems/merge-intervals/
# Given an space seprated string. cound the words in a comma seprated way
# Date: 18/10/2024
# The Problem Consist on one solution as of now . 
# The brute force solution for the problem is: 
def mergeintervals(arr):
  arr.sort()
  ans=[]
  for i in range(len(arr)):
    start,end=arr[i][0], arr[i][1]
    if ans and end <= ans[-1][1]:
      continue
    for j in range(i+1 , n):
      if arr[j][0] <=end:
        end= max(end, arr[j][1])
      else:
        break
     ans.append([start,end])
  print(ans)
arr=[[1,4],[4,5]]
mergeintervals(arr)
        
# Optimal solution
def merge(intervals):
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for interval in intervals:
            if merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])
intervals=[[1,3],[2,6],[8,10],[15,18]]
merge(intervals)
