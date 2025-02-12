import random
choices = ['rock', 'paper', 'scissors']
comp_choice = random.choice(choices)
r = "rock"
p = "paper"
s = "scissors"
comp_score = 0
human_score = 0
while True:
    if human_score==5:
        print("You won the game!")
        break
    elif comp_score==5:
        print("You lost the game!")
        break

    human_choice = input("Rock/paper/scissors: ").lower()
    comp_choice = random.choice(choices)

    if human_choice==comp_choice:
        print("Draw!")
    elif (human_choice==r and comp_choice==s) or (human_choice==p and comp_choice==r) or (human_choice==s and comp_choice==p):
        print("You win!")
        human_score+=1
    elif (human_choice==s and comp_choice==r) or (human_choice==r and comp_choice==p) or (human_choice==p and comp_choice==s):
        print("You lose!")
        comp_score+=1