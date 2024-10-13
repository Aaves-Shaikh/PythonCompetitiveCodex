# Largest word in a string.
# Given an string. The task is to find the largest word in it.
# Date: 13/10/2024
# The Problem Consist of two solution. A better Solution and A optimal Solution. 
# Method 1 the better Soln using Brute Force Method
def longest(word_list):
    longest_word =""
    longest_length = 0
    for word in word_list:
        if len(word) > longest_length:
            longest_length = len(word)
            longest_word = word
    print( longest_word , longest_length)
n = int(input("how many words you want to enter "))
word_list=[]
for i in range(n):
    word= input("enter a word: ")
    word_list.append(word)
longest_word, longest_length = longest(word_list)
print("The longest word is ", longest_word)
print("The length of the longest word is: ",longest_length)
# out in alphabetical order
str = (input("Enter the strings "))
words = [word for word in str.split(",")]
print(" , ".join(sorted(list(set(words)))))
