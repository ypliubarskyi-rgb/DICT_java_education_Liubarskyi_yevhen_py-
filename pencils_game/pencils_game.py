"""
Гра "Олівці".
Етап 4: другий гравець (Jack) є ботом з виграшною стратегією.
John – користувач, Jack – бот.
"""

import random


def print_pencils(count):
    """
    Друкує на екрані рядок з вертикальних рисок '|' відповідно до кількості олівців.
    """
    print("|" * count)


def ask_initial_pencils():
    """
    Запитує в користувача початкову кількість олівців.
    Повторює запит, поки користувач не введе додатнє ціле число.
    Правила помилок:
    - якщо введення не є числом або від'ємне -> "The number of pencils should be numeric"
    - якщо введено 0 -> "The number of pencils should be positive"
    """
    while True:
        print("How many pencils would you like to use:")
        raw = input()

        try:
            value = int(raw)
        except ValueError:
            print("The number of pencils should be numeric")
            continue

        if value <= 0:
            print("The number of pencils should be positive")
            continue

        return value


def ask_first_player(name1, name2):
    """
    Запитує ім'я першого гравця.
    Повторює запит, доки користувач не введе name1 або name2.
    У випадку помилки виводить:
    "Choose between 'name1' and 'name2'"
    """
    while True:
        print("Who will be the first (" + name1 + ", " + name2 + "):")
        name = input()
        if name == name1 or name == name2:
            return name
        print("Choose between '" + name1 + "' and '" + name2 + "'")


def ask_move(pencils_left):
    """
    Запитує у поточного гравця-людини, скільки олівців він хоче взяти.
    Дозволені значення: 1, 2 або 3.
    Перевірки:
    - якщо введено не '1', '2' або '3' -> "Possible values: '1', '2' or '3'"
    - якщо взяти хочуть більше, ніж залишилось -> "Too many pencils were taken"
    Повертає коректне ціле число (1, 2 або 3).
    """
    while True:
        move_raw = input()

        if move_raw not in ("1", "2", "3"):
            print("Possible values: '1', '2' or '3'")
            continue

        move = int(move_raw)

        if move > pencils_left:
            print("Too many pencils were taken")
            continue

        return move


def bot_move(pencils_left):
    """
    Обчислює хід бота (Jack) згідно з виграшною стратегією.

    Якщо позиція виграшна:
    - 4, 8, 12, ... (pencils % 4 == 0) -> взяти 3
    - 3, 7, 11, ... (pencils % 4 == 3) -> взяти 2
    - 2, 6, 10, ... (pencils % 4 == 2) -> взяти 1

    Якщо позиція програшна (pencils % 4 == 1):
    - бере випадкову кількість олівців від 1 до 3 (але не більше, ніж залишилось).
    """
    if pencils_left == 1:
        return 1

    remainder = pencils_left % 4

    if remainder == 0:
        return 3
    if remainder == 3:
        return 2
    if remainder == 2:
        return 1


    max_take = 3
    if pencils_left < 3:
        max_take = pencils_left
    return random.randint(1, max_take)


def main():
    """
    Головна функція для етапу 4.
    Реалізує гру, де John – людина, Jack – бот із виграшною стратегією.
    Той, хто бере останній олівець, програє.
    """
    name1 = "John"
    name2 = "Jack"

    pencils = ask_initial_pencils()
    current_player = ask_first_player(name1, name2)

    while pencils > 0:
        print_pencils(pencils)

        if current_player == name2:

            print(name2 + "'s turn:")
            move = bot_move(pencils)
            print(move)
        else:

            print(name1 + "'s turn!")
            move = ask_move(pencils)

        pencils -= move

        if pencils == 0:

            if current_player == name1:
                winner = name2
            else:
                winner = name1
            print(winner + " won!")
            break


        if current_player == name1:
            current_player = name2
        else:
            current_player = name1


if __name__ == "__main__":
    main()
