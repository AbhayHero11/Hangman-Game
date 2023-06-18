import random

def hangman():
    words= ['apple', 'banana', 'carrot', 'dragon', 'elephant']

    word = random.choice(words)
    guessed_letters = []
    max_attempts = 6
    attempts = 0

    while True:
        hidden_word = ''
        for letter in word:
            if letter in guessed_letters:
                hidden_word += letter
            else:
                hidden_word += '_ '
            
            print("\n" + hidden_word)

            if hidden_word == word:
                print("Congrats!! YOu got the right word.")
                break
            if attempts>= max_attempts:
                print("\\nSorry, you ran out of attempts. The word was:", word)

            guess = input("Guess a letter: ").lower()

            if guess.isalpha() and len(guess)== 1:
                if guess in guessed_letters:
                    print("You've already guessed that letter. Try again.")

                else:
                    guessed_letters.append(guess)
                    if guess not in word:
                        attempts += 1
                        print("Incorrect guess. Attempts remaining:", max_attempts - attempts)
            else:
                print("Invalid guess. Please enter a single letter.")

hangman()