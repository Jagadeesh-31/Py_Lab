#  Dictionary --> Collection of key-value pairs, Mutable, Ordered --->dict()


'''details = {}
print(details)
print(type(details))
'''
'''details = {'Name':'Tech','place':'Hyd','age':7}
print(details)


# Acessing Error

print(details['Name'])
# print(details['Age]') raise a key error

data = {'Name':'Tech','place':'Hyd','age':33,'age':22}
print(data) # recent update of values of age will be taken

# in dictonary we index by using key

# create dictionary using  other  datatypes
'''

'''
stu_data = { 'ids':[23,26,33,45],
                        'name':['sai','akash','jp','jd'],
                      'place':('Hyd','Vij'),
                      'gender':{'male',''}
    }
print(len(stu_data))
print(stu_data.keys())
print(stu_data['name'])

print(stu_data.values())

stu_data['Course'] = ['Pfs','jfs','aaa','da']

print(type(stu_data))

print(type(stu_data['ids']))


# insert 3 more unique ids

# Students as was not recommand this case  -- stu_data['ids']


stu_data['ids'].extend([56,67,88])
print(stu_data)


stu_data['name'].insert(1,'Chakri')


print(stu_data)

# insert new place as exist place

stu_data['place'] = list(stu_data['place'])
print(stu_data)

stu_data['place'].append('Viz')
print(stu_data)

# print below outputs


#['da','jfs']  do in single step
stu_data['Course']
print(stu_data['Course'])
print(stu_data['Course'][1::2])

# 23, 33, 45, 67, 88 id show as outpt
del stu_data['ids'][1::3]
print(stu_data)

'''




stu_data = { 'ids':[23,26,33,45],
                        'name':['sai','akash','jp','jd'],
                      'place':('Hyd','Vij'),
                      'gender':{'male',''}
    }
stu_data['name'].sort()
print(stu_data['name'])

# keys, val, items,
print(stu_data.items())

print(stu_data.get('branch'))
print(stu_data.get('branch','cse'))
print(stu_data)
#print(stu_data('branch')) --> it get error in dict


# setdefault

#update,pop,popitem,clear

stu_data.u



# clear,copty

# from keys
# nsted dict

# task dictionary-- own examples

