# Ask the user for input
text = input("Enter a string: ").lower().replace(" ", "")

# Check for empty string
if text == "":
    print("It's not a palindrome")
else:
    # Check if the text is equal to its reverse
    if text == text[::-1]:
        print("It's a palindrome")
    else:
        print("It's not a palindrome")
