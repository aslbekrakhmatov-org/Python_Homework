import random
comp_num = random.randint(1,100)
guesses = 1
answers = ['Y', 'YES', 'y', 'yes', 'ok']
while True:
    if guesses>10:
        print("You lost")
        answer = input("Do you want to play again? ")
        
        if answer in answers:
            guesses = 1    
        else:
            print("Game is over")
            break

    else:        
        human_num = int(input("Enter number between 1 and 100: "))
        guesses+=1
        
        if human_num>comp_num:
            print("Too high!")
        elif human_num<comp_num:
            print("Too low!")
        else:
            print("You guessed it right!")
            break



