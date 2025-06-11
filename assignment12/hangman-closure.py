def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        displayed = ""
        for ch in secret_word:
            if ch in guesses:
                displayed += ch
            else:
                displayed += "_"

        print(displayed)

       
        return set(secret_word).issubset(set(guesses))

    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter the secret word: ").strip().lower()
    game = make_hangman(secret_word)

    print("Start guessing letters!")

    while True:
        guess = input("Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter exactly one letter.")
            continue

        completed = game(guess)
        if completed:
            print("Congratulations! You've guessed the word!")
            break
