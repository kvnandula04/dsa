from typing import List
from itertools import permutations
import random


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combinations = []
        mappings = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        def backtrack(i, combination):
            if len(combination) == len(digits):  # got a valid combination
                combinations.append(combination)
                return

            for char in mappings[
                int(digits[i])
            ]:  # loop through all the characters which can be formed by the digit until valid combination is formed
                backtrack(i + 1, combination + char)

        if digits:
            backtrack(0, "")

        return combinations


sol = Solution()
print(sol.letterCombinations("23"))
