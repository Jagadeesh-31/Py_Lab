# datetime modueles  -->  datetime, module functionalites

import  datetime
#print(dir(datetime))

from datetime import datetime
a = datetime.now()
print(a)
print(type(a))

d = datetime.now()
print(d.date())
n= d.day
m = d.month
y= d.year
print(f'Today {d} - {m}-{y}')

d = datetime.today()
print(d.strftime("%A"))