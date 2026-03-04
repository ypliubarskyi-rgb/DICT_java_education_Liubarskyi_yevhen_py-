class CoffeeMachine:
    def __init__(self):
        """Инициализирует кофемашину со стандартным набором ресурсов."""
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "Choosing_actions"

    def handle_input(self, user_input):
        """Направляет ввод пользователя в нужный метод в зависимости от текущего состояния.

        Parameters:
        user_input (str): Команда или данные, введенные пользователем.
        """
        if self.state == "Choosing_actions":
            self.process_main_acion(user_input)
        elif self.state == "Choosing_coffee":
            self.process_buy_action(user_input)
        elif self.state == "Choosing_fill":
            self.process_fill_action(user_input)

    def process_main_acion(self, action):
        """Обрабатывает основные команды: buy, fill, take, remaining, exit.

        Parameters:
        action (str): Основное действие, выбранное пользователем.
        """
        if action == "buy":
            self.state = "Choosing_coffee"
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu\n")
        elif action == "remaining":
            self.print_state()
        elif action == "take":
            print(f"I gave u {self.money}")
            self.money = 0
        elif action == "exit":
            exit()
        elif action == "fill":
            self.state = "Choosing_fill"
            print("Enter amount of water, milk, beans and cups separated by spaces:")

    def process_buy_action(self, choice):
        """Управляет процессом выбора типа кофе.

        Parameters:
        choice (str): Номер типа кофе или команда 'back'.
        """
        if choice == "back":
            self.state = "Choosing_actions"
            return

        recipes = {
            "1": [250, 0, 16, 4],
            "2": [350, 75, 20, 7],
            "3": [200, 100, 12, 6]
        }

        if choice in recipes:
            self.make_coffee(recipes[choice])

        self.state = "Choosing_actions"

    def make_coffee(self, recipe):
        """Проверяет наличие ресурсов и списывает ингредиенты для приготовления кофе.

        Parameters:
        recipe (list): Список, содержащий [вода, молоко, зерна, стоимость].
        """
        req_water, req_milk, req_beans, req_money = recipe

        if self.water < req_water:
            print("Not enough water")
        elif self.milk < req_milk:
            print("Not enough milk")
        elif self.beans < req_beans:
            print("Not enough beans")
        elif self.cups < 1:
            print("Not enough cups")
        else:
            print("I have enough resources, making you a coffee!")
            self.money += req_money
            self.water -= req_water
            self.cups -= 1
            self.beans -= req_beans
            self.milk -= req_milk

    def print_state(self):
        """Выводит текущий уровень всех ресурсов и денег."""
        print(f"""
The coffee machine has:
{self.water} ml of water
{self.milk} ml of milk
{self.beans} g of coffee beans
{self.cups} disposable cups
${self.money} of money""")

    def process_fill_action(self, filling_action):
        """Разбирает строку ввода и добавляет ресурсы в машину.

        Parameters:
        filling_action (str): Строка, содержащая 4 целых числа через пробел.
        """
        try:
            data_string = filling_action.split()

            if len(data_string) != 4:
                print("Please enter 4 numbers!")
            else:
                data = list(map(int, data_string))

                if min(data) < 0:
                    print("Please enter dont negative numbers!")
                else:
                    fill_water, fill_milk, fill_beans, fill_cups = data
                    self.water += fill_water
                    self.milk += fill_milk
                    self.beans += fill_beans
                    self.cups += fill_cups
                    print("Resource added!")
        except ValueError:
            print("Error: Enter only numbers!")

        self.state = "Choosing_actions"


machine = CoffeeMachine()

while True:
    if machine.state == "Choosing_actions":
         print("\nWrite action (buy, fill, take, remaining, exit):")

    command = input(">@  ")
    machine.handle_input(command)