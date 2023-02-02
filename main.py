import random

f = open("Words.txt", "r")
x = f.readlines()

word1 = random.choice(x).strip().lower()

f.close()


def hangman(word):
    a = 0
    guessed_letters = []
    attempts = 5
    w = []  # modification
    vowels = ["a", "e", "i", "o", "u"]
    print("Let's start playing Hangman! You have 5 attempts to guess the word.")
    for y in word:
        w.append(y)
    while a < len(w):
        if w[a] not in vowels:
            w[a] = "_"
        a += 1
    z = 0
    print(" ".join(w))  # modification
    while attempts > 0:
        if "_" not in w:
            print("Bravo! You guessed the word.")
            print("The word was", " ".join(w))
            print("Guessed", " ".join(w), "with", 6 - attempts, "attempts left.")  # modification
            break
        guess = input("Enter a letter: ").lower()
        if guess.isalpha() and guess not in guessed_letters:
            if guess not in vowels:
                if guess in word:
                    print("Excellent!", guess, "is in the word.")
                    guessed_letters.append(guess)
                    while z < len(word):
                        if word[z] == guess:
                            w[z] = guess
                        z += 1
                    if "_" in w:
                        print(" ".join(w))  # modification
                    z = 0
                elif guess not in word:
                    attempts -= 1
                    print("Oops!", guess, "is not in word, try again!\nYou have", attempts, "attempt(s) left.")
                    guessed_letters.append(guess)
            else:
                print("Vowels are already given in the word.")
        elif guess in guessed_letters:
            print("You have already guessed this letter.")
        else:
            print("Not a valid guess. Try again!")

    if attempts == 0:
        print("Game over! Better luck next time.")
        print("The word was", word)


hangman(word1)