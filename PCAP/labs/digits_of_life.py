def digits_of_life(dob):
    total = sum(int(digit) for digit in dob)

    if total < 10:
        return total
    else:
        return digits_of_life(str(total))


dob = str(input("Enter your date of birth (DDMMYYYY): "))

if dob == "":
    print("It's not a valid date of birth")
else:
    print(digits_of_life(dob))
