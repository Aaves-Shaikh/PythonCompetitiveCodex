# Second Largest Element in Array 
# Link to the problem https://www.geeksforgeeks.org/problems/second-largest3735/1 
# Given an array, arr. The task is to find the largest element in it.
# Date: 03/10/2024
# The Problem Consist of three solution. A brute force Solution, A better Solution, and A optimal Solution. 

# Method 1: This approach uses brute force to check each element by performing reverse indexing on the array and returning the second largest element once found.
# ==================== better Solution ==================== 
# def secondLargest(arr):
#     arr.sort()
#     if arr[-1]!=arr[-2]:
#         print("The second largest element is: ",arr[-2])
#     else:
#         for i in range(-2,-len(arr),-1):
#             if arr[-i]<arr[-1] :
#                 print("The second largest element is: ",arr[-i], "Found at the index",i)
#                 break
#         else:
#             print("All the elemts are same")
    
# arr=[1, 8, 7, 56, 90,90,56]
# secondLargest(arr)

# Method 2: This is an improved method where I reverse the sorted array and return the second largest element found.
# ==================== better Solution ====================
def second_largest(arr):
    arr.sort(reverse=True)
    for i in range(1,len(arr)):
        if arr[i]<arr[0]:
            print("The second largest element is: ",arr[i],"found at index: ",arr.index(arr[i]))
            break
    else:
        print("All the elements are same")
arr=[1, 8, 7, 56, 90,90,56]
second_largest(arr)
# Method 3:This is the most effective approach, utilizing a data type known as 'set' to identify unique elements, after which we return the element at index -2 from the array or list.
# ==================== Optimal Solution ====================
def secondLargest_arr(arr1):
    secondLargest=set(arr1)
    if len(secondLargest)>2:
        print(sorted(secondLargest)[-2])
    else:
        print("please enter more than two values")
arr1=[1, 8, 7, 56, 90]
secondLargest_arr(arr1)
