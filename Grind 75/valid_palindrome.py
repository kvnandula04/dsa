class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
            
        return True
            

sol = Solution()
print(sol.isPalindrome("A man, a plan, a canal: Panama"))  # Expected output: True
print(sol.isPalindrome("race a car"))  # Expected output: False
print(sol.isPalindrome("0P"))  # Expected output: False
