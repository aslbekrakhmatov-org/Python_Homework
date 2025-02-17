import random
comp_num = random.randint(1,100)

answers = ['Y', 'YES', 'y', 'yes', 'ok']

while True:
    for x in range(10):
        human_num = int(input("Enter number between 1 and 100: "))
        
        if human_num>comp_num:
            print("Too high!")
        elif human_num<comp_num:
            print("Too low!")
        else:
            print("You guessed it right!")
            break
    print("You are lost. Do you want to play again? ")
    answer = input()
    if answer not in answers:
        break
