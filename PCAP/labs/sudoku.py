rows = []


def take_validate_input(rows):
    while True:
        line = input("Enter a row (or press Enter to finish): ")

        if line == "":
            break

        rows.append(line)

    if len(rows) == 9 and all(len(row) == 9 for row in rows):
        print("Input collected successfully!")
    else:
        print("Invalid input! Make sure to enter 9 rows of 9 digits each.")


def is_valid_block(block):
    # A valid block contains all digits 1-9 exactly once
    return "".join(sorted(block)) == "123456789"


def sudoku(rows):
    # Check rows
    if not all(is_valid_block(row) for row in rows):
        return "No"

    # Check columns
    for col in range(9):
        column = [rows[row][col] for row in range(9)]
        if not is_valid_block(column):
            return "No"

    # Check 3x3 sub-grids
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            block = []
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    block.append(rows[row][col])
            if not is_valid_block(block):
                return "No"

    return "Yes"


# Test on valid data
print(
    sudoku(
        [
            "295743861",
            "431865927",
            "876192543",
            "387459216",
            "612387495",
            "549216738",
            "763524189",
            "928671354",
            "154938672",
        ]
    )
)  # Expected output: Yes

# Test on invalid data
print(
    sudoku(
        [
            "195743862",
            "431865927",
            "876192543",
            "387459216",
            "612387495",
            "549216738",
            "763524189",
            "928671354",
            "254938671",
        ]
    )
)  # Expected output: No
