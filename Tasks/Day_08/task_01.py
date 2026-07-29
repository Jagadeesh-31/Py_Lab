# 1. Recursion logic for factorial

def fact(n):
    if n < 0:
          return("Enter a +ve for factorial")
    elif n == 0 or n ==1:
        return 1
    else:
        return n * fact(n-1)
n = int(input())
print(fact(n))




