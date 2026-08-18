# Inheritannce --> Hierarchical Inheritance, Hybrid Inheritance 

# Hierarchical Inheritance
# whatsapp scenario
'''
class User:
    """User class with Msg Propertites"""
    def send_message(self):
        print('Sending Messages')
class PersonalUser(User):
    """PErsonal user class inherting from user"""
    def status_update(self):
        print('Status Updated only for contacts')
class BusinessUser(User):
    """Business User"""
    def creat_catlog(self):
        print("catlog ccreation is possible")
class VerifiedBusinessUser(User):
    """Verified User"""
    def premium_acess(self):
        print("Bule tick added, premium features loaded")
class CommunityUser:
    """Commity Admi acess"""
    def creat_commity(self):
        print(f'Community Acess')
user1 = User()
user1.send_message()
user2 = PersonalUser()
user2.status_update()
user3 = BusinessUser()
user3.creat_catlog()
user4 = CommunityUser()
user4.creat_commity()
'''


# hybrid
'''
class User:
    """User class with voice calls"""
    def voice_call(self):
        print("Making voice call")
    def video_call(self):
        print('making video call')
class Notification(User):
    """Sendind Notification"""
    def notify(self):
        print("Sending Notification")
class BusinessUser:
    """Business User acess"""
    def catlog(self):
        print('Catlog is Updated')
class PremiumBusinessUsers(BusinessUser,Notification):
    """Premium Content"""
    def premium_acess(self):
        print('Bule tick verification and reach acess')
user1 = BusinessUser()
user1.catlog()'''



# Polymorphism

# method overloadijng -->method with default argumrnts, method with varible len(*args), checkimg with varible type

# method overiding --
# oper overloading 

# Hostar --> free user,premium user, adv premium user

'''
class Hostar:
    """Simple example to understand ploymorphism"""
    def watch(self):
        print('Welcome to hotstar home page... and loading....')
    def watch(self,movie):
        self.movie = movie
        print(f'Loaded hotstar watching {self.movie}')
user = Hostar()
user.watch("Leo")
user.watch("89")
'''


# method overloading with default arguments
'''
class Hotstar:
    """method overloading with default arguments"""
    def watch(self,movie=None):
        if movie==None:
            print('Welcome to hotstar....')
        else:
            print(f"Watching {movie}")
user = Hotstar()
user.watch()
user.watch("Vikram")
'''

# Inheritannce --> Hierarchical Inheritance, Hybrid Inheritance 

# Hierarchical Inheritance
# whatsapp scenario
'''
class User:
    """User class with Msg Propertites"""
    def send_message(self):
        print('Sending Messages')
class PersonalUser(User):
    """PErsonal user class inherting from user"""
    def status_update(self):
        print('Status Updated only for contacts')
class BusinessUser(User):
    """Business User"""
    def creat_catlog(self):
        print("catlog ccreation is possible")
class VerifiedBusinessUser(User):
    """Verified User"""
    def premium_acess(self):
        print("Bule tick added, premium features loaded")
class CommunityUser:
    """Commity Admi acess"""
    def creat_commity(self):
        print(f'Community Acess')
user1 = User()
user1.send_message()
user2 = PersonalUser()
user2.status_update()
user3 = BusinessUser()
user3.creat_catlog()
user4 = CommunityUser()
user4.creat_commity()
'''


# hybrid
'''
class User:
    """User class with voice calls"""
    def voice_call(self):
        print("Making voice call")
    def video_call(self):
        print('making video call')
class Notification(User):
    """Sendind Notification"""
    def notify(self):
        print("Sending Notification")
class BusinessUser:
    """Business User acess"""
    def catlog(self):
        print('Catlog is Updated')
class PremiumBusinessUsers(BusinessUser,Notification):
    """Premium Content"""
    def premium_acess(self):
        print('Bule tick verification and reach acess')
user1 = BusinessUser()
user1.catlog()'''



# Polymorphism

# method overloadijng -->method with default argumrnts, method with varible len(*args), checkimg with varible type

# method overiding --
# oper overloading 

# Hostar --> free user,premium user, adv premium user

'''
class Hostar:
    """Simple example to understand ploymorphism"""
    def watch(self):
        print('Welcome to hotstar home page... and loading....')
    def watch(self,movie):
        self.movie = movie
        print(f'Loaded hotstar watching {self.movie}')
user = Hostar()
user.watch("Leo")
user.watch("89")
'''


# method overloading with varible length argumnets
'''
class Hotstar:
    """method overloading with default arguments"""
    def watch(self,movie=None):
        if movie==None:
            print('Welcome to hotstar....')
        else:
            print(f"Watching {movie}")
    def watching_list(self,*movie):
        self.movie=movie
        print(f'watching list movie {self.movie}')
movie=input().lower()
user = Hotstar()
user.watch()
user.watch("Vikram")
user.watch(movie)
user.watching_list(['89','Leo','salaar'])'''

# managment System 

# method overloading --> checking types of argument
# hotstar --> one movie,more movie...

'''
class Hotstar:
    """checking type arguments usage """
    def movie_list(self,content):
        if isinstance(content,str):
            print(f"watching {content}")
        elif isinstance(content,list):
            for movie in content:
                print(movie)
user = Hotstar()
user.movie_list("vikram")
user.movie_list(["Leo","Vikram","Salaar"])

'''
