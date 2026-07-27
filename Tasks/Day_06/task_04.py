# Height Unit Converter

name = input("Enter your name: ")
print("Welcome", name)

while True:
    try:
        n = int(input("How many times do you want to convert height? "))
        if n > 0:
            break
        else:
            print("Enter a positive number.")
    except ValueError:
        print("Enter only numbers.")

for i in range(1, n + 1):
    print(f"\nConversion {i}")

    while True:
        try:
            print("\nSelect Height Unit")
            print("1. Centimeters")
            print("2. Inches")
            print("3. Feet")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                cm = float(input("Enter height in centimeters: "))
                if cm <= 0:
                    print("Height must be greater than 0. Try again.")
                    continue
                meters = cm / 100
                print("Height in meters =", round(meters, 2))
                break

            elif choice == 2:
                inches = float(input("Enter height in inches: "))
                if inches <= 0:
                    print("Height must be greater than 0. Try again.")
                    continue
                meters = inches * 0.0254
                print("Height in meters =", round(meters, 2))
                break

            elif choice == 3:
                feet = float(input("Enter height in feet: "))
                if feet <= 0:
                    print("Height must be greater than 0. Try again.")
                    continue
                meters = feet * 0.3048
                print("Height in meters =", round(meters, 2))
                break

            else:
                print("Invalid choice. Please select 1, 2, or 3.")

        except ValueError:
            print("Invalid input. Please enter numbers only.")
