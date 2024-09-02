# Dictionary holding the LED patterns for digits 0-9
led_patterns = {
    "0": ["###", "# #", "# #", "# #", "###"],
    "1": ["  #", "  #", "  #", "  #", "  #"],
    "2": ["###", "  #", "###", "#  ", "###"],
    "3": ["###", "  #", "###", "  #", "###"],
    "4": ["# #", "# #", "###", "  #", "  #"],
    "5": ["###", "#  ", "###", "  #", "###"],
    "6": ["###", "#  ", "###", "# #", "###"],
    "7": ["###", "  #", "  #", "  #", "  #"],
    "8": ["###", "# #", "###", "# #", "###"],
    "9": ["###", "# #", "###", "  #", "###"],
}


# Function to print the number using the LED patterns
def print_led_number(number):
    # Convert the number to a string
    str_number = str(number)

    # Create an empty list for each line of the output
    rows = ["", "", "", "", ""]

    # Append the corresponding pattern for each digit
    for digit in str_number:
        pattern = led_patterns[digit]
        for i in range(5):  # We have 5 rows
            rows[i] += pattern[i] + " "  # Add a space between digits

    # Print the result
    for row in rows:
        print(row)


# Example Usage
print_led_number(123)
print()  # Print a new line for separation
print_led_number(9081726354)
