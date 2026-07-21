# Nested Conditions Example

# ATM Withdrawal Scenario

pin = int(input("Enter a PIN: "))
correct_pin = 1888
card_inserted = True
balance = 23000
withdraw = int(input("Enter withdrawal amount: "))
if card_inserted:
     if pin == correct_pin:
         if balance > withdraw:
             print(f"Transaction Successful. New Balance: {balance - withdraw}")
         elif balance <= 0:
             print("Insufficient Balance. Please add money.")
         else:
            print("Transaction Failed. Maintain minimum balance.")
     else:
         print("Invalid PIN")
else:
     print("Account is Deactivated")
