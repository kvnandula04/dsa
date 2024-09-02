class Solution:
    def countSubstrings(self, s: str) -> int:
        char_length = 1
        substrings = []
        for char in s:
            substrings.append(char)