import random

print("The Computer has Thought One Secret Number! 🤔 Now Guess It !")
secret_number = random.randint(1, 20)

try:
    while True:
        user_input = int(input("Enter Your Guess (Between 1 and 20):"))

        if user_input == secret_number:
            print("Wow! Your Guess is Right! 😄")
            print("Thanks For Playing !")

            break
        elif user_input < secret_number:
            print("Think Big Number!")

        elif user_input > secret_number:
            print("Think Small Number!")

except ValueError:
    print("Invalid Input ! (Only Type Number)")