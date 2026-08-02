# BMI Usecase

'''
in this usecase (min-project) , we will make use of blocks statments

# BMI --> Body Mass Index -->> bmi=(weight/height**2) metres

'''
'''
n = int(input("Enter no.of exexcutions:"))
for i in range(1,n+1):
        
    weight = int(input("Enter your weight in Kgs:"))
    height = float(input("Enter you height in mtrs:"))
    name = input("Enter your name:")
    n = int(input("Enter your num:"))
    # print(bmi)

    # using built in dynamic appraoch for bmi calculator

    # (18.5 --> Underweight, 18.5-24.9  --> normalweight, 25,--29.9 --> overweight>=30)
    if bmi>0 and bmi > 0:
        bmi = (weight)/(height**2)
        if bmi <18.5:
            print(f" {name} -> Under weight and bmi is {bmi}")
        elif bmi > 18.5 and bmi < 24.9:
            print(f"{name} ->Normal Weight and bmi is {bmi}")
        elif bmi > 25 and bmi <29.9:
            print(f"{name} -> Overweight and bmi is {bmi}")
        elif bmi > 30:
                print(f"{name} -> Obesity and bmi is {bmi}")
    else:
        print("Invalid!!")

# task --> for some above bmi cla store in a dictionary

'''
'''
o/p as --> {name:[u1,u2],
            bmi :[bmi1,bmi2,]
} # alos used catgoy form useres  belongs to 
'''
# Exception Handle --> try,catch,final
'''
# weight

while True:
    try:
        w = int(input())
        h = float(input())
        if w >0 and h> 0:
            break
        elif w == 0 and h==0:
            break
        else:
            print("Make sure enter +ve values")
    except ValueError:
        print("Make Sure enter only valid input")
    except ZeroDivisionError:
        print("Both zeros are not allowed")
bmi = w / (h ** 2)

if w > 0 and h > 0:
    print(f"BMI = {bmi:.2f}")

if bmi < 18.5:
        print(f"Underweight")
        if bmi < 25:
            print(f"  Normal Weight")
        elif bmi < 30:
            print(f" Overweight")
        else:
            print(f" Obesity")
else:
        print("Invalid weight or height!")


# task -2 -->  try have zerto division error handle 

# Task - 3 --> bulid Atm claculator , user acc , pin verfication -

# check balannce , with draw , deposit, trancations, -->limit the valid pin 
'''
# functions

def add(a,b):
    c = a+b
    return c
a,b = map(int,input().split(","))
print(add(a,b))
