"""
Гра "Хрестики-нулики".
Етап 5: повноцінна гра для двох гравців ('X' та 'O') від порожнього поля до
кінця (перемога одного з гравців або нічия).
"""


def normalize_cell_symbol(symbol):
    """
    Нормалізує символ клітинки:
    - 'X' залишається 'X';
    - 'O' або '0' перетворюється на 'O';
    - '_' залишається '_'.
    """
    if symbol == "X":
        return "X"
    if symbol in ("O", "0"):
        return "O"
    if symbol == "_":
        return "_"
    return symbol


def build_grid_from_string(cells):
    """
    Перетворює рядок із 9 символів на двовимірний список 3x3.
    Очікуються символи 'X', 'O'/'0' або '_'.
    """
    cells = cells.strip()
    if len(cells) != 9:
        raise ValueError("Рядок повинен містити рівно 9 символів.")
    grid = []
    index = 0
    for _ in range(3):
        row = []
        for _ in range(3):
            row.append(normalize_cell_symbol(cells[index]))
            index += 1
        grid.append(row)
    return grid


def print_grid(grid):
    """
    Друкує ігрове поле 3x3 з рамкою.
    Символ '_' друкується як пробіл (порожня клітинка).
    """
    print("---------")
    for row in grid:
        visual_row = []
        for cell in row:
            if cell == "_":
                visual_row.append(" ")
            else:
                visual_row.append(cell)
        print("| " + " ".join(visual_row) + " |")
    print("---------")


def count_symbols(grid):
    """
    Підраховує кількість 'X', 'O' та '_' на полі.
    Повертає кортеж (кількість X, кількість O, кількість '_').
    """
    x_count = 0
    o_count = 0
    empty_count = 0
    for row in grid:
        for cell in row:
            if cell == "X":
                x_count += 1
            elif cell == "O":
                o_count += 1
            elif cell == "_":
                empty_count += 1
    return x_count, o_count, empty_count


def get_all_lines(grid):
    """
    Формує список усіх ліній на полі:
    3 рядки, 3 стовпці та 2 діагоналі.
    """
    lines = []

    for row in grid:
        lines.append(row)

    for col in range(3):
        column = [grid[row][col] for row in range(3)]
        lines.append(column)

    diag1 = [grid[i][i] for i in range(3)]
    diag2 = [grid[i][2 - i] for i in range(3)]
    lines.append(diag1)
    lines.append(diag2)

    return lines


def is_winner(grid, player):
    """
    Перевіряє, чи має гравець `player` ( 'X' або 'O' ) три символи в ряд.
    """
    for line in get_all_lines(grid):
        if all(cell == player for cell in line):
            return True
    return False


def analyze_state(grid):
    """
    Аналізує стан гри на полі 3x3 та повертає один із рядків:
    "Game not finished", "Draw", "X wins", "O wins" або "Impossible".
    """
    x_count, o_count, empty_count = count_symbols(grid)
    x_wins = is_winner(grid, "X")
    o_wins = is_winner(grid, "O")

    if abs(x_count - o_count) > 1:
        return "Impossible"

    if x_wins and o_wins:
        return "Impossible"

    if x_wins:
        return "X wins"

    if o_wins:
        return "O wins"

    if empty_count > 0:
        return "Game not finished"

    return "Draw"


def read_move_coordinates():
    """
    Зчитує координати ходу користувача у форматі "row col".
    Повторює запит доти, доки користувач не введе два цілі числа.
    """
    while True:
        raw = input("Enter the coordinates: ")
        parts = raw.split()
        if len(parts) != 2:
            print("You should enter numbers!")
            continue
        try:
            row = int(parts[0])
            col = int(parts[1])
        except ValueError:
            print("You should enter numbers!")
            continue
        return row, col


def apply_move_for_player(grid, player):
    """
    Дозволяє гравцю `player` ('X' або 'O') зробити один хід на полі 3x3.
    Перевіряє діапазон координат та зайнятість клітинки.
    """
    while True:
        row, col = read_move_coordinates()

        if not (1 <= row <= 3 and 1 <= col <= 3):
            print("Coordinates should be from 1 to 3!")
            continue

        row_index = row - 1
        col_index = col - 1

        if grid[row_index][col_index] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        grid[row_index][col_index] = player
        break


def play_game():
    """
    Запускає повну гру "Хрестики-нулики" для двох гравців.
    Початкове поле порожнє, гравці ходять по черзі до перемоги або нічиєї.
    """
    grid = build_grid_from_string("_________")
    print_grid(grid)

    current_player = "X"

    while True:
        apply_move_for_player(grid, current_player)
        print_grid(grid)

        state = analyze_state(grid)

        if state in ("X wins", "O wins", "Draw", "Impossible"):
            print(state)
            break

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"


def main():
    """
    Головна функція програми для етапу 5.
    Запускає повну гру для двох гравців.
    """
    play_game()


if __name__ == "__main__":
    main()
