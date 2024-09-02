def read_int(prompt, min, max):
    while True:
        try:
            # Try to convert the input to an integer
            v = int(input(prompt))

            # Check if the value is within the allowed range
            if min <= v <= max:
                return v
            else:
                print(f"Error: the value is not within permitted range ({min}..{max})")

        except ValueError:
            # Handle the case where input is not a valid integer
            print("Error: wrong input")


# Test the function
v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
