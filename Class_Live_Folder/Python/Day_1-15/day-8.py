'''
Tuples -> tuples are an Immutable,ordered,Indexex Sequnce  type
use ()
'''

'''data = 1,24,5
print(data)
print(type(data))
'''
'''
# Nested tuples and alos have list inside it


details = ('codegnan',32,(2,4,5),'sanketh',[12,45,'agents','rag'])
print(details)
print(type(details))
print(details[2])
print(details[4][2]) 
print(details)
# output as codegfaf
b = details[0].replace('n','f')
print(b)
print(details)


details[4][2] = details[4][2].replace('a','A')
print(details)
print(details[1:4])
print(details[::3])

 #  usind indexing, slicing, and striding

'''
# operations
'''
ages  = 22,28,24,26
ids = 231,232,232,234
print(ages+ids)
print(ages*2)
print(22 in ages)
'''

 # len,type,min,max,sorted
''' 
ages =22,24,29,28,27
print(min(ages))
print(max(ages))
print(tuple(sorted(ages))) # type casting
print(ages)
'''

#index,count
'''
details = ('sanketh','codegnan','agentic ai',34,23,5,8)
print(details)

print(details.index(34))
print(details.count(34))
'''
 # tuple - list..
'''details = ('sanketh','codegnan','agentic ai',34,23,5,8)

d = list(details)
print(type(d))

'''

# str -- list,tuple
'''a = 'codegnan'
b = list(a)
c = tuple(a)
print(b)
print(c)
print(type(b))
print(type(c))

b = str(b)
print(b)
print(type(b))
c = str(c)
print(c)
print(type(c))
'''

# sets datype -- >sets,forzon sets
'''
a ={}
b = set()
print(type(a))
print(type(b))



ids = {123,124,125,126,124,124}
isk = {12,3,45,54}
print(ids)
print(len(ids))
'''

# as set is mutable
# add,update
'''
ids = {123,124,129,126}
#ids.add(156)
#print(ids)
#ids.add('aai')
#print(ids)

ids.update(['jd','codegnan','500072'])
print(ids)
'''

# remove ele -- discard,remove,pop,clear
'''
ids = {123,124,129,126}
ids.remove(129)
print(ids)
ids.discard(124)
print(ids)
print(ids.pop())
print(ids)

'''


ids = {123,124,127,126,128,124}

# uinons | ,intersection,diff,symmentric,subsets,supersets

ages  ={ 22,28,24,26,29,124,144,127}

'''print(d)

e = ids.update(ages)
print(e)
print(ids)
'''
'''
f = ids.intersection(ages) #&
print(f)

g = ids.intersection_update(ages)
print(g)
print(ids)

'''
'''h = ids.difference(ages) #-
print(h)

g = ages.symmetric_difference(ids)

i = ids.symmetric_difference(ages)
print(i)


print(g)
'''

'''a = {1,2,3}
b = {1,2,3,4,5}
print(a.issubset(b))
print(b.issuperset(a))
print(a.isdisjoint(b))
'''


'''a = {8,6,7}
b = {1,2,3,4,}
print(a.isdisjoint(b))
'''


# frozen sets -->immutable
data = frozenset(ids)
print(data)
print(type(data))

details = frozenset([22,24,26,27])
print(details)

# sorted,max,min



# practice on lists sets create a nested seq inclide a list with tuple  and stings and sets
