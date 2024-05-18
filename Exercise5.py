# Snake,water,gun is a variation of the childrens game where players use hand gestures to represent 
#a snake, water, or a gun. The gun beats the snake, the water beats the gun, and the
#snake beats the water.
#write a python program to create  a snake water gun game in python using if else statemenrs.
#Do not create any fancy GUI. Use proper functions to check for win.
import random
comp = random.randint(0,2)
user=int(input("0 for snake, 1 for water, 2 for Gun"))

def check(comp, user):
    if comp == user:
        return 0
    elif comp==0 and user == 1:
        return -1
    elif comp==2 and user == 0:
       return -1
    elif comp==1 and user == 2:
       return -1
    else:
       return 1


score = check(comp, user)
print("you:", user)
print("computer: ",comp)
if score == 0:
   print("It is a draw")

elif score == 1:
    print("You win")
else:
   print("You lose")



    

