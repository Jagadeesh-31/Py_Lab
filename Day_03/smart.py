CORRECT_PIN = 1888
balance = 15000
max_attempts = 3
attempts = 0
is_blocked = False
pin_verified = False

print("      WELCOME TO THE SMART ATM SYSTEM    ")

if is_blocked:
    print("ACCOUNT BLOCKED Your account is currently blocked for 24 hours due to 3 failed attempts.")
    print("Simulated Time Remaining: 24 hours, 00 minutes, 00 seconds.")
else:
    print("  PIN Verification ")
    while attempts < max_attempts:
        user_pin = int(input("Please enter your 4-digit ATM PIN: "))

        if user_pin < 1000 or user_pin > 9999:
            print("Error: Invalid PIN format! Must be exactly 4 digits. (Attempt not counted)\n")
            continue  

        if user_pin == CORRECT_PIN:
            print("\nSuccess: PIN verified successfully!")
            pin_verified = True
            break
        else:
            attempts += 1
            print("Error: Incorrect PIN.")

            if max_attempts - attempts > 0:
                print("Remaining attempts:", max_attempts - attempts, "\n")
            else:
                is_blocked = True
                print("\n[ALERT] You have exceeded 3 failed attempts. Account blocked for 24 hours!")
                print("Block Start Simulated: 24 hours, 00 minutes remaining before next login.")

if pin_verified:
    print("\n--- Cash Withdrawal ---")
    while True:
        withdrawal_amount = int(input("Enter amount to withdraw (₹): "))

        if withdrawal_amount <= 0:
            print("Error: Withdrawal amount must be a positive number greater than 0.\n")
        elif balance - withdrawal_amount < 500:
            print("Error: Transaction Declined! Account must maintain a minimum balance of ₹500.")
            print("Current Balance:", balance, "| Maximum Withdrawable Amount:", balance - 500, "\n")
        else:
            balance = balance - withdrawal_amount
            print("\n--- Transaction Receipt ---")
            print("Withdrawn Amount:", withdrawal_amount)
            print("Updated Balance :", balance)
            print("----------------------------\n")
            break

    print("--- Weekend Budget Planner ---")
    while True:
        budget = int(input("Enter your planned weekend budget (₹): "))

        if budget < 0:
            print("Please enter a valid, non-negative budget.\n")
        elif budget > 10000:
            print("\nSuggested Activity: Plan a Trip")
            break
        elif budget >= 5001:
            print("\nSuggested Activity: Resort Stay")
            break
        elif budget >= 3001:
            print("\nSuggested Activity: Movie and Dinner")
            break
        elif budget >= 1001:
            print("\nSuggested Activity: Cafe and Shopping")
            break
        elif budget >= 501:
            print("\nSuggested Activity: Street Food and Park Visit")
            break
        else:  # 0 to 500
            print("\nSuggested Activity: Stay Home")
            break

print("\nThank you for using the Smart ATM System. Program ended.")
