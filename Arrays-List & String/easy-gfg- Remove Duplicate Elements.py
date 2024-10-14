# Second Largest Element in Array 
# Given an array, arr. The task is to find the duplicate elements in array if present and remove them.
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
# ==================== Optimal Solution ====================
def isduplicate(arr):
    if len(arr)!=len(set(arr)):
        new_arr=list(set(arr))
        new_arr.sort()
        print("The unique array is ",new_arr)
arr=[1,1, 8, 7, 9,56, 90,99,99,99]
isduplicate(arr)
