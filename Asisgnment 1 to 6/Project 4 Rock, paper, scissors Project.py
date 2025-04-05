import random
choice = ["rock","paper","scissors"]

while True:
   user_choice = (input("Pick and Choose Rock , Paper , Scissors : ")).lower()

   if user_choice not in choice :
    print("Invalid Choice ! Enter Only Rock, Paper, or Scissors ! ❌")
    continue

   computer_choice = random.choice(choice)
   print(f"Computer Choice is {computer_choice}")

   if user_choice == computer_choice :
    print("Match Draw ! 😐 ")

   elif (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock") :
     print("Wow You Win ! 😎 ")

   else:
    print("Computer Winner ! 😥 ")

   play_again = (input("Do You Want to Play Again ? (Yes/No) : ")).lower()

   if play_again != "yes" :
     print("Thank You For Playing ! ")

     break