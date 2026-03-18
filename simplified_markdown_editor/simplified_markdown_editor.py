def get_header():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 6:
                return f"{'#' * level} {input('Text: ')}\n"
            print("The level should be within the range of 1 to 6")
        except ValueError:
            print("Value must be a number")


def get_list(is_ordered):
    while True:
        try:
            number = int(input("Number of rows: "))
            if number > 0:
                break
            print("The number of rows should be greater than zero")
        except ValueError:
            print("Value must be a number")

    rows = [f"{i + 1}. {input(f'Row #{i + 1}: ')}" if is_ordered else f"* {input(f'Row #{i + 1}: ')}" for i in range(number)]
    return "\n".join(rows) + "\n"


def main():
    full_text = []

    formatters = {
        "plain": lambda: input("Text: "),
        "bold": lambda: f"**{input('Text: ')}**",
        "italic": lambda: f"*{input('Text: ')}*",
        "inline-code": lambda: f"`{input('Text: ')}`",
        "link": lambda: f"[{input('Label: ')}]({input('URL: ')})",
        "new-line": lambda: "\n",
        "header": get_header,
        "ordered-list": lambda: get_list(True),
        "unordered-list": lambda: get_list(False)
    }

    while True:
        command = input("Choose a formatter >>> ").strip()

        if command == "!done":
            with open('output.md', 'w', encoding="utf-8") as f:
                f.write("".join(full_text))
            break

        if command == "!help":
            print(f"Available formatters: {' '.join(formatters.keys())}")
            print("Special commands: !help !done")
            continue

        if command in formatters:
            result = formatters[command]()
            full_text.append(result)
            print("".join(full_text))
        else:
            print("Unknown formatting type or command")


if __name__ == "__main__":
    main()