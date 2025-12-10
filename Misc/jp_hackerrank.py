def chooseFleets(wheels):
    # Write your code here
    result = []

    for current_sum in wheels:
        # Approach 1:
        # # number of ways = 2x + 4y
        # ways = 0

        # # max number of 2 wheelers
        # for i in range(current_sum // 2 + 1):
        #     remaining = current_sum - (2 * i)
        #     # check remaining if we can add any 4 wheelers
        #     if remaining >= 0 and remaining % 4 == 0:
        #         ways += 1

        # result.append(ways)

        # Approach 2:
        if current_sum % 2 != 0:
            result.append(0)
        else:
            result.append((current_sum // 4) + 1)

    return result


print(chooseFleets([4, 6, 8]))
