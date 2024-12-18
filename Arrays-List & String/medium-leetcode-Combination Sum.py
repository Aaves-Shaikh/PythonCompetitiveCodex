# Combination Sum
# problem link:
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.
# Date 18/12/2024
# Method 1 using recursion
def combinationsum(candidate, target):
    ans=[]
    ds=[]
    def findcombination(index, target):
        if index=len(candidate):
            if target==0:
                ans.append(ds[:])
            return
            if candidate[index]<=target:
                ds.append(candidate[index])
                findcombination(index, target-candiates[index])
                ds.pop()
            findcombination(index+1, target)
        findcombination(0, target)
        print("All the possible sums equal to target are: ",ans)
 candidate = [2,3,6,7]
 target = 7
 combinationsum(candidate, target)
