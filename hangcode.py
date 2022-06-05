# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 16:01:04 2022

@author: Pascal-PC
"""


import random
word_list = ["panda", "zebra","elephant","rabbit","shark","chicken" , "Butterfly","goldfish","spider"]
hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hanglego='''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
         '''
print(hanglego)
print(" guess the word by inputing its letters\n the rules are simple just try to guess the letter\n if you are wrong you will see a draw of a man by continuing being wrong the man will be fully hanged.\n so carefull....")
chosen_word = random.choice(word_list)
lenghy = len(chosen_word)
display= []
for letter in range(0,lenghy):
    display += "_"
print(f"{' '.join(display)}")   
lives = 7
end_of_the_game = False

han =0
while end_of_the_game == False :
     guess = input("enter a letter to play: ").lower()
     
     for letter in range(0,lenghy) :
    
        if chosen_word[letter] == guess:
          display[letter] = guess
     if guess not in display:
          lives = lives - 1 
          
          print(hangman[han])
          han+=1
     print(f"{' '.join(display)}")
       
           
     if "_" not in display:
       end_of_the_game = True
       print("you win")
     if lives == 0:
         end_of_the_game = True
         print("you lose")
         print(chosen_word)
        
           

    