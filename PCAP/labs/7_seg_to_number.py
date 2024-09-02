# ------ Setup ------
# List the digits to be displayed in the 7-segment display
digits = """
 _     _  _     _  _  _  _  _ 
| |  | _| _||_||_ |_   ||_||_|
|_|  ||_  _|  | _||_|  ||_| _|
"""

# Create an array to hold the digits representations in their 7-segment display form
lines = digits.splitlines()
length = len(lines[1])

digits_arr = []

# Loop through the digits and append them to the digits_arr
for i in range(0, length, 3):
    digit = lines[1][i : i + 3] + lines[2][i : i + 3] + lines[3][i : i + 3]
    digits_arr.append(digit)

# ------ Main Program ------
# 1234
input1 = """
    _  _    
  | _| _||_|
  ||_  _|  |
"""

# 4338058286
input2 = """
    _  _  _  _  _  _  _  _  _ 
|_| _| _||_|| ||_ |_| _||_||_ 
  | _| _||_||_| _||_||_ |_||_|
"""

print(digits_arr)

# Add test data to an array
inputs = [input1, input2]

# Loop through the test data
for i in inputs:
    lines = i.splitlines()
    length = len(lines[1])

    output = ""

    for i in range(0, length, 3):
        digit = lines[1][i : i + 3] + lines[2][i : i + 3] + lines[3][i : i + 3]
        if digit in digits_arr:
            output += str(digits_arr.index(digit))

    print(int(output))
