# Opps with arguments

# varbile arguments 
'''
def sample(*args):
    """ Useage of Varible len srg"""
    print(args)
    print(type(args))
sample()
sample(1,2,3)
sample(1,23.45,'code')

# sample(name="sam") # raises a type error

def add(*a):
    res = 0
    print(a)
    for i in a:
        if type(i) in (int,float):
           # print(i)
            res+=i
    return res
# add()
#print(add(1,3))
print(add(1,3,'codegem',2.3,34,2.5,2+4j))

def sample(**kwargs):
    """Usage of Keyword arguments"""
    print(kwargs)
    print(type(kwargs))
sample()
sample(name = 'abhi',age=22,course='AAI')

def grocery(**item):
    print(item)
   # for i in items():
      #  print(i)
   # for j in items.values():
       # print(j)
    for key,val in item.items():
        print(f"{val} is {key}")
grocery()
grocery(name='Milk',price=35)
'''


'''
def bmi_cal(**kwargs):
    while True:
        try:
            name = input("Enter your name: ")
            weight = float(input("Enter your weight in Kgs: "))
            height = float(input("Enter your height in meters: "))
            num = int(input("Enter your num: "))

            if weight <= 0 or height <= 0:
                print("Weight and height must be greater than 0.")
                continue

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            print("BMI Report")
            print("Name     :", name)
            print("BMI      :", round(bmi, 2))
            print("Category :", category)

            choice = input("\nDo you want to calculate another BMI? (yes/no): ").lower()
            if choice != "yes":
                print("Thank you!")
                break

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
bmi_cal()



# task

# bmi --> unit conv  --> fun (args/kwagrs ****)


# Height Unit Converter + BMI Calculator using Dictionary

data = {
    "Name": [],
    "Height(m)": [],
    "BMI": [],
    "Category": []
}

print("===== Height Unit Converter & BMI Calculator =====")

while True:
    try:
        n = int(input("Enter no. of executions: "))
        if n > 0:
            break
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input! Enter numbers only.")

for i in range(1, n + 1):

    print(f"\n========== Execution {i} ==========")

    while True:
        try:
            name = input("Enter your name: ")
            num = int(input("Enter your mobile number: "))
            weight = float(input("Enter your weight (kg): "))

            if weight <= 0:
                print("Weight must be greater than 0.")
                continue

            print("\nSelect Height Unit")
            print("1. Centimeters")
            print("2. Inches")
            print("3. Feet")

            choice = int(input("Enter your choice: "))

            if choice == 1:
                cm = float(input("Enter height in centimeters: "))
                if cm <= 0:
                    print("Height must be greater than 0.")
                    continue
                meters = cm / 100

            elif choice == 2:
                inches = float(input("Enter height in inches: "))
                if inches <= 0:
                    print("Height must be greater than 0.")
                    continue
                meters = inches * 0.0254

            elif choice == 3:
                feet = float(input("Enter height in feet: "))
                if feet <= 0:
                    print("Height must be greater than 0.")
                    continue
                meters = feet * 0.3048

            else:
                print("Invalid choice! Please select 1, 2, or 3.")
                continue

            bmi = weight / (meters ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            # Store data in dictionary
            data["Name"].append(name)
            data["Height(m)"].append(round(meters, 2))
            data["BMI"].append(round(bmi, 2))
            data["Category"].append(category)

            print("\n===== Result =====")
            print("Name          :", name)
            print("Height (m)    :", round(meters, 2))
            print("BMI           :", round(bmi, 2))
            print("Category      :", category)

            break

        except ValueError:
            print("Invalid input! Please enter numeric values only.")

        except ZeroDivisionError:
            print("Height cannot be zero.")

print("\n========== BMI REPORT ==========")

for i in range(len(data["Name"])):
    print({
        "Name": data["Name"][i],
        "Height(m)": data["Height(m)"][i],
        "BMI": data["BMI"][i],
        "Category": data["Category"][i]
    })



# scope of varibles

# local
def fname(name):
    name="code"
    return name
print(fname())
#print name() --> rises a error 

# global
name = 'code'
def uname():
return name
print(uname())
print(name+' AAI')
# global keyword

count = 15
def update(**kwagrs):
    global count
    count+=10
    return count
print(update())
print(update(count+11))

# nonloacl

def outer():
    count = 10
    def inner():
        nonlocal count
        count+=5
        return count
    print(inner())   
    return count
print(outer())

'''

# built in scope 

len = 34
print(len)

