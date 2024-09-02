def mysplit(strng):
    output = []
    word = ""

    for char in strng:
        if char == " ":
            output.append(word)
            word = ""
        else:
            word += char

    output.append(word)
    return output


print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
