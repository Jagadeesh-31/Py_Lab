# Membership oprs

'''fru = ['apple','orange','banana']
print('apple' in fru)
print(45 in fru)
print(45 in fru)
print(45 in [3,4,6,45,7])
print('5' in '234645')
print('code' in 'codegnan')
'''

# Identity oprs
'''
a = [1,2,3,4]
b = [1,2,3,4]
print(a==b)
print(a is b)
print(a is not b)
print(id(a))
print(id(b))
c = a
print(c is a)
print(c==a)
print(a is c)
print(id(a))
print(id(c))
print(c is not b)
'''



# logical oprs

a =14;b=23
c = a<b and b>a
print(c)
d = a<b and 'code' in ['apple']
print(d)

c = 12
# e  = c+=5
# print(e)
e = b<c or a in [12,23,4,14]
print(e)
print(not(False))
