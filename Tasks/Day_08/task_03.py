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
