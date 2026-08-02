'''
assert 
'''
'''
x =  int(input("Enter a postive num:"))
#assert x > 0
#assert x > 0, "Value must be positive Number"
assert x in x
x += 2
print(f'Update val is {x}')

'''

# Nested --> Patterns Generations
'''
for i in range(3):
    for j in range(2):
       # print(f"Value i is {i} , Value of j is {j} ")
       print(i,j)
'''
'''
for i in range(2):
    for j in range(4):
       # print(f"Value i is {i} , Value of j is {j} ")
       print(i,j)'''

# Num patterns , row based number  patterns ,cloumns baesd patterns traiangle
'''
for i in range(1,5):
    for j in range(1,4):
       print(j,end=" ")
    print()
  '''
'''
1 1 1
2 2 2
3 3 3
'''
'''
for i in range(1,4):
    for j in range(1,4):
       print(i,end=" ")
    print()       
'''
'''
A A A
B B B
C C
 C
'''
'''
for i in range(ord('A'), ord('D')):
    for j in range(ord('A'), ord('D')):
        print(chr(i), end=" ")
    print()
'''

'''
 1 2 3 
 4 5 6 
 7 8 9
 '''
'''
n=1
for i in range(3):
    for j in range(3):
        print(n, end = " ")
        n+=1
    print()
'''

'''
* * *
* * *
* * *
'''
'''
n=1
for i in range(3):
    for j in range(3):
        print("*", end = " ")
        n+=1
    print()
    '''
'''
for i in range(4):
    for j in range(5):
        print("*", end = " ")
    print()
    '''

'''
*
**
***
****
'''


for i in range(1,5):
    for j in range(i):

        print("*", end = " ")
    print()




    # task

'''
   ***
   **
   *
''''

'''
1
23
456
78910



A
B C
D E F
'''