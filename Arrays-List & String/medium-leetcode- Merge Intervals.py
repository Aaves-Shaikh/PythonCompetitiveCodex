# Merge intervals 
# Link to the problem :https://leetcode.com/problems/merge-intervals/
# Given an space seprated string. cound the words in a comma seprated way
# Date: 18/10/2024
# The Problem Consist on one solution as of now . 
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
