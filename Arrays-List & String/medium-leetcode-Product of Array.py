# Product of Array Except Self
# problem link https://leetcode.com/problems/product-of-array-except-self/description/
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# Date 13/12/2024
# method 1 Brute force using two pointers 'i' , 'j'
def product_arr(nums):
    answer=[]
    for i in range(len(nums)):
        prod=1
        for j in range(len(nums)):
            if i!=j:
                prod*=nums[j]
        answer.append(prod)
    print("the final product of array is: ",answer)
nums=[1,2,3,4]
product_arr(nums)

# Optimal Solution
def productArray(arr):
    n = len(arr)
    if n == 0:
        return []

    # Initialize left and right product arrays
    left_arr = [1] * n
    right_arr = [1] * n

    # Calculate left products
    left_mul = 1
    for i in range(n):
        left_arr[i] = left_mul
        left_mul *= arr[i]

    # Calculate right products
    right_mul = 1
    for i in range(n - 1, -1, -1):
        right_arr[i] = right_mul
        right_mul *= arr[i]

    # Calculate the final product array
    return [l * r for l, r in zip(left_arr, right_arr)]

# Example usage
arr = [5, 6, 7, 9]
result = productArray(arr)
print("The final product array is:", result)
