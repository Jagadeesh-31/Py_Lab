# list comprehension

# append ele in list 
'''
list = []
for i in range(10):
    list.append(i)
    print(list)
'''

# apped ele in list with comprehension
'''
list = [i for i in range(10)]
print(list)
'''

# operations
'''
n = int(input())
list = [i for i in range(n)]
print(list)
list.append(56)
print(list)
print(list[::-1])
'''

# squares of numbers
'''
data = [i**2 for i in range(10)]
print(data)


e = [i%2==1 for i in range(10)]
print(e)
'''

'''
details = ['saketh','codegnan','data','agents','rag']
new = [i.upper() for i in details]
print(new)
print(*new)

'''

'''
a,*nam,c = 1,'saketh','codegnan','data',34
print(a)
print(nam) # output as -> ['saketh', 'codegnan', 'data']
print(*nam) #output as -. saketh codegnan data
print(c)
'''

'''
a = [15,20,25,30]
# update val in list
a  = [i+5 for i in a]
print(a)
'''
'''
data = ['codegnan','agents','rag']
let = [i[0] for i in data]
print(let)


data = ['codegnan','agents','rag']
let = [i[0][1:5] for i in data]
print(let)

'''

'''
collections = list(map(int,input().split(",")))
print(collections)
res = [i for i in collections if i%2==0]
print(res)

'''
# fliter --> lambda
'''
collections = list(map(int,input().split(",")))
print(collections)
res = list(filter( lambda i:i%2==0 ,collections ))
print(res)
'''

#1\collections = list(map(int,input().split(",")))
# fetch value if codition false_value for in items
'''
final = [i for i in collections if i >10]
print(final)

'''
# list comprehension using if-else cond
'''
data = [12,3,4,5,6,7,9]
print(data)
res = ["New" if i%2==0 else "old" for i in data]
print(res)
'''

# Nested List Condition 

# Nested -> one inse another(one loop inside another app)
'''
a = [(i,j) for i in  range(5) for j in range(3)]
print(a)


b = [(i,j) for i in [1,2,3,4]  for j in [2,3,5]]
print(b)

'''

# mulitplication
'''
b = [f"{i}*{j}= {i*j}" for i in range(1,11)  for j in range(1,11) if ]
print(b)
print(*b)
'''


# colors 
'''
colors = ['Red','Bule','Green']
sizes = ["S","M","L"]
dress = [(i,j) for i in colors for j in sizes]
print(dress)
'''
# Nested  comprehension wit if
'''
b = [i*j for i in range(1,11)  for j in range(1,11) if i!=j ]
print(b)
print(*b)
'''

#  using in list  
'''
a = [1,3,5,7]
b = [2,4,6,8,9]
c = [x+5 if x<y else x for x in a for y in b]
print(c)
'''

'''a = [1,3,5,7]
b = [2,4,6,8,9]
c = (x+5 if x<y else x for x in a for y in b)
print(c)

'''

#  no tuple comprehesion - generator

"""Normal syntax """
'''
def fun():
    return 1,2,3,4
print(fun())
'''


# yield --> generaqtor functions
'''
def fun():
    yield 1
    yield 2
    yield 3
b = fun()
print(next(b))
print(next(b))
'''


def display():
    yield "Python"
    yield "GenAi"
    yield "Rag"
    yield "Agentic"
print(display())
print(type(display()))
d = display()
print(next(d))

