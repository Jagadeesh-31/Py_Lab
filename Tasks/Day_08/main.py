# ---------- Task 1 ----------
def fact(n):
    if n < 0:
        return "Enter a +ve number"
    elif n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


# ---------- Task 2 ----------
def sum_of_n(n):
    if n < 0:
        return "Sum not possible"
    elif n == 0 or n == 1:
        return 1
    return n + sum_of_n(n - 1)


# ---------- Task 3 ----------
def fib(n):
    if n < 0:
        return "Enter a +ve number"
    elif n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


# ---------- Task 4 ----------
data = {
    "S.No": [],
    "Name": [],
    "BMI": [],
    "Category": []
}


def bmi_calculator():
    while True:
        try:
            sno = int(input("Enter S.No: "))
            name = input("Enter Name: ")
            weight = float(input("Enter Weight (kg): "))
            height = float(input("Enter Height (m): "))

            bmi = weight / (height ** 2)

            if bmi < 18.5:
                category = "Underweight"
            elif bmi < 25:
                category = "Normal Weight"
            elif bmi < 30:
                category = "Overweight"
            else:
                category = "Obesity"

            data["S.No"].append(sno)
            data["Name"].append(name)
            data["BMI"].append(round(bmi, 2))
            data["Category"].append(category)

            print("\nBMI Report")
            print({
                "S.No": sno,
                "Name": name,
                "BMI": round(bmi, 2),
                "Category": category
            })
            break

        except ValueError:
            print("Invalid Input")
        except ZeroDivisionError:
            print("Height cannot be zero")


# ---------- Task 5 ----------
def run_atm():
    balance = 10000
    history = []

    while True:
        print("\nSMART ATM")
        print("1. Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. History")
        print("5. Exit")

        ch = input("Enter Choice: ")

        if ch == "1":
            print("Balance:", balance)

        elif ch == "2":
            amt = int(input("Enter Amount: "))
            if amt <= balance:
                balance -= amt
                history.append(("Withdraw", amt))
                print("Withdraw Successful")
            else:
                print("Insufficient Balance")

        elif ch == "3":
            amt = int(input("Enter Amount: "))
            balance += amt
            history.append(("Deposit", amt))
            print("Deposit Successful")

        elif ch == "4":
            if history:
                for i in history:
                    print(i)
            else:
                print("No Transactions")

        elif ch == "5":
            print("Thank You")
            break

        else:
            print("Invalid Choice")


# ---------- Main Menu ----------
def day8_tasks():
    while True:
        print("\n========== DAY-08 TASKS ==========")
        print("1. Factorial")
        print("2. Sum of N Numbers")
        print("3. Fibonacci")
        print("4. BMI Calculator")
        print("5. ATM Simulation")
        print("6. Exit")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            n = int(input("Enter Number: "))
            print("Factorial =", fact(n))

        elif choice == "2":
            n = int(input("Enter Number: "))
            print("Sum =", sum_of_n(n))

        elif choice == "3":
            n = int(input("Enter Number: "))
            print("Fibonacci =", fib(n))
            print("Series:")
            for i in range(n):
                print(i, end=" ")
            print()

        elif choice == "4":
            bmi_calculator()

        elif choice == "5":
            run_atm()

        elif choice == "6":
            print("Program Closed")
            break

        else:
            print("Invalid Choice")


# ---------- Driver ----------
day8_tasks()
