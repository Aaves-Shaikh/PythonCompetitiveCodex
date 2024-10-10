# Reverse Words 
# Link to the problem : https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/1 
# Given an space seprated string. cound the words in a comma seprated way
# Date: 09/10/2024
# The Problem Consist on one solution as of now . 
# ==================== Otimal Solution ====================
def reverse_words(str):
  words=str.split(".")
  words=[::-1]
  reverse_str=".".join(words)
  print(reverse_str)
str= "Solving a problem every day increases your coding skills"
reverse_words(str)
