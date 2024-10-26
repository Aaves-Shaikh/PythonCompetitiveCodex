# Sort 0s, 1s and 2s
# Given an array. The task is to sort the array in Sort 0s, 1s and 2s.
# Date: 26/10/2024
# the probelm link : https://www.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1 
# The Problem Consist of two solution. A brute force Solution, and a optimal Solution. 
# Metod1:
def sortArray(arr):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    for num in arr:
        if num == 0:
            cnt0 += 1
        elif num == 1:
            cnt1 += 1
        else:
            cnt2 += 1
    for i in range(cnt0):
        arr[i] = 0
    for i in range(cnt0, cnt0 + cnt1):
        arr[i] = 1
    for i in range(cnt0 + cnt1, len(arr)):
        arr[i] = 2
n = 6
arr = [0, 2, 1, 2, 0, 1]
sortArray(arr)
print("After sorting:")
for num in arr:
    print(num, end=" ")
print()
