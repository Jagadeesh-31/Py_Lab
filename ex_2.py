# Even-Odd Checker

num = int(input("Enter a number: "))

if num < 0:
    if num % 2 == 0:
        print("Negative Even Number")
    else:
        print("Negative Odd Number")

elif num > 0:
    if num % 2 == 0:
        print("Positive Even Number")
    else:
        print("Positive Odd Number")

else:
    print("Zero is neither even nor odd")
