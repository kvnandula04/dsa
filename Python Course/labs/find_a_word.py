first_string = input("Enter the first string: ")
second_string = input("Enter the second string: ")


def find_a_word(first_string, second_string):
    index = 0
    for char in first_string:
        index = second_string.find(char, index)
        if index == -1:
            return "No"
        index += 1
    return "Yes"


print(find_a_word(first_string, second_string))
