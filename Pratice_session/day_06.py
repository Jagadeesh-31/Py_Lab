# 1.armstrong number

n=int(input("Enter any number: "))
a=list(map(int,str(n)))
b=list(map(lambda x:x**3,a))
if(sum(b)==n):
    print(f"{n} is an armstrong number. ")
else:
    print(f"{n} is not an arsmtrong number. ")

#2. Marks improve
a,b,c = map(int,input().split(","))
if a>0 and b>0 and c>0:
    if a>=60 and b>=70 and c>=80:
        print("Improving")
    else:
        if a <=90 and b<=85 and c<=80:
            print("Deciling")
elif a==0 and b==0 and c ==0:
    print("Enter Correct Marks")
else:
    print("Invalid Marks")

# 3.data plan
plan_input = input("Enter plan (e.g., 5GB): ").upper()

size = int(plan_input.replace("GB", ""))

if size == 1:
    print('Plan A')
elif size <= 5:
    print("Plan B")
else:
    print("Plan C")


# 4.bmi claculation



# 3. Bmi Calculator


# Use Dict for BMI Calculation

data = {
    "S.No":[],
    "Name": [],
    "BMI": [],
    "Category": []
}


def bmi_calculator():
    while True:
        try:
            weight = float(input("Enter your weight in Kgs: "))
            height = float(input("Enter your height in meters: "))
            name = input("Enter your name: ")
            num = int(input("Enter your num: "))

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            data["S.No"].append(num)
            data["Name"].append(name)
            data["BMI"].append(round(bmi, 2))
            data["Category"].append(category)

            break

        except ValueError:
            print("Invalid input! Please enter numeric values.")

        except ZeroDivisionError:
            print("Height cannot be zero. Please enter a valid height.")


def display_report():
    print("\nBMI Report")

    for i in range(len(data["Name"])):
        print({
            "S.No": data["S.No"][i],
            "Name": data["Name"][i],
            "BMI": data["BMI"][i],
            "Category": data["Category"][i]
        })


n = int(input("Enter no.of executions: "))

for i in range(1, n + 1):
    print(f"\nExecution {i}")
    bmi_calculator()
display_report()



# 1. Even Number

n = int(input())
for i in range(n+1,-1,-1):
    if i%2==0:
        print(i,end=" ")



       # 2. Square Pattern of Number

n = int(input())
num = 1
max_num = n * n
width = len(str(max_num))  # Find how wide the largest number is

for i in range(n):
    for j in range(n):
        print(str(num).rjust(width), end=" ")
        num += 1
    print()


    #3. n nums divisble by 3
    n = int(input())
i = 1

while i <= n:
    if i % 3 == 0:
        print(i,end=" ")
    i += 1


#4. Multiplication table

n = int(input())

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


# 5.list of nums
nums = list(map(int, input().split(",")))
print(nums,sep=" ")
