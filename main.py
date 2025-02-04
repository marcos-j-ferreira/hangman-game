import random 

word_list: list = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white", "brown"]

def choose_word(words: list = [None]) -> list:
    return random.choice(words)

def initialize_word(word: str = None) -> list:
    hidden_word: list = []
    word_length: int = len(word) 

    for i in range(word_length):
        hidden_word.append("_")

    return hidden_word

def validate_letter_in_word(word, letter: str = None):

    if letter is None:
        return False
    
    if type(letter) is not str:
        return False
    
    if len(letter) != 1:
        return False
    
    for i in range(len(word)):
        if letter == word[i]:
            return True
        
    return False

def display_game_status(letter, hidden_word, lives, guessed_letters):

    status: str = f"\n\n Lives: {lives}\n Guessed letters: {guessed_letters}\n Entered letter: {letter}\n\n Word: {hidden_word}\n\n"
    print(" \n------- Hangman Game ------- \n")
    print(status)

def letter_already_guessed(letter: str, guessed_letters: list = [None]) -> bool:

    for guessed_letter in guessed_letters:
        if letter == guessed_letter:
            return True
    
    return False

def end_game(lives, word, guessed_letters, win, total_lives) -> None:

    win_message: str = "\n\n --- Congratulations you won!!! ---- \n\n"
    lose_message: str = "\n\n --- You lost!!! ---- \n\n"

    if win == 1:
        print(f"{win_message} Word: {word}\n Remaining lives: {lives}/{total_lives}\n Guessed letters: {guessed_letters}\n\n") 
    else:
        print(f"{lose_message} Word: {word}\n Remaining lives: {lives}/{total_lives}\n Guessed letters: {guessed_letters}\n\n")

def is_valid_letter(letter: str) -> bool:

    if letter.isalpha():
        return True
    return False

def calculate_lives(word: str):

    return len(word) // 2

def main():

    word = choose_word(word_list)

    lives: int = calculate_lives(word)
    total_lives = lives
    hidden_word = initialize_word(word)
    correct_guesses: int = 0

    guessed_letters: list = []

    win: int = 0

    while lives > 0:

        if correct_guesses == len(word):
            win += 1
            end_game(lives, word, guessed_letters, win, total_lives) 
            break

        letter: str = str(input("Enter a letter: "))

        is_valid = is_valid_letter(letter)

        if not is_valid:
            print("Enter a letter")
            continue

        is_in_word = validate_letter_in_word(word, letter)

        already_guessed = letter_already_guessed(letter, guessed_letters)

        if already_guessed:
            print("Letter already guessed")
            continue
        guessed_letters.append(letter)

        if is_in_word:
            correct_guesses += 1

            for i in range(len(hidden_word)):
                if word[i] == letter:
                    hidden_word[i] = letter
            
        if not is_in_word:
            lives -= 1

        display_game_status(letter, hidden_word, lives, guessed_letters)
    
    if lives == 0:
        end_game(lives, word, guessed_letters, win, total_lives)

    print(" -- Game Over! -- \n")

main()
