salary =int(input())
rate =int(input())
exp =int(input())
att = int(input())
amt = 0
if rate > 0:
          if rate == 5:
             amt += salary * 0.25
          elif rate ==4:
              amt+=salary*0.15
          elif rate == 3:
              amt+=salary *0.10
else:
    print("Invalid")

if exp >0:
    if exp >10:
        amt+= salary * 0.10
    elif 5 <= exp <= 10:
            amt+= salary*0.05
else:
    print("Invalid")
if att >0:
    if att >= 95:
        amt+=5000
    elif 85 <= att <= 94:
        amt+=2000
else:
    print("Invalid")
print(int(amt))
 
