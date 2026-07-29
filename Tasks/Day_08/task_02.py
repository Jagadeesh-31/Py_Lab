# 2. Sum of numbers

def sum_of_n(n):
    if n < 0:
        return "Sum of n Nums is Not Possible"
    elif n ==0 or n== 1:
        return 1
    else:
        return n + sum_of_n(n-1)
n = int(input())
print(sum_of_n(n))

          
