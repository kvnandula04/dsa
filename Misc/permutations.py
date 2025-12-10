def permute(nums):
    permutations = []

    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        permutations.extend(perms)
        nums.append(n)

    return permutations


nums = [1, 2, 3]

permutations = sorted(permute(nums))
next_lexicographic_permutation = permutations[
    (permutations.index(nums) + 1) % len(permutations)
]

print(next_lexicographic_permutation)
