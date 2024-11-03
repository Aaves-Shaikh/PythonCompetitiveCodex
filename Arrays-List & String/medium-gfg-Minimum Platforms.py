# Minimum Platforms
# Link to the problem https://www.geeksforgeeks.org/problems/minimum-platforms-1587115620/1 
# Given arrival and departure times of all trains that reach a railway station. Find the minimum number of platforms required for the railway station so that no train is kept waiting
# Date: 03/11/2024
# 
# Method 1 the  Brute Force Method 
def minimumPlatform(arr,dep):
    arr.sort()
    dep.sort()
    platforms_needed=0
    max_platforms=0
    i=0
    j=0
    while i<len(arr) and j <len(dep):
        if arr[i]<=dep[j]:
            platforms_needed+=1
            i+=1
        else:
            platforms_needed-=1
            j+=1
        max_platforms = max(max_platforms,platforms_needed)
    print(max_platforms)
arr=[0900, 0940, 0950, 1100, 1500, 1800]
dep=[0910, 1200, 1120, 1130, 1900, 2000]
minimumPlatform(arr,dep)
