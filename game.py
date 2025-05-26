"""
WORKFLOW OF PROJECT
1 - input from user(Rock,paper,scissor)
2 - computer choice(computer will choose randomly not conditionlly)
3 - Result print

cases:
A - Rock
Rock - Rock = tie
Rock - paper = paper win
Rock - scissor = Rock win

B - paper
paper - paper = tie
paper - Rock = Paper win
paper - scissor = scissor win

C - Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = scissor win

"""

import random 
item_list=["Rock","Paper","Scissor",]

user_choice = input("Enter your move = Rock , paper, scissor=")
comp_choice = random.choice(item_list)

print(f"user chouice = {user_choice}, computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: =match Tie")

elif user_choice == "Rock":
    if comp_choice == "paper":
        print("paper covers Rock = computer win")
    else:
        print("Rock smashes scissor = you win")

elif user_choice == "paper":
    if comp_choice =="scissor":
        print("scissor cuts papper, computer win")
    else:
        print("paper covers rock, you win")

elif user_choice == "scissor":
    if comp_choice == "paper":
        print("scissor cuts paper, you win")
    else:
         print("Rock smashes scissor, computer win")               