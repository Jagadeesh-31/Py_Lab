"""
use random module --> Rock,paper,scissor
"""
'''
import random

player1 = input("Enter the choiceRock,paor,scissor").lower()
player2 = random.choice(['Rock','Paper','Scissors']).lower()

if player1 == 'Rock' and player2=='Paper':
    print("Player2 Won")
elif player1 == 'rock' and player2=='scissors':
    print("Player1  Won")
elif player1 == 'paper' and player2=="rock":
    print('Player1 Won')
elif player1 =='paper' and player2=='scissor':
    print('Player2 Won')
elif player1 == 'scissor' and player2=='rock':
    print('Player2 won')
elif player1 == 'scissor' and player2=="paper":
    print("Player1 Won")
elif player1==player2:
    print("It a tie") 
else:
    print("Invalid")


# task --> Build a Game Genaerator sequnece  -->Choice menu
# task 1 -> Rocker paper game
# task 2 -> Stro genarator (random.choice) [when,what,how,who,where]
# task3 --> Otp mail sent
# 4 -- bmi caluclation



'''
# build our own qr code --> pyqrcode 

import pyqrcode,png

link = 'https://www.linkedin.com/in/jagadeesh-boyalla/'
qr = pyqrcode.create(link)
print(qr)
qr.png("myqr.png",scale=15)
print(qr)