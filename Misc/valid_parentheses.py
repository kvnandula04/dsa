class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {"{": "}", "(": ")", "[": "]"}
        stack = []

        for char in s:
            if char in "([{":
                stack.append(char)
            elif char in ")]}":
                if not stack or char != parentheses[stack[-1]]:
                    return False
                else:
                    stack.pop()

        return stack == []


sol = Solution()
print(sol.isValid("()[]"))
print(sol.isValid("([])"))
print(sol.isValid("([]"))
print(sol.isValid("([\{\}])"))
print(sol.isValid("(]"))
