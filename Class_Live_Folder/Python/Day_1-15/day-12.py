# Nested Conditions --> One codition inside another -->if,else
'''
Syntax:
if codition:
      if codition:
          statments(s)....
      elif codtion2..:
          statments(s)
'''
'''
# Use case :  Atm withdrawel secenario

#check whether card is valid/not --> entered pin is correct or not  ---> check  balac

pin = int(input("Enter a pin:"))
correct_pin =  1888
card_inserted = True
balance = 23000
with_draw = int(input("Enter a amt:"))
if card_inserted:
          if pin == correct_pin:
              if balance >with_draw:
                  print(f"Trasction is completed Sucessfully, New Balance:{balance-with_draw} ")
              elif balance <=0:
                  print("You have low balance,&  Add more Balance")
              else:
                  print("Tranction failed, please  maintain minimum balance")

          else:
              print("Pin is invalid")
else:
    print("You have  Account is Deactived")







'''

# weekwnd plan trip

Budget = int(input())
if Budget > 500:
   if Budget>10000:
             print("Plan a trip")
   elif Budget > 5000:
        print("Resort Stay")
   elif Budget >3000:
        print("Movie and Dinner")
   elif Budget >1000:
       print("Cafe and Shopping")
   elif Budget >500:
       print("Street Food and Park Vist")
       print("Enter Correct Budget")
elif Budget < 0:
    print("Enter Correct Budget")
else:
    print("Stay Home")
      


