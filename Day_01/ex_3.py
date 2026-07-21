# 3. Season Identifier

month = int(input("Enter month number: "))

if month > 1 or month > 12:
    if month == 12 or month == 1 or month == 2:
        print("Season: Winter")
    elif month == 3 or month == 4 or month == 5:
        print("Season: Spring")
    elif month == 6 or month == 7 or month == 8:
        print("Season: Summer")
    else:
        print("Season: Autumn")
else:
    print("Invalid month entered")
