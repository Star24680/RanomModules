import random
playing=True
Number=str(random.randint(10,20))
print("I will generate a number from 10-20 and you have to guess the number(one digit at a time)")
print("The game ends when you get 1 hero")
while playing:
    Guess=input("Give me your best guess ")
    if Number==Guess:
        print("You win the game!!!!!!!")
        print("The number was", Number)
        break
    else:
        print("Your guess is incorrect!Try again")