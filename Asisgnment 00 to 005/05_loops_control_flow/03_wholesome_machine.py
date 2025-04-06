AFFIRMATION = "You are Doing Great ! Keep It Up !"

def wholesome_machine():
    print(f"Please Type the Following Affirmation {AFFIRMATION}:")

    while True:
     user_input = input()
     if user_input == AFFIRMATION:
         print("Great Job ! You are Doing Amazing !")
         break
     else:
         print("That's Okay! Just keep Trying !")
         
wholesome_machine()