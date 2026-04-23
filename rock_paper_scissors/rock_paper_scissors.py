import random
from abc import ABC, abstractmethod


class RockPaperScissors(ABC):
    """
            Ініціалізує гру з динамічним набором варіантів та генерує правила.
    """
    def __init__(self, options):
        self.options = options
        self.rules = self._generate_rules(options)

    def _generate_rules(self, options):
        """
                Математично вираховує, хто кого перемагає, базуючись на позиціях у списку.
                Використовує алгоритм 'половини' для створення збалансованого ігрового циклу.
        """
        rules = {}
        n = len(options)
        for i in range(n):

            current = options[i]
            reordered = options[i + 1:] + options[:i]

            half = len(reordered) // 2
            winning_against_current = reordered[:half]
            rules[current] = winning_against_current
        return rules

    @abstractmethod
    def get_bot_move(self):
        pass


class DynamicBot(RockPaperScissors):
    def get_bot_move(self):
        return random.choice(self.options)


class Game:
    """
            Ініціалізує ігровий процес з вибраним ботом та початковим рейтингом гравця.
            Встановлює стан гри на очікування введення користувача.
    """
    def __init__(self, bot: RockPaperScissors, score: int):
        self.bot = bot
        self.score = score

    def get_safe_input(self, prompt=""):
        while True:
            user_input = input(prompt).strip()
            if user_input == "!exit":
                print("Bye!")
                exit()
            elif user_input == "!rating":
                print(f"Your rating: {self.score}")
                continue

            if user_input in self.bot.options:
                return user_input
            else:
                print("Invalid input")

    def run(self):
        user_move = self.get_safe_input("> ")
        bot_move = self.bot.get_bot_move()

        if user_move == bot_move:
            print(f"There is a draw ({bot_move})")
            self.score += 50
        elif bot_move in self.bot.rules[user_move]:

            print(f"Sorry, but the computer chose {bot_move}")
        else:

            print(f"Well done. The computer chose {bot_move} and failed")
            self.score += 100


def main():

    name = input("Enter your name: ")
    print(f"Hello, {name}\nWelcome to Rock Paper Scissors")
    print("select game type\n-1 simple game (rock, paper, scissors)\n-2 custom game")



    user_score = 0
    try:
        with open("rating.txt", "r", encoding="utf-8") as file:
            for line in file:
                parts = line.split()
                if parts and parts[0] == name:
                    user_score = int(parts[1])
                    break
    except FileNotFoundError:
        pass

    options = ["rock", "paper", "scissors"]
    choice = input().strip()


    if choice == "2":
        print("Enter options separated by comma (rock,gun,lightning,devil,dragon):")
        raw_input = input().strip()
        if raw_input:
            options = list(map(lambda x: x.strip(), raw_input.split(",")))

    elif choice == "1":
        print("Standard game selected.")
    else:
        print("Unknown command. Loading standard game by default.")

    print("Okay, let's start(exit = !exit, rating = !rating)")


    bot = DynamicBot(options)
    game = Game(bot, user_score)

    while True:
        game.run()


if __name__ == '__main__':
    main()