# Prime Number
# For a given number n check if it is prime or not. A prime number is a number which is only
# Date: 30/10/2024
# The Problem https://www.geeksforgeeks.org/problems/prime-number2314/1
# Metod1:
def isprime(n):
    if n<=1:
        print("No")
    fo/r i in range(2,n): #now this is a very basic soln to a basic prb as i will traverse from 2 to the number n, if the n is a large number and then and not a prime then the time complexity will increase. for this below is the optimal soln.
        /if n%i==0:
            print("Yes, This is a prime number!!! ")
            break
        else:
            print("No this is not a prime number!!! ")
            break
n=29
isprime(n)
