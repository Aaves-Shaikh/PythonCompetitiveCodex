# Second Largest Element in Array 
# Given an array. The task is to find the duplicate elements in array if present and remove them.
# Date: 03/10/2024
# The Problem Consist of Two solution. A brute force Solution, and a optimal Solution. 
# Metod1: using the for loop we check if the element is present in the list if no we append it else we move forward
def is_duplicate(arr1):
    unique_element=[]
    for i in (arr1):
        if i not in unique_element:
            unique_element.append(i)
    print("The unique array is: ",unique_element)
arr1=[1,1, 8, 7, 9,56, 90,99,99,99]
is_duplicate(arr1)

# Method 2: In this method we simply use set function to check if there are any duplicate values. 
#  ==================== Better Solution ====================
# A solution withouy using an hashmap
def removeDuplicates(self, arr):
    arr.sort()
    unique_index = 0
    for i in range(1, len(arr)):
        if arr[i] != arr[unique_index]:
            unique_index += 1
            arr[unique_index] = arr[i]
    print("The arrary containing only unique element is: ", unique_index + 1)
arr = [2, 2, 2, 2, 2]
removeDuplicates(arr)
# ==================== Optimal Solution ====================
def isduplicate(arr):
    if len(arr)!=len(set(arr)):
        new_arr=list(set(arr))
        new_arr.sort()
        print("The unique array is ",new_arr)
arr=[1,1, 8, 7, 9,56, 90,99,99,99]
isduplicate(arr)
