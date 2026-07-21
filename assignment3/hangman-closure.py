def make_hangman(secret_word):
    guesses = set()

    def hangman_closure(letter):
        guesses.add(letter.lower())

        guessed_word = "".join(
            char if char.lower() in guesses or not char.isalpha() else "_" 
        for char in secret_word
        )

        print(guessed_word)

        return guessed_word == secret_word
    
    return hangman_closure


if __name__ == "__main__":
    secret_word = input("Enter secret word:")
    hangman = make_hangman(secret_word)
    while True:
        user_letter = input("Please guess a letter:")
        if len(user_letter) != 1 or not user_letter.isalpha():
            print("Invalid iput! Please enter a single letter")
            continue

        if hangman(user_letter):
            print("Congratulaitons, you guessed it!")
            break