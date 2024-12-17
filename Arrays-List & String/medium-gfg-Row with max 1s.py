# Row with max 1s
# Problem Link: https://www.geeksforgeeks.org/problems/row-with-max-1s0023/1
# You are given a 2D binary array arr[][] consisting of only 1s and 0s. Each row of the array is sorted in non-decreasing order.
# Your task is to find and return the index of the first row that contains the maximum number of 1s. If no such row exists, return -1.
# Date: 17/122/2024
# method 1
def rowWithMax1s(arr):
  n = len(arr)
  m = len(arr[0])
  max_rows_index = -1
  max_ones = 0
  j = m-1
  for i in range(n):
    while j >=0 and arr[i][j] ==1:
      j-=1
      nums_ones = m-(j+1)
      if nums_ones>max_ones:
          max_ones = nums_ones
          max_row_index = i
    print("The maximum row's with 1 is: ",max_row_index)
arr=[[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
rowWithMax1s(arr)

# Method2 Better solution
def row_with_max1s(nums):
  n = len(nums)
  max_row = -1
  max_count = 0
  for number in range(n):
    count=arr[number].count(1)
    if count>max_count:
      max_count=count
      max_row = number
  print("The row number with max 1's is: ",max_row)
nums=[[0,0], [1,1]]
row_with_max1s(nums)
