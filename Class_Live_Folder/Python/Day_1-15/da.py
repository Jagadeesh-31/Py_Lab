Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#type converstion
ade = 32
b = float(ade)
b
32.0
c = complex
c = complex(ade)
c
(32+0j)
bool(0)
False
d = bool




9
d = bool(age)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    d = bool(age)
NameError: name 'age' is not defined. Did you mean: 'ade'?
d  = bool(ade)
d
True
price  = 33.33
a = int(price)
a
33
a = complex(price)
a
(33.33+0j)
a = bool(price)
a
True
b = 2+3j
a = int(b)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a = int(b)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> e = int(b)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    e = int(b)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
>>> h = float(b)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    h = float(b)
TypeError: float() argument must be a string or a real number, not 'complex'
>>> f = bool(b)
>>> f
True
>>> h = bool(price+age)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    h = bool(price+age)
NameError: name 'age' is not defined. Did you mean: 'ade'?
>>> h
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    h
NameError: name 'h' is not defined
>>> price  = 33
>>> age = 22
>>> h = bool(price+age)
>>> h
True
>>> a = bool(int(float(23)))
>>> a
True
>>> a = int (float(bool(11)))
>>> a
1
>>> a =True
>>> int(a)
1
>>> float(a)
1.0
>>> complex(a)
(1+0j)
