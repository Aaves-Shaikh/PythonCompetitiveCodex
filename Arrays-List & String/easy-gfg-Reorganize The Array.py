# Reorganize The Array
# Link to the problem https://www.geeksforgeeks.org/problems/reorganize-the-array4810/1
# Given an array, with indices ranging from 0 to arr.size() - 1, your task is to write a program that rearranges the elements of the array such that arr[i] = i. 
# If an element i is not present in the array, -1 should be placed at the corresponding index.
# Date: 27/11/2024
# The Problem Consist of two solutions. A brute force Solution, and A optimal Solution. 
def rearrange(a):
    for i in range(len(a)):
        while a[i] != i and a[i] != -1:
          tmp = a[a[i]]
          a[a[i]] = a[i]
          a[i] = tmp
        print(a)
arr=[8, -8, 9, -9, 10, -11, 12]
rearrange(arr)
