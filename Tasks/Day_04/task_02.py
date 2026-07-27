'''
1
23
456
78910
'''

n = int(input())
r = int(input())
for i in range(1,r+1):
      for j in range(i):
          print(n,end=" ")
          n+=1
      print() 
