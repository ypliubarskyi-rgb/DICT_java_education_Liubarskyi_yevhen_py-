import random


def get_number_of_friends():
    """
    Запитує у користувача кількість друзів, що приєднуються до вечірки.

    Повертає:
        int або None: кількість друзів, або None у разі некоректного вводу.
    """
    print("Enter the number of friends joining (including you):")
    try:
        num_friends = int(input())
    except ValueError:
        return None
    return num_friends


def get_friends_dict(num_friends):
    """
    Створює словник з іменами всіх учасників вечірки.

    Аргументи:
        num_friends (int): кількість людей, чиї імена потрібно зчитати.

    Повертає:
        dict: словник, де ключ — ім'я, значення — початкова сума (0).
    """
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0
    return friends


def get_total_amount():
    """
    Запитує загальну суму рахунку.

    Повертає:
        int або None: загальна сума, або None у разі хибного вводу.
    """
    print("Enter the total amount:")
    try:
        total_amount = int(input())
    except ValueError:
        return None
    return total_amount


def ask_lucky_feature():
    """
    Запитує користувача, чи бажає він використати функцію
    «Who is lucky?» для випадкового вибору того, хто не платить.

    Повертає:
        str: відповідь користувача ("Yes" або інший рядок).
    """
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    return input()


def split_equally(friends, total_amount):
    """
    Рівномірно розподіляє загальну суму рахунку між усіма учасниками.

    Аргументи:
        friends (dict): словник з іменами та сумами.
        total_amount (int): загальна сума рахунку.
    """
    num_friends = len(friends)
    share = round(total_amount / num_friends, 2)
    for name in friends:
        friends[name] = share


def apply_lucky_feature(friends, total_amount):
    """
    Реалізує функцію «Who is lucky?»:
    випадково обирає людину, яка не платить, та перераховує суми для інших.

    Аргументи:
        friends (dict): словник з іменами та сумами.
        total_amount (int): загальна сума рахунку.
    """
    answer = ask_lucky_feature()

    if answer == "Yes":
        lucky_one = random.choice(list(friends.keys()))
        print(f"{lucky_one} is the lucky one!")

        num_friends = len(friends)
        if num_friends > 1:
            new_share = round(total_amount / (num_friends - 1), 2)
            for name in friends:
                friends[name] = new_share
            friends[lucky_one] = 0
        else:
            # Якщо у списку лише одна людина — вона нічого не платить
            for name in friends:
                friends[name] = 0

        print(friends)
    else:
        print("No one is going to be lucky")
        print(friends)


def split_bill():
    """
    Основна функція, що координує процес розподілу рахунку.

    Виконує:
        - зчитування кількості учасників
        - введення їхніх імен
        - зчитування суми
        - розподіл суми
        - застосування функції випадкового щасливчика
    """
    num_friends = get_number_of_friends()

    if num_friends is None or num_friends <= 0:
        print("No one is joining for the party")
        return

    friends = get_friends_dict(num_friends)

    total_amount = get_total_amount()
    if total_amount is None:
        print("No one is joining for the party")
        return

    split_equally(friends, total_amount)
    apply_lucky_feature(friends, total_amount)


if __name__ == "__main__":
    split_bill()
