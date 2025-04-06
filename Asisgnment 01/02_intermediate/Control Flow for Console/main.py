import random

Num_Rounds = 5
def highe_low_game():

    score = 0
    print("Welcome to the High-Low Game !")
    print("-"*20)
    
    for round_nums in range(1,Num_Rounds + 1):
        print(f"Round {round_nums}")
        user_num = random.randint(1,100)
        computer_num = random.randint(1,100)
        print(f"You Number is {user_num}")
        
        while True:
          user_guess = input("Do You Think Your Number is Higher or Lower Than the Computer ? (higher/lower) : ").strip().lower()
          if user_guess in ["higher","lower"]:
              break
          else:
              print("Please Enter Either 'Higher' or 'Lower'")
              
        if (user_guess == "higher" and user_num > computer_num) or (user_guess == "lower" and user_num < computer_num):
            print(f"You were Right ! The computer Number Was {computer_num}")
            score += 1
        else:
            print(f"Oho, That's Incorrect. The Computer Number Was {computer_num}")      
        print(f"Your Score is Now {score}")
    print("Thanks for Playing !")
    
    if score == Num_Rounds:
        print("Wow! You played Perfectly 🎉")
    elif score >= Num_Rounds //2:
        print("Good job, You Played Really Well 👍")
    else:
        print("Better Luck Next Time 😢")

highe_low_game()