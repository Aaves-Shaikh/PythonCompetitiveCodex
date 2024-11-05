# Parenthesis Checker
# Link to the problem :  https://www.geeksforgeeks.org/problems/parenthesis-checker2744/0
# 
# Date: 05/11/2024
# The Problem Consist on one solution as of now . 
# ==================== Otimal Solution ====================
def ispar(x):
        stack=[]
        for char in x:
            if char in ["{","(","["]:
                stack.append(char)
            else:
                if not stack :
                    print(False)
                if stack and ((stack[-1]=='(' and char==')')or
                             (stack[-1]=="{" and char=="}")or
                             (stack[-1]=="[" and char=="]")):
                    stack.pop()
                else:
                    print(False)
        if stack:
            print(False)
        print(True)

x="{([])}"
ispar(x)
