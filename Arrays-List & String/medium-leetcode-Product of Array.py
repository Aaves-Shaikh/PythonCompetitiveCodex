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
      
