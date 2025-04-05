import random

words_list = ["computer", "python", "disneyland", "programming", "kingston"]

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def hangman():
    word = random.choice(words_list)
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        print("Welcome to Hangman!")
        print(f"Word: {display_word(word, guessed_letters)}")
        guessed_letters_str = " ".join(guessed_letters)
        print(f"Guessed Letters: {guessed_letters_str}")
        print(f"Attempts Left: {attempts}")


        guess = input("Enter a letter: ").lower()
        guessed_letters.add(guess)

        if guess in word:
            print("Wow! Correct Guess 😎")
        else:
            print("Wrong Guess 😥")
            attempts -= 1

        if "_" not in display_word(word, guessed_letters):
            print(f"Congrats! 👋 You Guess the right word: {word}")
            break

    if attempts == 0:
        print(f"Sorry, You Ran Out of Attempts. The Word Was: {word}")

hangman()