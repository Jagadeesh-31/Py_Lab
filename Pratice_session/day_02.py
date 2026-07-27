price = 5000

seat = input().lower()
days = int(input())
festival = input().lower()
age = int(input())

if seat == "business":
    price += price * 0.40
elif seat == "premium":
    price += price * 0.20

if days > 30:
    price -= price * 0.10
elif days < 7:
    price += price * 0.25

if festival == "yes":
    price += price * 0.20

if age >= 60:
    price -= price * 0.15

print(int(price))
