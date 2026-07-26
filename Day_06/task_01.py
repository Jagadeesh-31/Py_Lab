names = []
bmis = []
categories = []

n = int(input("Enter no.of executions: "))

for i in range(1, n + 1):

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

    names.append(name)
    bmis.append(round(bmi, 2))
    categories.append(category)

print("\n----- BMI REPORT -----")

for i in range(n):
    print(f"{names[i]} -> {categories[i]} and BMI is {bmis[i]}")
