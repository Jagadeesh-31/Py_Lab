# day_15

'''
Repetition --> for, while

while
'''

# while simple usage 
'''
count = 0
while count <5:
    print("you can  acess ele")
    a = []
    a.append("codegnan")
    print(a)
    count+=1'''

# Checking vaild attempets
'''
count = 6
while count >=1:
    print(f"Count = {count}")
    count-=1
    print(count)
   
'''

# To find valid password

'''
password = input("Enter Password:")
while password !='admin':
    password = input("Enter a Password")
    if password == 'admin':
             print(f'Correct password --> acess grant')
    else :
            print(" you acc has bolcked")
print(f'Correct password --> acess grant')
'''
'''
# now give 3 chanes for password check ---. if more than
password = input("Enter Password:")
count = 0
while password !='admin':
    password = input("Enter a Password")
    if password == 'admin':
             print(f'Correct password --> acess grant')
    else :
            password = input("Enter a Password")
            if password != 'admin':
               while count <3:
                       count+=1
               print(" you acc has bolcked")
               break
if password =='admin':
    print(f'Correct password --> acess grant')
else:
    print('Inavild Password')
'''
'''
# refrence
password = input("Enter Password: ")
count = 1

while password != "admin":
    print("Invalid Password")

    if count == 3:
        print("Your account has been blocked.")
        break

    password = input("Enter Password: ")
    count += 1

if password == "admin":
    print("Correct Password --> Access Granted")
'''
'''
# for with else,while with else --> else will be executed owhen loop completed done

# search item in store

search = input("Enter a search item: ")
store = ['mobile','laptop','powerbank','laptop']
for item in store:
    if search == item:
        print('item found')
        break
else:
    print("item not found!")

'''
# task
'''
 PIN verfication user should be give 3 chances if 3rd  chance is over
 it should return account  blocked  for this 24hrs --> balance with drwan show no.of chaqnces  to type corrct pin,'''

# break ,countinue, pass --> jumping statements


# contiune

'''
for i in 'codegnan':
    if i =='g':
        continue
         # break
    print(i)
'''
# pass

for i in range (10):
    pass
    print(i,end=' ')

