# pass By value
#pass ny obj ref

# pass by  val ref --

'''
def update(number):
    number = 15
    number *= 5
    return number
print(update(5))
print(update('2'))

'''
'''
# str 

def strs(name):
    name = 'codenow'
    return name +"AI"
print(strs("Agentic"))
name = 'Code'
print(strs("name"))
'''


# pass obj --> list
'''
def lst(items):
    items.append("ai")
    return items
ls = ['code','gt']
print(lst(ls))
'''

# set

'''
# dic
def dic(items):
    items.update({"course": "AI"})
    return items

d = {"name": "Code", "type": "GT"}
print(dic(d))'''


#cbulit functions

#if __name__ == " __main__":
    #print(2+34)
    #print(dir())
    #print(dir(__builtins__)) 
#print(abs(-23))

# all,any
'''
data = ['sakth','sai']
data.clear()
d = [None,23,22]
print(all(data))
print(any(data))
print(all(d))
print(any(d))

'''
'''
if __name__ == "__main__":
    print(dir(__builtins__))
print(bin(6))
print(chr(65))
print(bool(0))
print(complex())
print(dict(name='codenow',place='hyd'))

'''

#print(divmod(5,3))

#print(eval("5+3"))

data = ['code','saket','ai']
#print(dict(enumerate(data)))
'''
for i in data:
    print(data.index(i),":",i)
'''
'''
for i,name in enumerate(data):
    print(i,":",name)

  '''

a = eval


