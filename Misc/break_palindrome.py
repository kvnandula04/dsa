class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if n == 1:
            return ""

        for i in range(n // 2):  # only need to search until midpoint
            if palindrome[i] != "a":  # first non-a character
                return palindrome[:i] + "a" + palindrome[i + 1 :]

        return palindrome[:-1] + "b"  # case of all a characters


sol = Solution()
print(sol.breakPalindrome("abccba"))
print(sol.breakPalindrome("acccccca"))
print(sol.breakPalindrome("aaaaa"))
print(sol.breakPalindrome("zzz"))
