import random

words_list = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black", "white", "brown"]

def select_random_word(words: list = [None]) -> str:
    return random.choice(words)


def initialize_hidden_word(word: str = None) -> list:
    hidden_word = ["_"] * len(word)
    return hidden_word

def is_valid_letter(word: str, letter: str = None) -> bool:
    if not letter or not isinstance(letter, str) or len(letter) != 1:
        return False
    return letter in word

def display_game_status(letter: str, hidden_word: list, lives: int, guessed_letters: list):
    status_message = (
        f"\n\n Lives: {lives}\n Guessed letters: {guessed_letters}\n Letter guessed: {letter}\n\n Word: {hidden_word}\n\n"
    )
    print("\n------- Hangman Game -------\n")
    print(status_message)

def is_already_guessed(letter: str, guessed_letters: list = [None]) -> bool:
    return letter in guessed_letters

def end_game(lives: int, word: str, guessed_letters: list, victory: bool, total_lives: int) -> None:
    success_message = "\n\n --- Congratulations! You guessed the word!!! ---- \n\n"
    failure_message = "\n\n --- You lost!!! ---- \n\n"

    if victory:
        print(f"{success_message} Word: {word}\n Remaining lives: {lives}/{total_lives}\n Guessed letters: {guessed_letters}\n\n")
    else:
        print(f"{failure_message} Word: {word}\n Remaining lives: {lives}/{total_lives}\n Guessed letters: {guessed_letters}\n\n")

def is_single_alpha_character(letter: str) -> bool:
    return letter.isalpha()

def calculate_initial_lives(word: str) -> int:
    return len(word) // 2

def main():
    word = select_random_word(words_list)

    lives = calculate_initial_lives(word)
    total_lives = lives
    hidden_word = initialize_hidden_word(word)
    correct_guesses = 0

    guessed_letters = []
    victory = False

    while lives > 0:
        if correct_guesses == len(word):
            victory = True
            end_game(lives, word, guessed_letters, victory, total_lives)
            break

        letter = input("Enter a letter: ").strip()

        if not is_single_alpha_character(letter):
            print("Please enter a valid letter.")
            continue

        if is_already_guessed(letter, guessed_letters):
            print("Letter already guessed.")
            continue

        guessed_letters.append(letter)
        
        if is_valid_letter(word, letter):
            correct_guesses += word.count(letter)
            for i in range(len(word)):
                if word[i] == letter:
                    hidden_word[i] = letter
        else:
            lives -= 1

        display_game_status(letter, hidden_word, lives, guessed_letters)

    if lives == 0:
        end_game(lives, word, guessed_letters, victory, total_lives)

    print(" -- End of Game! -- \n")

if __name__ == "__main__":
    main()