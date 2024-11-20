# Summary Ranges
# Link https://leetcode.com/problems/summary-ranges/description/
# for the given array, Return the smallest sorted list of ranges that cover all the numbers in the array exactly. 
# That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
# Date 20/11/2024
# For the problem we have one solution.
def summaryRanges( nums): 
  ranges = [[-inf, -inf]]
  for x in nums:
    if x == ranges[-1][1] + 1: ranges[-1][1] = x
    else: ranges.append([x, x])
  print([f'{a}' if a == b else f'{a}->{b}' for a, b in islice(ranges, 1, None)])
  nums=[0,1,2,4,5,7]
  summaryRanges(nums)
