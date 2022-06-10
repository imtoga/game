
import random
logo ='''
                        _   _                         _             
  __ _ _  _ ___ ______ | |_| |_  ___   _ _ _  _ _ __ | |__  ___ _ _ 
 / _` | || / -_|_-<_-< |  _| ' \/ -_) | ' \ || | '  \| '_ \/ -_) '_|
 \__, |\_,_\___/__/__/  \__|_||_\___| |_||_\_,_|_|_|_|_.__/\___|_|  
 |___/                                                              
'''
cp = random.randint(1, 100)
level = {
    "easy" : 10,
    "hard" :  5, 
    }
print(logo)
print("welcome to -the Guess the number- name\nguess a number between 1,100")
user_level = input("choose the difficulty type:(easy or hard)")
end_game = False
win = "False"
#-------------------------------------------
def com(x):
    if x > cp :
        print("Too high")
    else:
        print("Too low")
        
def win(x):
    if x == cp:
        return 0
#---------------------------------------------
if user_level == "easy":
    print("You have 10 attempts remaining to guess the number")
else:
    print("You have 5 attempts remaining to guess the number")
    
ii =  level[user_level]  

while end_game == False and ii> 0:
     ii -=1
     num = int(input("make a guess:\n"))
     if win(num) == 0:
        print("you win")
        win = "True"
        end_game = True
     else:
        com(num)
if win != "True":
   print(f"you lose\nthe answer was:{cp}")        