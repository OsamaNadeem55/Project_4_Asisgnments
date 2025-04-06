PROMPT = "What Do You Want ? "
JOKE: str = "Here is a Joke for You ! Ramsha is Heading Out to the Grocery Store. A Programmer Tell Her : Get a Liter of Milk, and If They have Eggs, Get 12. Ramsha Returns with 13 Liters of Milk. The Programmer Asks Why and Ramsha Replies : 'Because They Had Eggs' "
SORRY =  "Sorry I Only Tell jokes."
def joke_bot():
    print("Welcome to the Joke Bot !")
    user_input = input(PROMPT).lower()
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)
    print("Good Bye !")
    
joke_bot()