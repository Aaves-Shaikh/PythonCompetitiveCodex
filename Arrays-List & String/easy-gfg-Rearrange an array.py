# Second Largest Element in Array 
# Given an array, Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’.
# Date: 16/10/2024
# The Problem Consist of Two solution. A brute force Solution, and a optimal Solution. 
# Metod1:
def zigZag(arr, n):
    arr.sort()
    for i in range(1, n-1, 2):
        arr[i], arr[i+1] = arr[i+1], arr[i]
    print(arr)
if __name__ == "__main__":
    arr = [4, 3, 7, 8, 6, 2, 1]
    n = len(arr)
    zigZag(arr, n)
