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

# Better Solution
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


# Optimal Solution 1:
def product_except_self(arr):
    n = len(arr)
    left_arr = [1] * n
    right_arr = [1] * n

    # Calculate left products
    left_mul = 1
    for i in range(n):
        left_arr[i] = left_mul
        left_mul *= arr[i]

    # Calculate right products
    right_mul = 1
    for j in range(n - 1, -1, -1):
        right_arr[j] = right_mul
        right_mul *= arr[j]

    # Calculate the result by multiplying left and right products
    result = [l * r for l, r in zip(left_arr, right_arr)]
    return result

# Example usage
arr = [1, 2, 3, 4]
print(product_except_self(arr))  # Output: [24, 12, 8, 6]

# Optimal Solution 2
def productOfArray(arr):
    Len = len(arr)
    left_arr = [1]* Len
    right_arr = [1]* Len
    left_mul = 1
    right_mul = 1
    for i in range(Len):
        j = -i -1
        left_arr[i] = left_mul
        right_arr[j] = right_mul
        left_mul *= arr[i]
        right_mul *= arr[j]
    return[l,r for l,r in zip(left_arr, right_arr)]
arr=[5 ,3,2,1,6]
res = productOfArray(arr)
print("The final product array is:", res)
    
