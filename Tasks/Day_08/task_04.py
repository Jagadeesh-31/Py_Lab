# fibonacci

def fib(n):
    if n < 0:
        return "Enter a +ve for fibonacci"
    elif n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))
for i in range(n):
    print(i,end=" ")
