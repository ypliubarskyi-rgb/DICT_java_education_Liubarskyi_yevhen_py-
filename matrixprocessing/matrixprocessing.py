def read_matrix(p_size="Enter size: ", p_mat="Enter matrix:"):
    """Зчитує розмір та елементи матриці з консолі."""
    try:
        line = input(p_size).split()
        if not line: return None, None, None
        n, m = map(int, line)
        print(p_mat)
        return n, m, [list(map(float, input().split())) for _ in range(n)]
    except: return None, None, None

def print_result(mat):
    """Виводить матрицю, форматуючи числа до гарного вигляду."""
    print("The result is:")
    for row in mat:
        print(*(int(x) if x == int(x) else round(x, 2) for x in row))
    print()

def add_matrices():
    """Додає дві матриці, якщо їхні розміри однакові."""
    n1, m1, a = read_matrix("Enter size of first matrix: ")
    n2, m2, b = read_matrix("Enter size of second matrix: ")
    if n1 == n2 and m1 == m2:
        print_result([[a[i][j] + b[i][j] for j in range(m1)] for i in range(n1)])
    else: print("The operation cannot be performed.\n")

def multiply_by_const():
    """Множить кожен елемент матриці на введене число."""
    n, m, a = read_matrix()
    if a:
        c = float(input("Enter constant: "))
        print_result([[a[i][j] * c for j in range(m)] for i in range(n)])

def multiply_matrices():
    """Виконує класичне множення матриць (рядок на стовпець)."""
    n1, m1, a = read_matrix("Enter size of first matrix: ")
    n2, m2, b = read_matrix("Enter size of second matrix: ")
    if m1 == n2:
        res = [[sum(a[i][k] * b[k][j] for k in range(m1)) for j in range(m2)] for i in range(n1)]
        print_result(res)
    else: print("The operation cannot be performed.\n")

def transpose_matrix():
    """Транспонує матрицю за одним із чотирьох обраних способів."""
    print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    ch = input("Your choice: ")
    n, m, a = read_matrix("Enter matrix size: ")
    if not a: return
    if ch == '1': res = [[a[j][i] for j in range(n)] for i in range(m)]
    elif ch == '2': res = [[a[n-1-j][m-1-i] for j in range(n)] for i in range(m)]
    elif ch == '3': res = [r[::-1] for r in a]
    elif ch == '4': res = a[::-1]
    else: return
    print_result(res)

def get_det(m):
    """Рекурсивно обчислює визначник квадратної матриці."""
    if len(m) == 1: return m[0][0]
    if len(m) == 2: return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    det = 0
    for j in range(len(m)):
        minor = [row[:j] + row[j+1:] for row in m[1:]]
        det += ((-1)**j) * m[0][j] * get_det(minor)
    return det

def inverse_matrix():
    """Знаходить обернену матрицю через матрицю алгебраїчних доповнень."""
    n, m, a = read_matrix()
    if not a or n != m:
        print("This matrix doesn't have an inverse.\n")
        return
    det = get_det(a)
    if det == 0:
        print("This matrix doesn't have an inverse.\n")
        return
    adj_t = []
    for j in range(n):
        row = []
        for i in range(n):
            minor = [r[:j] + r[j+1:] for r in (a[:i] + a[i+1:])]
            row.append(((-1)**(i+j)) * get_det(minor))
        adj_t.append(row)
    print_result([[adj_t[i][j] / det for j in range(n)] for i in range(n)])

def main():
    """Головне меню програми для вибору операцій."""
    menu = "\n1. Add matrices\n2. Multiply matrix by constant\n3. Multiply matrices\n4. Transpose matrix\n5. Calculate determinant\n6. Inverse matrix\n0. Exit\nYour choice: "
    while True:
        choice = input(menu)
        if choice == '1': add_matrices()
        elif choice == '2': multiply_by_const()
        elif choice == '3': multiply_matrices()
        elif choice == '4': transpose_matrix()
        elif choice == '5':
            n, m, a = read_matrix()
            if a: print(f"The result is:\n{get_det(a)}\n")
        elif choice == '6': inverse_matrix()
        elif choice == '0': break

if __name__ == "__main__":
    main()