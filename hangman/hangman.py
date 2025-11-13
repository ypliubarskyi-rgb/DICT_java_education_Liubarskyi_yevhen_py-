import random

WORDS = ["python", "java", "javascript", "php"]


def play_game():
    secret_word = random.choice(WORDS)
    masked = ["-"] * len(secret_word)
    mistakes_left = 8
    guessed = set()

    while mistakes_left > 0:
        print()
        print("".join(masked))
        letter = input("Input a letter: > ")


        if len(letter) != 1:
            print("You should input a single letter")
            continue

        if not letter.islower() or not letter.isalpha():
            print("Please enter a lowercase English letter")
            continue

        if letter in guessed:
            print("You've already guessed this letter")
            continue

        guessed.add(letter)


        if letter in secret_word:
            improved = False
            for i, ch in enumerate(secret_word):
                if ch == letter and masked[i] == "-":
                    masked[i] = letter
                    improved = True
            if not improved:
                print("No improvements")
                mistakes_left -= 1
        else:
            print("That letter doesn't appear in the word")
            mistakes_left -= 1

        
        if "-" not in masked:
            print()
            print(f"You guessed the word {secret_word}!")
            print("You survived!")
            return

    print("You lost!")


def main():
    print("HANGMAN")
    while True:
        cmd = input('Type "play" to play the game, "exit" to quit: ')
        if cmd == "play":
            play_game()
        elif cmd == "exit":
            break


if __name__ == "__main__":
    main()
