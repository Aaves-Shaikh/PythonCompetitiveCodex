 Second Largest Element in Array 
# Given an array. The task is to Return the modified array in such a way that if the current and next numbers are valid numbers and are equal then double the current number value and replace the next number with 0.
# Date: 03/10/2024
# Problem Link: https://www.geeksforgeeks.org/problems/ease-the-array0633/1
# The Problem Consist of One solution. A brute force Solution
# Metod1:
def modifyAndRearrangeArr (arr) : 
        #Complete the function
        n=len(arr)
        for i in range(n-1):
            if arr[i]!=0 and arr[i]==arr[i+1]:
                arr[i]=2*arr[i]
                arr[i+1]=0
        ans=[num for num in arr if num !=0]
        s=len(ans)
        for i in range(s,n):
            ans.append(0)
        print(ans)
  arr=[2, 2, 0, 4, 0, 8]
modifyAndRearrange(arr)
