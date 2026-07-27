# electricity bill

units = int(input())
sr_citizen = input().lower()=="senior"

if  0 < units <=100:
        base_amt = units * 1.5
elif 100 < units <= 200:
        base_amt = units * 2.5
elif 200 <units <= 500:
        base_amt = units * 4
elif 500 < units <= 800:
        base_amt = units * 6
else:
        base_amt = units * 6 * 1.05

if sr_citizen :
    base_amt *=0.9
print(int(base_amt))


