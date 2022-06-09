# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:18:10 2022

@author: sahel
"""
logo = '''
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  

'''

#---------------------------------- 
def BlackJack(): 
    import random
   
    def one_check():
        if 11 in user and sum(user)>21:
            user.remove(11)
            user.append(1)
    def add(x):
        '''this function for adding'''
        summ = 0
        one_check()
        for i in range (0 , len(x)):
            summ +=x[i]
        
        return summ

    def loseruser(x):
        if add(x) > 21:
            print(f"Dealer wins:{cp}")
          
    def losercp(x):
        if add(x) > 21:
            print("You win")
#---------------------------
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    user=[]
    cp =[]
    ending = False
    for i in range(0,2):
        user.append(cards[random.randint(0,12)])
        cp.append(cards[random.randint(0,12)])
    if add(user) ==21:
        print("BlackJack")
        ending = True
    
    print(f"your cards are :\n {user}")
    print(f"the dealer first card is :\n {cp[0]}")
    
    cp_add = cp[0] + cp[1]
    while cp_add <17:
        cp_add += cards[random.randint(0,12)]
        loseruser(user) 

    while ending == False :
     hit = input("do you wish to hit(Y or N) \n")
     if hit == "Y":
             user.append(cards[random.randint(0,12)])
             print(f"your cards are :\n {user}")
             if add(user) > 21:
               print(f"Dealer wins {cp}")
               ending = True
         
     else:
                 if add(user) > 21 or add(cp) >21:
                     losercp(cp)
                     loseruser(user)
                     ending = True
                 elif add(user) > add(cp):
                     print("you win")
                     ending = True
                 elif add(user) < add(cp):
                     print(f"Dealer wins {cp}")
                     ending = True
                 else:
                     print("equal")
                     ending = True
while input("Do you want to play BlackJack (Y N)") == "Y":
    print("\x1B[2J")
    print(logo)
    BlackJack()