# Smart ATM Banking Management System

# System Accounts Database
users = {
    "1888": {
        "name": "kl",
        "balance": 25000,
        "blocked": False,
        "drawn_today": 0,
        "count_today": 0,
        "rewards": 100,
        "history": ["Deposit ₹20000", "Withdraw ₹1000"]
    },
    "5678": {
        "name": "Rahul",
        "balance": 15000,
        "blocked": False,
        "drawn_today": 0,
        "count_today": 0,
        "rewards": 50,
        "history": ["Deposit ₹15000"]
    },
    "8888": {
        "name": "Priya",
        "balance": 30000,
        "blocked": False,
        "drawn_today": 0,
        "count_today": 0,
        "rewards": 200,
        "history": ["Deposit ₹30000"]
    }
}

atm_cash = 50000
maintenance = False
txn_counter = 1001
total_txns = 0
bad_inputs = 0

running = True
logged_pin = None

# PART 1: SMART ATM SYSTEM
while running:
    if bad_inputs >= 5:
        print("\nToo many wrong inputs. Program stopping.")
        break

    if maintenance:
        print("\nATM is currently under maintenance.")
        break

    if atm_cash <= 0:
        print("\nATM has no cash left.")
        break

    print("      SMART ATM BANKING SYSTEM    ")

    card = input("Is card inserted?\n1. Yes\n2. No\nEnter option: ").strip()
    if card == "2":
        print("Please insert your ATM card.")
        continue
    elif card != "1":
        bad_inputs += 1
        print("Invalid choice.")
        continue

    lang = input("\nSelect Language (1. English / 2. Telugu / 3. Hindi): ").strip()
    bank = input("Select Bank (1. SBI / 2. HDFC / 3. ICICI / 4. Axis): ").strip()
    acc = input("Select Account Type (1. Savings / 2. Current): ").strip()

    if lang not in ["1", "2", "3"] or bank not in ["1", "2", "3", "4"] or acc not in ["1", "2"]:
        bad_inputs += 1
        print("Invalid selection.")
        continue

    attempts = 0
    logged_pin = None

    # PIN Verification Loop (Max 3 attempts)
    while attempts < 3:
        pin = input("\nEnter 4-digit PIN (9999 for Admin): ").strip()

        # ADMIN MODE
        if pin == "9999":
            print("\n ADMIN MENU")
            print("1. Check ATM Cash")
            print("2. Check Total Transactions")
            print("3. Unblock User Account")
            print("4. Toggle Maintenance Mode")
            print("5. Register New Account (Keyboard Input)")
            
            ad_ch = input("Enter choice (1-5): ").strip()

            if ad_ch == "1":
                print("ATM Cash Remaining: ₹", atm_cash)
            elif ad_ch == "2":
                print("Total Transactions Today:", total_txns)
            elif ad_ch == "3":
                print("\nRegistered Accounts:")
                for p_key, u_data in users.items():
                    status = "Blocked" if u_data["blocked"] else "Active"
                    print(f"PIN: {p_key} | Name: {u_data['name']} | Status: {status}")
                
                unblock_p = input("Enter PIN to unblock: ").strip()
                if unblock_p in users:
                    users[unblock_p]["blocked"] = False
                    print("Account unblocked successfully!")
                else:
                    print("Account PIN not found.")
            elif ad_ch == "4":
                maintenance = not maintenance
                print("Maintenance status set to:", maintenance)
            elif ad_ch == "5":
                print("\n--- NEW ACCOUNT REGISTRATION ---")
                new_name = input("Enter Customer Name: ").strip()
                
                while True:
                    new_pin = input("Set 4-Digit PIN: ").strip()
                    if len(new_pin) == 4 and new_pin.isdigit():
                        if new_pin in users:
                            print("PIN already exists! Try another.")
                        elif new_pin in ["0000", "1111", "1234", "9999"]:
                            print("Weak PIN! Choose a better PIN.")
                        else:
                            break
                    else:
                        print("PIN must be 4 digits.")
                
                while True:
                    bal_str = input("Enter Initial Deposit (Min ₹500): ").strip()
                    if bal_str.isdigit() and int(bal_str) >= 500:
                        in_bal = int(bal_str)
                        break
                    else:
                        print("Invalid amount. Minimum deposit is ₹500.")

                users[new_pin] = {
                    "name": new_name,
                    "balance": in_bal,
                    "blocked": False,
                    "drawn_today": 0,
                    "count_today": 0,
                    "rewards": 0,
                    "history": [f"Account Created: Deposit ₹{in_bal}"]
                }
                print(f"Account for {new_name} created successfully!")
            else:
                print("Invalid option.")
            break

        # USER LOGIN & PIN VERIFICATION
        if pin in users:
            if users[pin]["blocked"]:
                print("\nAccount is BLOCKED due to security reasons.")
                print("Please wait 24 hours for automatic recovery or visit your bank branch.")
                break
            logged_pin = pin
            break
        else:
            attempts += 1
            bad_inputs += 1
            if attempts < 3:
                print("Wrong PIN! Remaining attempts:", 3 - attempts)
            else:
                print("\n3 Incorrect PIN attempts entered!")
                print("Account blocked! 4th attempt is NOT allowed.")
                print("Your account will recover automatically after 24 hours.")

    if not logged_pin:
        continue

    # USER MAIN ATM SESSION
    u_data = users[logged_pin]
    print("\nWelcome,", u_data["name"] + "!")

    session = True
    while session:
        if bad_inputs >= 5:
            running = False
            session = False
            break

        print("\n=== ATM MAIN MENU ===")
        print("1. Balance Enquiry")
        print("2. Cash Withdrawal")
        print("3. Cash Deposit")
        print("4. Mini Statement")
        print("5. Change PIN")
        print("6. Fast Cash")
        print("7. Savings Goal")
        print("8. Loan Eligibility")
        print("9. Exit ATM")

        ch = input("Enter choice (1-9): ").strip()

        if ch == "1":
            cb = u_data["balance"]
            ab = cb - 500 if cb >= 500 else 0
            print("\nCurrent Balance  : ₹", cb)
            print("Available Balance: ₹", ab)
            print("Reward Points    :", u_data["rewards"])

        elif ch == "2" or ch == "6":
            amt = 0
            if ch == "6":
                print("\nFast Cash Options:")
                print("1. ₹500  2. ₹1000  3. ₹2000  4. ₹5000  5. ₹10000")
                fc_ch = input("Select option (1-5): ").strip()
                fc_map = {"1": 500, "2": 1000, "3": 2000, "4": 5000, "5": 10000}
                if fc_ch in fc_map:
                    amt = fc_map[fc_ch]
                else:
                    bad_inputs += 1
                    print("Invalid option.")
                    continue
            else:
                amt_str = input("Enter amount to withdraw (multiples of 100): ").strip()
                if amt_str.isdigit():
                    amt = int(amt_str)
                else:
                    bad_inputs += 1
                    print("Invalid input format.")
                    continue

            if amt <= 0 or amt % 100 != 0:
                print("Amount must be positive and a multiple of 100.")
            elif u_data["count_today"] >= 5:
                print("Daily limit reached! Maximum 5 withdrawals per day.")
            elif u_data["drawn_today"] + amt > 20000:
                print("Daily withdrawal limit of ₹20,000 exceeded.")
                print("Already drawn today: ₹", u_data["drawn_today"])
            elif u_data["balance"] - amt < 500:
                print("Failed! Minimum balance of ₹500 required.")
            elif amt > atm_cash:
                print("ATM has insufficient cash.")
            else:
                print("\nProcessing transaction...")
                print("Transaction Successful!")

                u_data["balance"] -= amt
                atm_cash -= amt
                u_data["drawn_today"] += amt
                u_data["count_today"] += 1
                total_txns += 1

                if amt >= 5000:
                    u_data["balance"] += 50
                    print("Cashback Earned: ₹50 added to balance!")

                pts = amt // 100
                u_data["rewards"] += pts
                print("Reward points earned:", pts)

                temp_amt = amt
                c500 = temp_amt // 500
                temp_amt %= 500
                c200 = temp_amt // 200
                temp_amt %= 200
                c100 = temp_amt // 100

                print("Currency Notes Dispensed:")
                if c500 > 0:
                    print("  ₹500 x", c500)
                if c200 > 0:
                    print("  ₹200 x", c200)
                if c100 > 0:
                    print("  ₹100 x", c100)

                tid = "TXN" + str(txn_counter)
                txn_counter += 1
                u_data["history"].append("Withdraw ₹" + str(amt))

                rec = input("\nPrint Receipt? (1. Yes / 2. No): ").strip()
                if rec == "1":
                    print("      TRANSACTION RECEIPT     ")
                    print("Transaction ID :", tid)
                    print("Customer Name  :", u_data["name"])
                    print("Amount         : ₹", amt)
                    print("New Balance    : ₹", u_data["balance"])

        elif ch == "3":
            d_str = input("Enter deposit amount: ").strip()
            if d_str.isdigit() and int(d_str) > 0:
                damt = int(d_str)
                u_data["balance"] += damt
                atm_cash += damt
                total_txns += 1
                u_data["history"].append("Deposit ₹" + str(damt))
                print("Successfully deposited ₹", damt)
            else:
                bad_inputs += 1
                print("Invalid deposit amount.")

        elif ch == "4":
            print("\n--- MINI STATEMENT ---")
            print("Customer:", u_data["name"])
            print("Last Transactions:")
            if len(u_data["history"]) == 0:
                print("No transactions yet.")
            else:
                for item in u_data["history"][-5:]:
                    print(" -", item)
            print("Current Balance: ₹", u_data["balance"])

        elif ch == "5":
            old_p = input("Enter current PIN: ").strip()
            if old_p == logged_pin:
                new_p = input("Enter new 4-digit PIN: ").strip()
                if len(new_p) == 4 and new_p.isdigit():
                    if new_p in ["0000", "1111", "1234", "9999"]:
                        print("Weak PIN! Simple sequences are not allowed.")
                    else:
                        conf_p = input("Confirm new PIN: ").strip()
                        if conf_p == new_p:
                            users[new_p] = users.pop(logged_pin)
                            logged_pin = new_p
                            print("PIN updated successfully!")
                        else:
                            print("PIN confirmation mismatched.")
                else:
                    print("PIN must be 4 digits.")
            else:
                bad_inputs += 1
                print("Incorrect current PIN.")

        elif ch == "7":
            g_str = input("Enter monthly savings goal: ").strip()
            if g_str.isdigit():
                goal = int(g_str)
                if u_data["balance"] >= goal:
                    print("Goal Achieved!")
                else:
                    print("Need ₹", goal - u_data["balance"], "more to reach goal.")
            else:
                bad_inputs += 1
                print("Invalid goal amount.")

        elif ch == "8":
            if u_data["balance"] >= 10000:
                print("Eligible for Personal Loan up to ₹50,000!")
            else:
                print("Not eligible. Minimum balance of ₹10,000 required.")

        elif ch == "9":
            print("Thank you for using the ATM!")
            session = False
            running = False
            continue

        else:
            bad_inputs += 1
            print("Invalid choice.")

        if session:
            again = input("\nDo another transaction? (1. Yes / 2. No): ").strip()
            if again != "1":
                print("Thank you for using the ATM!")
                session = False
                running = False

# PART 2: WEEKEND PLANNER & BUDGET

if logged_pin and logged_pin in users:
    u_data = users[logged_pin]
    print("\n" + "="*35)
    print("      WEEKEND PLANNER & BUDGET      ")
    print("="*35)
    b_in = input("Enter your budget: ").strip()

    if b_in.isdigit() or (b_in.startswith("-") and b_in[1:].isdigit()):
        Budget = int(b_in)

        if Budget < 0:
            print("Enter Correct Budget")
        elif Budget > 10000:
            print("Plan a Trip")
        elif Budget > 5000:
            print("Resort Stay")
        elif Budget > 3000:
            print("Movie and Dinner")
        elif Budget > 1000:
            print("Cafe and Shopping")
        elif Budget > 500:
            print("Street Food and Park Visit")
        else:
            print("Stay Home")

        if Budget >= 0:
            b_left = u_data["balance"]
            if Budget > b_left:
                b_used = Budget - b_left
            else:
                b_used = 0

            print("Budget Left: ₹", b_left)
            print("Budget Used: ₹", b_used)

            if b_left < (Budget * 0.2):
                print("Advice: High Spending! Save More.")
            else:
                print("Advice: Excellent Savings!")
    else:
        print("Enter Correct Budget")
