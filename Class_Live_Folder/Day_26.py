
from datetime import datetime,timedelta

'''
b = datetime(2026,8,15)
print(b)
print(type(b))

c = datetime(day=10,month=9,year=2026,hour=10,minute=30)
print(c)
print(type(c))
'''

'''
d = datetime.date()
print(d)'''

# print(dir(datetime))


# Accept input from user --. convert to datetime obj -return
#string from (part date,month name)
'''
day = input()
mon = input()
year= int(input())
s = datetime.now()
print(s)
print(day,mon,year)
d = datetime.today()

print(f'{d.strftime("%A")} {day} - {mon}-{year}')
'''
'''
d,m,y = map(int(input().split(",")))
print(d,m,y)
d_obj = datetime(y,m,d)
print(d_obj)
print(f"Today is {d_obj.strftime("%A")}")
print(f"The month is {d_obj.str("%B")}")
'''

#strptime() --> datetime --> str formate 

'''
f = datetime.now()
#print(f)
#print(type(f))
dayofweek = datetime.strptime(("2005-12-11"),"%Y-%m-%d")
#print(dayofweek)

#print(dayofweek.strftime("%A"))



# timedelta--> handling  tim diff
print(f)
print(dayofweek)
#days,hrs,mins,sec
diff = timedelta(days=5,hours=10)
print(diff)

print(f-diff)
print(f+diff)
print(f+timedelta(hours=5,minutes=30))  # this return cureent time ist time


d =f+timedelta(hours=5,minutes=30)
print(d)
print(f'Future date is {d+timedelta(days=5,hours=10)}')'''


# time --> time functionality 

import time
'''
#print(dir(time))
print(time.tzname)
print(time.ctime)
print(time.localtime())'''
d_obj = time.localtime()
y = d_obj.tm_year
m = d_obj.tm_mon
day = d_obj.tm_mday
print(f"Date is {day}-{m}-{y}")