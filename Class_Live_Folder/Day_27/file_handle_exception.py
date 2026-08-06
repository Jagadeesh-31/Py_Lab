
'''
Tokens --> Identifiers,Varibles, Keywords,Literals,Operaters,Punctuators [],(),{}
Operators --> datatypes, control statments, function , module(use-def,built-in)
# email  automation (Bulk main (excel )),virutal assisent
File handling error handle (try,exception,finally) --> oops,reg expres -> web scrapping
 '''

# Store the data --> Files (.txt files) --> open()
# Files modes --> 'r','w','a'


'''
Syntax:
# default file mode --> open ("file.txt")
'''

#file = open('/home/workspace/my-project/Py_Lab/Day_27/example.txt')
'''print(file)
print(file.read()) # return the entire text from  the file 
print(file.read(10)) # we can also mention size
a = file.readlines()
print(len(a))
print(file.readline())
'''
#print(file.readlines())
import os
'''
if os.path.exists('/home/workspace/my-project/Py_Lab/Day_27/example.txt'):
    f = open('/home/workspace/my-project/Py_Lab/Day_27/example.txt').read()
    print(f)
    print("File is Found")
else:
    print("File not Found")
'''
 # default read mode
'''
file_path = '/home/workspace/my-project/Py_Lab/Day_27/example.txt'
if os.path.exists(file_path):
    print(f"File Size is {os.path.getsize(file_path)} Bytes")
    print(f'File path is {os.path.abspath(file_path)}')
else:
    print("File not Found")'''
# w mode --> 
'''
a = open('agents.txt','w')
print(a)
a.write("AAA-HYD_001")
a.write("APPLED AGENTIC AI")
a.close()
a.writelines("Rag is concept of Agentic Ai")
a.close()
'''
'''
b = open('example.txt','w')
print(b)
b.writelines("Rag is concept of Agentic Ai")
b.close()
'''

# if the file already present 'w' mode will overrider the content
'''
with open('example.txt','r+') as file:
    # print(file.read())  # raise an error 
    print(file)
    file.writelines("GenAI is Also part of the AAI")
    #file.seek(0)
    print(file.read())
    
'''


# append 
'''
with open('example.txt','a') as f:
    print(f)
    f.write("\n Pyhton,Agents,Rag.....")
    f.writelines("Hi Everyone")
    '''
'''
with open('rag.txt','a') as r:
    print(r)
    r.writelines("Agents,Mcp")

with open('rag.txt','r+') as d:
    print(d.read())
    d.write('\n Claude, Cahtgpt, Copilot')
    
'''
'''import os
d = os.listdir()
print(d)

for file in d:
    if file.endswith('.txt'):
        print(file)
'''

# Exception Handling --> Program (try,except,finally)

'''
try:
    base stmts which may raise error
    ........
except Exception (Error name) as e:
    ..........
finally:
    stmnts (s)....

'''

# TypeError, ValueError,Index Error, Arithmetic Error, Zero Divison Error, Att Error 
'''
try:
    a, b = map(int, input("Enter a,b values: ").split(','))

    res = a / b
    print(f"Result is {res}")

except ZeroDivisionError:
    print("Denominator cannot be zero.")

except ValueError:
    print("Please enter only integers separated by a comma.")
finally:
    print("Alway will be Printed")
'''


# exception together 
try:
    a, b = map(int, input("Enter a,b values: ").split(','))

    res = a / b
    print(f"Result is {res}")

except (ZeroDivisionError,ValueError) as e:
  print(f"The error occured {e}")

finally:
    print("Alway will be Printed")