'''
1
12
123
1234
12345
'''
'''n = int(input())
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''


'''
A 
A B
A B C
A B C D'''
'''
for i in range(ord('A'),ord('F')):
    for j in range(ord('A'),i+1):
        print(chr(j),end=" ")
    print()
   '''
'''
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if j <= n-i:
            print(" ",end='')
        else:
            print('*',end=' ')
    print()
    
'''
    # hom task

'''
        *
       * *
    * *  * *
     * * *
      * *
       *
'''

'''    *
   ***
  *****
 *******
*********
 *******
  *****
   ***
    *

    '''


n = int(input())

# Upper Half
for i in range(1, n + 1):

    # Spaces
    for j in range(n - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()

# Lower Half
for i in range(n - 1, 0, -1):

    # Spaces
    for j in range(n - i):
        print(" ", end="")

    # Stars
    for j in range(2 * i - 1):
        print("*", end="")

    print()