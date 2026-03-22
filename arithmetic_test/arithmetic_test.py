import random
import operator
from abc import ABC, abstractmethod




class TaskProvider(ABC):
    """
    Абстрактний клас (шаблон).
    Він гарантує, що кожен рівень складності матиме методи generate та get_description.
    """

    @abstractmethod
    def generate(self):
        """Повертає кортеж: (текст_завдання, числова_відповідь)"""
        pass

    @abstractmethod
    def get_description(self):
        """Повертає текстовий опис рівня для збереження у файл"""
        pass


class SimpleArithmeticTask(TaskProvider):
    """Рівень 1: Прості операції з числами 2-9"""

    def generate(self):
        ops = {"+": operator.add, "-": operator.sub, "*": operator.mul}
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        char = random.choice(list(ops.keys()))
        return f"{a} {char} {b}", ops[char](a, b)

    def get_description(self):
        return "simple operations with numbers 2-9"


class SquareTask(TaskProvider):
    """Рівень 2: Квадрати чисел 11-29"""

    def generate(self):
        num = random.randint(11, 29)
        return str(num), num ** 2

    def get_description(self):
        return "integral squares of 11-29"




class TestEngine:
    """
    Клас, що керує процесом тестування.
    """

    def __init__(self, task_provider: TaskProvider):
        self.task_provider = task_provider
        self.mark = 0
        self.total_tasks = 5

    def _get_safe_int(self, prompt=""):
        """Внутрішній метод для безпечного зчитування чисел"""
        while True:
            try:
                user_input = input(prompt).strip()
                return int(user_input)
            except ValueError:
                print("Incorrect format.")

    def run(self):
        """Запуск циклу з 5 питань"""
        for _ in range(self.total_tasks):
            question, correct_answer = self.task_provider.generate()
            print(question)

            user_answer = self._get_safe_int("> ")

            if user_answer == correct_answer:
                print("Right!")
                self.mark += 1
            else:
                print("Wrong!")

        print(f"Your mark is {self.mark}/{self.total_tasks}.")
        self._ask_to_save()

    def _ask_to_save(self):
        """Логіка збереження результатів у файл"""
        choice = input("Would you like to save your result to the file? Enter yes or no.\n> ").lower()
        if choice in ["yes", "y", "yes", "Yes", "YES"]:
            name = input("What is your name?\n> ")
            desc = self.task_provider.get_description()
            # Запис у файл (режим 'a' - додавання)
            with open("results.txt", "a", encoding="utf-8") as f:
                f.write(f"{name}: {self.mark}/{self.total_tasks} in level {desc}.\n")
            print('The results are saved in "results.txt".')




def main():

    levels = {
        "1": SimpleArithmeticTask(),
        "2": SquareTask()
    }

    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = input("> ").strip()

        if choice in levels:

            engine = TestEngine(levels[choice])
            engine.run()
            break
        else:
            print("Incorrect format.")


if __name__ == "__main__":
    main()