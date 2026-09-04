Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #type cov -- int,float,complex,bool ---list
>>> age = 22
>>> type(age)
<class 'int'>
>>> b = list(age)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b = list(age)
TypeError: 'int' object is not iterable
>>> c = list(1,2,3)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    c = list(1,2,3)
TypeError: list expected at most 1 argument, got 3
>>> c = list((1,2,3))
>>> c
[1, 2, 3]
>>> b = list((16.4,33.45,33))
>>> b
[16.4, 33.45, 33]
>>> c = list((1+2j,3+5j,4+9j))
>>> c
[(1+2j), (3+5j), (4+9j)]
>>> d = list((True,False))
>>> d
[True, False]
>>> pruce = 33.45
>>> e = list(price)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    e = list(price)
NameError: name 'price' is not defined. Did you mean: 'pruce'?
>>> com = 3+5j
>>> f = list(com)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    f = list(com)
TypeError: 'complex' object is not iterable
>>> a = list(True)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a = list(True)
TypeError: 'bool' object is not iterable
>>> a = bool(list(a))
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a = bool(list(a))
NameError: name 'a' is not defined
#tuple
tem=33.4
tuple(temp)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    tuple(temp)
NameError: name 'temp' is not defined. Did you mean: 'tem'?
tuple(2,3,4)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple(2,3,4)
TypeError: tuple expected at most 1 argument, got 3
tuple(23.4,33.4)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    tuple(23.4,33.4)
TypeError: tuple expected at most 1 argument, got 2
tuple(True)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    tuple(True)
TypeError: 'bool' object is not iterable
m = tuple(1,2.5,'code')
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    m = tuple(1,2.5,'code')
TypeError: tuple expected at most 1 argument, got 3
m = tuple((1,2.5,'code'))
m
(1, 2.5, 'code')
tuple(False)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    tuple(False)
TypeError: 'bool' object is not iterable
tuple(None)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    tuple(None)
TypeError: 'NoneType' object is not iterable
n  = tuple((1,2.5,3+1j,True))
n
(1, 2.5, (3+1j), True)
val = 45
b = str(val)
b
'45'
print(b)
45
type(b)
<class 'str'>
dfis = 1.5
a = str(dfis)
a
'1.5'
c=str(1+3j)
c
'(1+3j)'
d = str(True)
d
'True'
a = 3
b  = set(a)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    b  = set(a)
TypeError: 'int' object is not iterable
b = 14.5
e = set(b)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    e = set(b)
TypeError: 'float' object is not iterable
c = 2+4j
f = set(c)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    f = set(c)
TypeError: 'complex' object is not iterable
d = True
g = set(d)
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    g = set(d)
TypeError: 'bool' object is not iterable
a = set(1,2,3)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a = set(1,2,3)
TypeError: set expected at most 1 argument, got 3
b = set(12.3,12.35)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    b = set(12.3,12.35)
TypeError: set expected at most 1 argument, got 2
set(2+3j)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    set(2+3j)
TypeError: 'complex' object is not iterable
a = 23
b = dict(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    b = dict(a)
TypeError: 'int' object is not iterable
c = 23.45
d = dict(c)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    d = dict(c)
TypeError: 'float' object is not iterable
e = 2+3j
f = dict(e)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    f = dict(e)
TypeError: 'complex' object is not iterable
g = True
h = dict(g)
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    h = dict(g)
TypeError: 'bool' object is not iterable
a = dict{'name:Jd','age:22','college:srkr'}
SyntaxError: invalid syntax
a = dict('name:Jd','age:22','college:srkr')

Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    a = dict('name:Jd','age:22','college:srkr')
TypeError: dict expected at most 1 argument, got 3
