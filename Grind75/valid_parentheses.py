# Code
class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")": "(", "}": "{", "]": "["}
        stack = []

        for c in s:
            if c in brackets.values():  # open bracket
                stack.append(c)

            elif c in brackets.keys():  # closed bracket
                if not stack or stack[-1] != brackets[c]:
                    return False
                stack.pop()

        return len(stack) == 0


# Test
sol = Solution()

solution = sol.isValid("()")
print(solution)  # Expected Output: True
solution = sol.isValid("()[]{}")
print(solution)  # Expected Output: True
solution = sol.isValid("(]")
print(solution)  # Expected Output: False
solution = sol.isValid("([])")
print(solution)  # Expected Output: True
