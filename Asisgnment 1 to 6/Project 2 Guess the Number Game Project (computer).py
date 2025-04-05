import random
print("Guess The Secret Number 1 to 20 Range !")

user_input = int(input("Enter Secret Guess Number(Computer Guess The Number):"))
computer_num = random.randint(1,10)
print(f"Computer First Guess :{computer_num}")

while True :
   feedback = input("Is This Guess Correct ? (Big/Small/Correct) :")
   if feedback == "Correct":
    print("Wow ! Computer Guess Correct Value ! ")
    break
   elif feedback == "Small":
    print("Guess Digit Small")

   elif feedback == "Big":
    print("Guess Digit Big")

   else:
    print("Invalid Input ! (Only type Big, Small, Correct)")

    continue

   computer_num = random.randint(1,10)
   print(f"Computer New Guess :{computer_num}")