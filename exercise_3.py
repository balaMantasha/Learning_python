# -*- coding: utf-8 -*-
"""Exercise 3

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rco1t0BNRyY4fLso2wDMtKcuvPSTP9SL
"""

a = input("Do You want to play the game?")
if (a=="Yes"):
  print("Q1:What is the Capital of India?")
  print("Option 1:Delhi","Option 2:Mumbai", "Option 3:Kolkata", "Option 4: J&K")
  b = input("Write your answer here?")
  if (b=="Delhi"):
    print("This is the correct answer. Youv'e won 5000 Rupees.")
    c = input("Would you like to continue with the game?")
    if (c=="Yes"):
      print("Q2:Compressive strength of concrete is measured in?")
      print("Option 1:Newtons","Option 2:MPa", "Option 3:Km", "Option 4: Kelvin" )
      d = input("Write your answer here?")
      if (d=="MPa"):
       print("This the correct answer. Youv'e won 10000 Rupees.")
       c = input("Would you like to continue with the game?")
       if (c=="Yes"):
        print("Q2:Is it Sunny today?")
        print("Option 1:Yes","Option 2:No", "Option 3:Maybe", "Option 4: Maybe not" )
        e = input("Write your answer here?")
        if (e=="Yes"):
         print("This the correct answer. Youv'e won 20,000 Rs.")
        else:
          print("This is a wrong answer.")
      else:
       print("This is a wrong answer")
    else:
      print("Thank you for playing")
  else:
   print("This is a wrong answer")
else:
  print("You can play whenever you're ready.")

print("Let's play the Game!!!")
questions =["1.Who is the PM of India?" , " 2.What is the national game of India?" , " 3.What is the Capital of India?"]
options=["a.Narendra Modi" "b.Rahul Gandhi" "c.Arvind Kejriwal" "d.Amit Shah" , "a.Hockey" "b.Cricket" "c.Rubgy" "d.Chess" , "a.Mumbai " "b.New Delhi " "c.Pune " "d.Punjab "]
correct_options=["a" , "a" ,"b" ]
prize_money =[1000 , 10000,25000]
Prize_earned =0
for i in range(0,len(questions)):
  print(questions[i])
  print(options[i])
  print(prize_money[i])
  user_input=input("Enter the correct option: ")
  if(user_input == correct_options[i]):
    print("You entered the correct option")
    Prize_earned = Prize_earned + prize_money[i]
  else:
    print("You entered the wrong option and have lost the game!!!")
    break
print(Prize_earned)