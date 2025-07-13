import random

# Predefined list of 5 words
words = ["apple", "table", "chair", "house", "plant"]

# Choose a random word from the list
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display hidden word with underscores
def display_word():
    displayed = ""
    for letter in secret_word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "
    return displayed.strip()

print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time.")
print("You have", max_guesses, "wrong guesses.\n")

# Game loop
while incorrect_guesses < max_guesses:
    print("Word: ", display_word())
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print(" Please enter one valid letter.\n")
        continue

    if guess in guessed_letters:
        print(" You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print(" Good guess!\n")
    else:
        incorrect_guesses += 1
        print(" Wrong guess! You have", max_guesses - incorrect_guesses, "tries left.\n")

    # Check for win
    if all(letter in guessed_letters for letter in secret_word):
        print(" Congratulations! You guessed the word:", secret_word)
        break
else:
    print(" Game Over! The word was:", secret_word)