class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = ""
        longest_palindrome_length = 0

        for i in range(len(s)):
            # odd case
            left, right = i, i

            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest_palindrome_length:
                    longest_palindrome = s[left : right + 1]
                    longest_palindrome_length = right - left + 1

                left -= 1  # expand outwards - move left pointer to the left
                right += 1  # expand outwards - move right pointer to the right

            # even case
            left, right = i, i + 1  # i + 1 is the right pointer for even case
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > longest_palindrome_length:
                    longest_palindrome = s[left : right + 1]
                    longest_palindrome_length = right - left + 1

                left -= 1
                right += 1

        return longest_palindrome


sol = Solution()
print(sol.longestPalindrome("babad"))
print(sol.longestPalindrome("cbbd"))
