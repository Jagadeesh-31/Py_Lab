def bmi_cal(**kwargs):

    while True:

        try:

            name = input("Enter your name : ")

            weight = float(input("Enter your weight : "))
            w_unit = input("Enter weight unit (kg/lbs) : ").lower()

            if w_unit == "lbs":
                weight = weight * 0.453592

            height = float(input("Enter your height : "))
            h_unit = input("Enter height unit (m/cm) : ").lower()

            if h_unit == "cm":
                height = height / 100

            if weight <= 0 or height <= 0:
                print("Invalid weight or height")
                continue

            bmi = weight / (height * height)

            if bmi < 18.5:
                print("\nUnderweight")
            elif bmi < 25:
                print("\nNormal Weight")
            elif bmi < 30:
                print("\nOverweight")
            else:
                print("\nObesity")

            print("Name :", name)
            print("BMI :", round(bmi, 2))

            ch = input("\nDo you want to continue (yes/no) : ").lower().strip()

            if ch != "yes":
                print("Thank You")
                break

        except ValueError:
            print("Enter valid numbers only")

bmi_cal()
