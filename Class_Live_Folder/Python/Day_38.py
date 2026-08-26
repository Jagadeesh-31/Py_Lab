'''
Tokens --> operator, Datatype, --> control flow  stmnts -- pop -- oop

Regula expressions  --> Data Analaysis(numpy,pandas , vizulization) --> web scriping and virtual assesuent
 
'''

# Regular Expressions


import re
# we use represention as r
'''
a = "\n"
print(a)
b = r"\n"  # here we use the representation of raw string  r' it treated as a character 
print(b)
print(len(b))
print(dir(re))'''


# we have received order as order id:24512
'''

string = "Order Id :4512"
result = re.search(r'\d',string)
print(result)
print(result.group())
result = re.search(r'\d+',string) # /d+ match digit - for one or more occrence
print(result)
print(result.group())

'''
# extract age of user from the data
'''
data = "My name is Rahul and My age is 25, i live in hyd"
age = re.search(r'\d+',data)
print(age) # it return the matching object
print(age.start()) # # return starting of obj
print(age.end()) # it  returns the end of matching objcet
print(age.span())
print(age.group()) # it return  complete match object
'''


# re.match()
'''
greeting = "Hello Agents"
res = re.match(r'Hello',greeting)
print(res)
if res:
    print(f'Matcung is Found {res.group()}')
else:
    print("Match Not found")


greeting = "Good Agents"
res = re.match(r'Hello',greeting)
print(res)
if res:
    print(f'Matcung is Found {res.group()}')
else:
    print("Match Not found")


#re.search()

f = re.search(r'[A-Z]',greeting)
print(f)

g = re.search(r'[A-Z]\w',greeting)
print(g)

h = re.search(r'[A-Z]\w+',greeting)
print(f.group())

j = re.search(r'[a-z]\w+',greeting)
print(j)
print(j.group())
i = re.findall(r'[A-Z]\w+',greeting)
print(j)

print(j.group())
k = re.findall(r'[A-z]\w+',greeting)
print(k)

gree = "Python 35 Agents 25 GENAI"
l = re.findall(r'[A-z][a-z]\w+',gree)
print(l)

'''

# re.finditer()
'''
ids = '23 45 36'
g = re.finditer(r'\d+',ids)
for n in g:
    print(n.group(),n.start())
print(*g)'''

#re.fullmatch()

data = "Codegnan is Hyderabad, Vijaywada & Vizag , contact number:8989898989"


#res = re.fullmatch(r'\d{2}',data) # patteren applicable for entire string it return None
#res = re.findall(r'\d{10}',data)
res = re.fullmatch(r'\d{10}','8989898989')

print(res)
print(res.group())



#res.sub() --> where can replace the original pattern
#re.split() --> we can specify the split pattern

f = " i love Food"
g = re.sub(r'Food','Agents',f)
print(g)
h = re.sub(r'\s','*',f)
print(h)

g = "Agents,GENAI;RAG,Python"
k = re.split(r'[,;]',g)
print(k)