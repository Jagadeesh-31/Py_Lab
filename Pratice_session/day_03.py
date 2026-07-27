'''base_pre = 10000

age = int(input("Enter age: "))
health_score = int(input("Enter health score: "))
vehicle_type = input("Enter vehicle type: ").lower()

amt = base_pre

if age < 25:
    amt += base_pre * 0.20
elif age < 50:
    amt += base_pre * 0.15

if health_score >= 80:
    amt -= base_pre * 0.10
else:
    amt += base_pre * 0.20

# Vehicle-based premium
if vehicle_type == "sports":
    amt += base_pre * 0.30
elif vehicle_type == "suv":
    amt += base_pre * 0.15
else:
    print("Invalid vehicle type")
    exit()

print(int(amt))
'''
'''
credit = int(input())
income = int(input())
lbs = int(input())
if credit >= 750:
    print("Eligible")
elif credit > 650 and credit <750:
    print("Condition apply")
elif credit < 650:
    print("Not Eligibile")
if income <= 50000:
    print("Eiligible")
else:
        print(" Not Eiligible")

if lib <=2000:
        print("Eiligible")
else :
        print(" Not Eiligible")

if credit and income and loan_:
    print("Approved")
else:
    print("Failed")
    
'''

credit = int(input())     
income = int(input())
lbs = int(input())

if credit >= 750 and income >= 50000 and lbs <= 20000:
    print("Approved")

elif 650 <= credit < 750 and income >= 50000 and lbs <= 20000:
    print("Condition Apply")

else:
    print("Failed")
