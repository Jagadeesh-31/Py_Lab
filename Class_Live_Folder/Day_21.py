# Recursive Functionals, Anonymous Functions
'''
def test():
    """With out Base Case"""
    return test()
print(test())
'''

# factorial  5!=(5*(5-1)*(5-2)*(5-3)*(5-4)) -> 120 
'''
def factorial(n):
    """Recursive Apporach"""
    if n < 0:
        return "Enter a +ve Number"
    elif n==0 or n==1:
        return 1
        
    else:
        return n*factorial(n-1)
n = int(input())
print(factorial(n))
'''


# sum of n  natural numbers

'''
def sum_nn(n):
    if n <0:
        return "Enter a +ve Number"
    elif n==0:
        return 0
    else:
        return n + sum_nn(n-1)
n = int(input())
print(sum_nn(n))

'''
'''
# area  of rectangle
def area_of_rec(l,b):
    if l < 0 or b <0:
        return "Enter a +ve Numbers"
    else:
        return l*b
l = int(input())
b = int(input())
print(area_of_rec(l*b))
'''
'''
# lambda

s = lambda s : s*s
print(s(4,3))

'''

'''
User reg in a web page---name
first name --> 
'''
'''
f_n = input()
l_n = input()
c = lambda f_n,l_n : f_n+" "+l_n
print(c(f_n,l_n))
'''
'''
# def 
f_n = input()
l_n = input()
def con(f_n,l_n):
    return f_n.title()+" "+l_n.title()
print(con(f_n,l_n)) 
'''
'''
n  = int(input())
res = lambda n:"Even" if n%2==0 else "Odd"
print(res(n))
'''
# len name
'''
n = input()
res = lambda name:len(name)
print(res(n))
'''

# filter 
'''
a = list(map(int,input().split(',')))
print(a)
b = list(filter (lambda x:x%2 ==0,a))
print(b)
'''
'''
name = ['pavan','abhiram','nihanth','saikrian','roshan']
b = list(filter( lambda name:len(name) > 6,name ))
print(b)


# maps

name = ['pavan','abhiram','nihanth','saikrian','roshan']
b = list(map( lambda name:name.upper(),name ))
print(b)
'''
'''
price = [1000,2500,3500,4000]
b = list(map( lambda price:(price - price *0.1),price))
print(b)
'''


from functools import reduce
numbers = [1,4,5,7,8]
res = reduce(lambda a,b:a+b,numbers)
print(res)