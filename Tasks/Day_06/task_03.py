accounts = {}
max_attempts = 3
logged_pin = None

print("SMART ATM SYSTEM")

print("\nfirst lets create some accounts")

try:
    n = input("how many accounts you want to create? ")
    n = int(n)
    if n <= 0:
        raise ValueError("need atleast 1 account")
except ValueError:
    print("that wasnt valid, taking 1 account by default")
    n = 1

for i in range(1, n+1):
    print("\ncreating account", i, "of", n)
    while True:
        try:
            name = input("Name: ").strip()
            if name == "":
                raise ValueError("name cant be blank")

            pin = input("Set a 4 digit pin: ").strip()
            if len(pin) != 4 or not pin.isdigit():
                raise ValueError("pin has to be 4 digits")
            if pin in accounts:
                raise ValueError("pin already taken, pick another")

            bal = input("opening balance: ").strip()
            bal = int(bal)
            if bal < 0:
                raise ValueError("balance cant be negative")

            accounts[pin] = {
                "name": name,
                "balance": bal,
                "history": []
            }
            print("account created for", name)
            break
        except ValueError as e:
            print("error:", e, "- try again")

print("\nall done, now login with your pin")

# pin check
tries = 0
while tries < max_attempts:
    try:
        pin = input("\nEnter PIN: ").strip()
        if len(pin) != 4 or not pin.isdigit():
            raise ValueError("pin should be 4 digits")

        if pin not in accounts:
            raise KeyError("no account with this pin")

        acc = accounts[pin]
        logged_pin = pin
        print("welcome", acc["name"])
        break

    except ValueError as e:
        tries += 1
        print("error:", e, "|", max_attempts - tries, "tries left")
    except KeyError as e:
        tries += 1
        print("error:", e, "|", max_attempts - tries, "tries left")

    if tries == max_attempts:
        print("too many wrong tries, blocked for now")

if logged_pin is None:
    print("could not log in")
else:
    acc = accounts[logged_pin]
    active = True

    while active:
        print("\n---- MENU ----")
        print("1 Check balance")
        print("2 Withdraw")
        print("3 Deposit")
        print("4 History")
        print("5 Avg transaction")
        print("6 Exit")

        try:
            ch = input("choice: ").strip()

            if ch == "1":
                print("balance:", acc["balance"])

            elif ch == "2":
                amt = int(input("amount to withdraw: "))
                if amt <= 0:
                    raise ValueError("enter positive amount")
                elif amt > acc["balance"]:
                    print("not enough balance")
                else:
                    acc["balance"] -= amt
                    acc["history"].append(("withdraw", amt))
                    print("done, new balance:", acc["balance"])

            elif ch == "3":
                amt = int(input("amount to deposit: "))
                if amt <= 0:
                    raise ValueError("enter positive amount")
                else:
                    acc["balance"] += amt
                    acc["history"].append(("deposit", amt))
                    print("done, new balance:", acc["balance"])

            elif ch == "4":
                if not acc["history"]:
                    print("no transactions yet")
                else:
                    for t, a in acc["history"]:
                        print(t, "-", a)

            elif ch == "5":
                try:
                    total = sum(a for _, a in acc["history"])
                    avg = total / len(acc["history"])
                    print("average:", round(avg, 2))
                except ZeroDivisionError:
                    print("no transactions to average")

            elif ch == "6":
                print("bye, thanks for using the atm")
                active = False

            else:
                print("invalid option")

        except ValueError as e:
            print("bad input:", e)
        except Exception as e:
            print("something went wrong:", e)

# weekend planner thing
if logged_pin is not None:
    acc = accounts[logged_pin]
    print("\n----- weekend planner -----")

    try:
        budget = int(input("enter your budget: "))

        if budget < 0:
            print("enter a proper budget")
        else:
            if budget > 10000:
                print("plan a trip")
            elif budget > 5000:
                print("resort stay")
            elif budget > 3000:
                print("movie and dinner")
            elif budget > 1000:
                print("cafe and shopping")
            elif budget > 500:
                print("street food and park")
            else:
                print("just stay home")

            left = acc["balance"]
            used = budget - left if budget > left else 0
            print("balance left:", left)
            print("budget used:", used)

            try:
                ratio = left / budget
                if ratio < 0.2:
                    print("spending too much, save more")
                else:
                    print("good savings")
            except ZeroDivisionError:
                print("budget was 0, nothing to check")

    except ValueError:
        print("enter a proper number for budget")
