class Solution:
    def firstUniqChar(self, s: str) -> int:
        chars = {}

        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

        for index, char in enumerate(chars):
            if chars[char] == 1:
                return s.index(char)

        return -1


sol = Solution()
print(sol.firstUniqChar("leetcode"))
print(sol.firstUniqChar("aabb"))
print(sol.firstUniqChar("dddccdbba"))
