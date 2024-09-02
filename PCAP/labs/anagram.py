# Ask the user for input
text1 = input("Enter the first string: ").lower().replace(" ", "")
text2 = input("Enter the second string: ").lower().replace(" ", "")

# Check for empty string
if text1 == "" or text2 == "":
    print("It's not an anagram")
else:
    if sorted(text1) == sorted(text2):
        print("It's an anagram")
    else:
        print("Not anagrams")
