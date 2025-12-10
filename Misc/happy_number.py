def isHappy(n: int) -> bool:
    appeared = []
    result = 0

    while len(appeared) == len(set(appeared)):  # while no duplicates
        result = sum(
            int(digit) ** 2 for digit in str(n)
        )  # calculate the sum of the squares of the digits

        n = result
        appeared.append(result)

        if result == 1:  # if the result calculated is 1, return True
            return True

        result = 0

    return False  # if a duplicate appears, it means it's stuck in a loop without having found a 1, so return False by default


print(isHappy(2))
