# Minimum Jumps
# Description: You are given an array arr[] of non-negative numbers. Each number tells you the maximum number of steps you can jump forward from that position.
# Date: 22/01/2025
# Method 1 using greedy algo

def minijumps(arr):
  if not arr:
    print("There are no elements in the array so the minimun jumps will be 0. ")
  if len(arr)==1:
    print("There is only 1 elements in the array so the minimun jumps will be 0. ")
  curr_jumps,   min_jumps, jump_cnt = 0,0,0
  for i in range(len(arr)-1):
    min_jumps = max(min_jumps, i + arr[i])
    if curr_jumps == i:
      if min_jumps == i:
        print(-1)
    else:
      jump_cnt += 1
      curr_jumps = min_jumps
  print("The minimum number of jumps needed to move from the first position in the array to the last position is: " jumps_cnt)
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
minijumps(arr) #output = 3
