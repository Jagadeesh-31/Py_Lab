'''
   Type Coverstion --> list, tuple,set,dict
   list --> str,tuple,dic
'''

'''
age = [23,21,43]
age = list((21,12,43))

print(type(age))

b=  str(age)
print(b)

print(len(b))

c = tuple(age)
print(type(c))

e = dict.fromkeys(age)
print(e)
'''

'''# str -->list,tuple,dict

name = 'Codegnan'
print(type(name))
a = list(name)
print(a)
h = name.split(",")
print(h)

e = dict.fromkeys(name)
print(e)
'''


'''
#  Input Formating --> list,tuple,input,dict-->eval
data =eval(input("Enter Val"))
print(data)
print(type(data))
'''
'''
# repetition statements (loop) --> for , while

# loops  will automate tasks


marks = [24,25,21,20]
for mark in marks:
    print(mark)
    print(mark,end="\t")
'''
# Find the sum and avg of marks

'''marks = list(map(int,input().split(',')))
print(marks)
s = 0;avg=0
for i in marks:
    print(i)
    s+=i
    print(s)
    avg =s/len(marks)
    print(avg)
print(f"Total marks is {s}")
print(f"Total avg is {avg : s/len(marks)}")
'''
'''
l = list(input().split(','))
res = 0
for i in l:
    if type(i) in (int, float):
        res+=i
    print(res)
    '''

details = {
          'name':['sai','abhi','ram'],
          'marks':[45,65,34]
    }
'''
print(details.items())
 for i in details:
     print(1)
 '''    '''
for key in details:
     print( key)

for values in details.values():
     print(values)
for key,value in details.items:
     print(f'Keys is {key}')
     print(f'Values is {value}')


# range (start,end,step)

for i in range (5):
    print(i,end=' ')

for i in range(1,11):
    print(i,end=' ')
'''

'''
for i in range(10,-1,-2):
    print(i)

'''
'''
for i in reversed(range(0,10,2)):
    print(i)
'''
# home task

#output
'''
# A B C D E F G H

start = input().upper()
end = input().upper()

for i in range(ord(start), ord(end) + 1):
    print(chr(i), end=" ")'''
# h f db

a = input("Start: ").lower()
b = input("End: ").lower()
for i in range(ord(b), ord(a) - 1, -2):
    print(chr(i), end=" ")

'''
# Daily Workout --> Fintess  Streak

work_log = [1,1,1,0,1,1,0]
longest_streak = 0
current_streak = 0
# for including if, else
for day in work_log:
     if day  ==1:
         current_streak+=1
         if current_streak > longest_streak:
               longest_streak = current_streak
     else:
            current_streak =0
print(longest_streak)

'''



