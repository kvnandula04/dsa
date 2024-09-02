class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = ""

        for char in s:
            if char.isdigit():
                current_num += char
            elif char == "[":
                stack.append((current_string, int(current_num)))
                current_string = ""
                current_num = ""
            elif char == "]":
                last_string, last_num = stack.pop()
                current_string = last_string + (current_string * int(last_num))
            else:
                current_string += char

        return current_string


sol = Solution()
print(sol.decodeString("3[a]2[bc]"))  # Output: "aaabcbc"
print(sol.decodeString("3[a2[c]]"))  # Output: "accaccacc"
print(sol.decodeString("2[abc]3[cd]ef"))  # Output: "abcabccdcdcdef"
print(sol.decodeString("100[leetcode]"))  # Output: "leetcodeleetcodeleetcode..."
