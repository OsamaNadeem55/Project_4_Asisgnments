import random

def guess_game():
    print("Guess My Number")
    computer_gen = random.randint(0,10)

    while True:
     my_guess = int(input("I am Thinking a Number Between (0 to 20) Enter a Guess: "))
     if my_guess == computer_gen:
         print(f"Congrats! 😎 The Number Was : {my_guess} ")
         break
     elif my_guess > computer_gen:
         print("Your Guess is Big")
     elif my_guess < computer_gen:
         print("Your Guess is Small")
         

guess_game()