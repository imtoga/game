# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 21:04:53 2022

@author: Pascal-PC
"""

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
  ''' 
paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)       
  '''
print("welcome to the rock,paper,scissors game\n")
game = [rock , scissors, paper]
user = input("choose one between rock, scissors and paper:\n")

if user == "rock":
    print(rock)
elif user == "paper":
    print(paper)
else:
    print(scissors)
    
cp = random.randint(0, 2)
print(game[cp])

if user == "rock":
    if game[cp] == scissors:
        print("you won")
    else:
        print("you lose")
elif user == "paper":
    if game[cp] == rock:
        print("you win")
    else:
        print("you lose")
elif user == "scissors":
    if game[cp] == paper:
        print("you win")
    else:
        print("you lose")
        
