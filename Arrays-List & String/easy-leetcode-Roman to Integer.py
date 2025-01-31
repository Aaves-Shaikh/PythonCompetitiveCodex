# Roman to Integer
# problem Link: https://leetcode.com/problems/roman-to-integer/
# Description: The Task is Given a roman numeral, convert it to an integer.
# date: 31/01/2025
# This is a easy problem and have only one solution
def romanToInt(s):
        trans = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        number = 0
        s= s.replace("IV" , "IIII").replace("IX", "VIIII")
        s= s.replace("XL" , "XXXX").replace("XC", "LXXXX")
        s= s.replace("CD" , "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += trans[char]
        print("The integer of the given number is: ", number)
s = "III" 
romainToInt(s)
