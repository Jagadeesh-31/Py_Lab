# ploymorphism

# method overriding 

# Hotstar  -->  free user (can watch limited content and advertisements)
#           --->paid user (can watch premium content without advertisements)
#           -->premium user (watch live and premium content without advertisements)
'''
class User:
    """Method Overriding"""
    def watch(self):
        print("Watching basic content with advertisements")
class PaidUser:
    def watch(self):
         print("Watching premium content without advertisements")
    def paid_watch(self):
                 print("Watching premium content without advertisements")
u1 = User()
u1.watch()
u2 = PaidUser()
u2.watch()
u2.paid_watch()'''


# Different Subscription Plans
'''
class User:
    """Method Overriding with Hotstar scenario - Different Subscription Plans"""
    def watch(self):
        print("Watching basic content with advertisements")


class VIP_User(User):
    def watch(self):
        super().watch()
        print("Watching premium content without advertisements")


class Premium_User(VIP_User):
    def watch(self):
        super().watch()
        print("Watching premium Live content without advertisements")


u1 = User()
u1.watch()

u2 = VIP_User()
u2.watch()

u3 = Premium_User()
u3.watch()
'''



#Operator Overloading-->+,-,*,/
#(Magic Method / Dunder Method)
#__add__,__str__,__init__

'''
#integers
a = 15;b = 23
print(a+b)
print(a.__add__(b))
print(a.__add__(55))

#string
a = "jaga"
b = "b"
print(a+b)
print(a.__add__(b))
print(a.__str__())
print(a.__add__("M"))

#list
a = [1, 2, 3]
b = [4, 5, 6]
print(a+b) #merging
print(a.__add__(b))
print(a.__len__()) #prints len(a)
print(a.__add__([7, 8]))

'''


# Watch History in Hotstar Scenario
'''
class WatchHistroy:
    """understanding watching"""
    def __init__(self,hours):
        self.hours=hours
    # def new(self,other):
        #return self.hour+other.hour  --> Type Error for + 
    def __add__(self,other):
        return self.hours+other.hours
u1 = WatchHistroy(120)
u2 = WatchHistroy(100)
print(u1+u2)# here we are able to add both users watch history only beacuse 

# we use __add__ ()
'''

'''

class WatchHistroy:
    """understanding watching"""
    def __init__(self,hours):
        self.hours=hours
    # def new(self,other):
        #return self.hour+other.hour  --> Type Error for + 
    def __add__(self,other):
        return self.hours+other.hours
    def __str__(self):
         return f'Watching content for {self.hours} hours'
   # def new(self):
      #   return f'Watching content for {self.hours} hours'

u1 = WatchHistroy(120)
u2 = WatchHistroy(100)
print(u1+u2)
print(u1.__str__())


'''
# Abstractions 

# Instagram 


from abc import ABC, abstractmethod

class Content(ABC):
    @abstractmethod
    def upload(self):
        pass


class Photo(Content):
    def upload(self):
        print("Photo is Uploading")
        print("Photo is Compressing")
        print("Photo upload with effects")


class Video(Content):
    def upload(self):
        print("Video is uploading")
        print("Encoding video")
        print("Video compress without losing quality and upload")


class Reel(Content):
    def upload(self):
        print("Adding effects to reels")
        print("Uploading reel")
        print("Reel is uploaded")


contents = [Photo(), Video(), Reel()]

for con in contents:
    print(con)
    con.upload()