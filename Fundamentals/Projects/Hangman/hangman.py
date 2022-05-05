import random
import string 
from words import words





def pick_valid_word():
    valid_word = random.choice(words)

    if "-" in valid_word or " " in valid_word or len(valid_word) < 3:
        valid_word = random.choice(words)
    return valid_word.upper()


def hangman():
    word = pick_valid_word()
    word_letters = set(word)
    alphabet = set(string.ascii_letters.upper())
    used_letters = set()
    lives = 6 


    while len(word_letters) > 0 and lives > 0:
        if len(used_letters) > 0:
            print(f"You have {lives} lives left")
            print("The letters you have guessed are", " ".join(used_letters))


            show_word = [letter if letter in used_letters else "_" for letter in word]
            print("Current word", "".join(show_word))
         
        user_choice = input("Please pick a letter\n").upper()

        if user_choice in alphabet and user_choice not in used_letters:
            used_letters.add(user_choice)
            if user_choice in word_letters:
                word_letters.remove(user_choice)
            elif user_choice not in word_letters:
                lives = lives - 1
        else:
            print("Invalid characters")
    if lives == 0:
        print("Sorry, You ran out of lives...The word was", word)
    else:
        print("Congratulations! You got the word", "".join(word))
    


hangman()


#while lives and number of letters uncovered of the word is above zero hangman continues
#ask player to choose a letter
#if letter is part of the word then add it to the used_letters list 
#if letter is not a part of the word then add it to the used letters list and reduce a life
#if letter is invalid then return a message stating it is invalid



