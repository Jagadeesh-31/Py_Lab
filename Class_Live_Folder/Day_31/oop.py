'''
Tokens --> Datatypes --> Control Flow --> Functions --> Modules
Procedual Oriented Programimng --> Functions 
OOP --> Object Oriented Programing -->  objects
'''

# Wooden chair --> chair as obj,class(blue print which includes complent measurements,
#dimensions), carpenter -->User,Scrap,material,wood--> Memory

'''
class Product:
    """Simple Class demonstration with e-commerce example """
    platform="Amazon" # class Attrribute
    def display_product(self):
        print(f'Displaying Products')
    platforms = 'Flipkart'
    def stock_available(self):
            print(f'stock is availabble')
laptop = Product()
print(dir(laptop))
print(laptop.platform)
laptop.display_product()
laptop.stock_available()
Mobile = Product()
print(Mobile.platforms)
Mobile.display_product()
Mobile.stock_available()



# Product --> Class,platform --> attributes,display_product,stock_available --> methods..abs
'''
'''
class Product:
    """Usage of class with instance attributes"""
    platform = "Amazon" # class Attributes
    def store_product(self,name,price):
        self.name = name
        self.price = price
    def display_product(self):
        print(f'Product name is {self.name}')
        print(f'Product price is {self.price}')
Mobile = Product()
#print(dir(Mobile))
Mobile.store_product("Iphone",55000)
print(Mobile.name,Mobile.price)
Mobile2 = Product()
Mobile2.store_product("IQ",38000)
Mobile2.display_product()'''


# dynamic data
'''
class Product:
    """Usage of class with instance attributes"""
    platform = "Amazon" # class Attributes
    def store_product(self,name,price):
        self.name = name
        self.price = price
    def display_product(self):
        print(f'Product name is {self.name}')
        print(f'Product price is {self.price}')
n = int(input())
for i in range(n):
    prods = Product()
    name = input(f"Product {i+1} name: ")  
    price = int(input(f"Product {i+1} price: "))  
    prods.store_product(name, price) 
    prods.display_product() '''
'''
class Students:
    """Student detail AAA batch"""

    batch = "AAA-HYD_001"

    def stu_data(self):
        self.name = input("Enter student name: ")
        self.age = int(input("Enter age: "))
        self.place = input("Enter place: ")

    def details(self):
        print(f"Student name: {self.name}")
        print(f"Student from: {self.place} and age: {self.age}")


Std1 = Students()

print(Std1.batch)

Std1.stu_data()
Std1.details()

print(Std1.__dict__)
print(Std1.__doc__)
print(Std1.__class__)

Std1.stu_data()
Std1.details()
'''

class Students:
    """Student detail AAA batch"""

    batch = "AAA-HYD_001"
    def __init__(self,name,place,age):
        self.name = name
        self.place = place
        self.age = age
    def stu_data(self):
        self.name = name 
        self.age = age
        self.place = place

    def details(self):
        print(f"Student name: {self.name}")
        print(f"Student from: {self.place} and age: {self.age}")
Std1 = Students("saketh","hyd",22)
Std1.details()
Std2 = Students(name="sai",place="hyd",age=22)
Std2.details()
name = input()
place = input()
age = int(input())
Std3 = Students(name,place,age)
Std3.details()