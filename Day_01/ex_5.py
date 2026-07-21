# Weekend Plan Based on Budget using Nested If

Budget = int(input("Enter your budget: "))

if Budget > 0:
    if Budget > 10000:
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
else:
    print("Enter Correct Budget")
