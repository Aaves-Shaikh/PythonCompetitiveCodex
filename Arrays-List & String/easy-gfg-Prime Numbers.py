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
Method 2: 
def is_prime(N):
    if N<=1:
        print("Not a prime nunber: ")
    for i in range(2,int(N**0.5)+1): #this is a better soln, than above as the loop will only traverse till the square root of the number i.e from 2 to 5 only if n is not divisible the loop breaks, here the number of iterations of n has reduce Significantly saving the time complexity
        if N%i==0:
            print("This is a prime number: ")
            break
        else:
            print("This is a not prime number: ")
            break
n=29
is_prime(n)
