from art import logo
from art import vs
from game_data import data
from os import system
import random

'''*************************************[Game-Code]**************************************'''
play_again = True 
while play_again == True:
    true = True 
    your_score = 0
    while true == True:
        print(logo)
        # Display Your score 
        print(f'Your current Score: {your_score}')
        # 1st-pick that wiil be compared with nxt one
        rand_pick = random.choice(data)
        # print 1st-pick 
        print(f"Compare A : {rand_pick['name']}, a {rand_pick['description']} from {rand_pick['country']}.")
        # print VS logo 
        print(vs)
        # 2nd-pick that to be compared with 1st one
        vs_pick = random.choice(data)
        # print 2nd-pick 
        print(f"Compare B : {vs_pick['name']}, a {vs_pick['description']} from {vs_pick['country']}.")
        # compare N make descition
        user_desc = str(input("who's got the more followers? [A/B]  "))
        user_desc_Aa = user_desc.upper()
        while user_desc_Aa not in ['A' , 'B']:
            print('Invalid input!')
            user_desc = str(input("who's got the more followers? [A/B]  "))
            user_desc_Aa = user_desc.upper()

        A = rand_pick['follower_count']
        B = vs_pick['follower_count']
        # print(user_desc_Aa)    
        # print(A)
        # print(B)

        # decide who has more  A OR B
        if B < A and user_desc_Aa == 'A':
            your_score +=1
            system('cls')
        elif B > A and user_desc_Aa == "B":
            your_score +=1
            system('cls')
        else:
            print('Wrong Choice!')
            true = False

    user_inpt = input('Play Again? [y/n]')
    while user_inpt not in ['y' , 'n']:
        print('Invalid input!')
        user_inpt = input('Play Again? [y/n]')

    if user_inpt == 'y':
        pass
    else:
        play_again = False

        
'''**************************************[END]************************************************'''