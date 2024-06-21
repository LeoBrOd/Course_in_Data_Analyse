import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive',
             'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)


def display_hangman(wrong_guesses):
    stages = [
        """
          --------
          |      |
          |
          |
          |
          |
          |
          -------
      """,
        """
          --------
          |      |
          |      O
          |
          |
          |
          |
          -------
      """,
        """
          --------
          |      |
          |      O
          |      
          |
          |
          |
          -------
      """,
        """
          --------
          |      |
          |      O
          |      |
          |
          |
          |
          -------
      """,
        """
          --------
          |      |
          |      O
          |     /|
          |
          |
          |
          -------
      """,
        """
          --------
          |      |  
          |      O  
          |     /|\ |
          |         
          |        
          |
          -------
      """,
        """
          --------
          |      |
          |      O
          |     /|\ |
          |     / \ |
          |
          |
          -------
      """
    ]
    print(stages[wrong_guesses])


def play_hangman():
    secret_word = word.lower()
    word_chars = list(secret_word)
    guessed_letters = set()
    wrong_guesses = 0

    word_display = ["_" for _ in word_chars]

    while wrong_guesses < 6 and "_" in word_display:
        print(" ".join(word_display))
        print(f"You have {6 - wrong_guesses} guesses left.")

        while True:
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
            elif guess in guessed_letters:
                print("You already guessed that letter. Try again.")
            else:
                break
        guessed_letters.add(guess)

        if guess in word_chars:

            for i in range(len(word_chars)):
                if word_chars[i] == guess:
                    word_display[i] = guess
        else:
            wrong_guesses += 1
            display_hangman(wrong_guesses)

    if "_" not in word_display:
        print(f"You won! The word was {''.join(word_chars)}.")
    else:
        print(f"You lost! The word was {''.join(word_chars)}.")


play_hangman()
