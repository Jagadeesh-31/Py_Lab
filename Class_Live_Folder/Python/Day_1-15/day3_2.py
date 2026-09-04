'''n = int(input("Enter cp:"))
m = float (input("Enter sp:"))
total=n-m
print('Total Profit:',totalname
'''
'''
name,place = input("Enter your detail:").split()
print(name,place)
'''
'''name,place = input("Enter your detail:").split(",")
print(name,place)
'''

'''a,b,c = input("Enter detials:").split(',')
print(a)
print(b)
print(c)
'''


'''a,b,c = map(int,input("Enter detials:").split(','))
print(a)
print(b)
print(c)
'''
'''a,b,c = map(float,input("Enter detials:").split(','))
print(a)
print(b)
print(c)


a,b = map(float,input("Enter detials:").split(','))
print(a)
print(b)
'''
'''
data = input('Enter data:').split(',')
print(data)
print(data[:--1])
'''

'''d = list(map(int,input("Enter data:").split(',')))
print(d)'''

'''d = list(map(float,input("Enter data:").split(',')))
print(d)
'''

'''print(31,7,2026,sep="/t")

print(31,7,2026,sep="/------------/")
'''

name = 'codegnan'
place = 'hyd'
co = 'aaa'
''''print(name,place,end="")
print(co)
'''
'''print("Name:",name,"place:",place,"co:",co,sep=",")
flt = 45.56
print("%f"%(flt))
print("%.f"%(flt))
print("%.1f"%(flt))
print("%.2f"%(flt))

name,course = input("Enter a data:").split(",")
print(f"{name} is enrolled in {course} course")
'''

name,course = input("Enter a data:").split(",")
print("{} is enrolled in {} course".format(name,course))
