import random

secrate = random.randint(0,10)
print("Guess My Number")
print("I am Thinking  Number Between (0 and 10)")
user_guess = int(input("Enter a Guess : "))

while True:
    if user_guess > secrate:
        print("Your Guess is Big")
    elif user_guess < secrate:
        print("Your Guess is Small")
    elif user_guess == secrate:
        print(f"Congrats! 😊 The Number Was : {user_guess}")
        break
    user_guess = int(input("Enter a Number : "))