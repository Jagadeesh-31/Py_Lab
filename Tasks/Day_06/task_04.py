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
