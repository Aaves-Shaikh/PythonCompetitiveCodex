# Strings Rotations
# Link to the problem https://www.geeksforgeeks.org/problems/check-if-strings-are-rotations-of-each-other-or-not-1587115620/1 
# Given an string. The task is to check if s2 is a rotated version of the string s1.
# Date: 25/10/2024
# The Problem Consist of two solutions. A brute force Solution, and A optimal Solution. 
# ====================  Optimal Solution ====================
 def areRotations(s1,s2):
    a1=s1+s2
    if s2 in a1:
        print("yes")
    else:
        print("No")
s1="geeksforgeeks"
s2="skeegrofskeeg"
areRotations(s1,s2)
