# Union in the array
# Given an two array A and B. The task is to find the union of those elements.
# Date: 02/11/2024
# The Problem Consist of Two solution. A brute force Solution, and a optimal Solution. 
# Metod1: 
 def union(A,B):
    union=[]
    for i in A+B:
        if i not in union:
            union.append(i)
            union.sort()
    print(f"The union elements in array A and B are {union}")
A=[4, 5, 6, 5, 7, 5, 2, 1, 65, 3, 22 ]
B=[1,2,3,4,5,6,7,8,9]
union(A,B)

# Method 2 optimal solution
def union1(C,D):
    union1=list(set(C) | set(B))
    union1.sort(reverse=True)
    print(f"The union elements in array A and B are {union1}")
C=[4, 5, 6, 5, 7, 5, 2, 1, 65, 3, 22 ]
D=[1,2,3,4,5,6,7,8,9]
union1(C,D)
