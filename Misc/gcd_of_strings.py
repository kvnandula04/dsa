class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def divisible(s, t):
            return s == t * (len(s) // len(t))

        if len(str1) < len(str2):
            str1, str2 = str2, str1

        for i in range(len(str2), 0, -1):
            gcd = str2[:i]
            if divisible(str1, gcd) and divisible(str2, gcd):
                return gcd

        return ""


sol = Solution()
print(sol.gcdOfStrings("ABCABC", "ABC"))  # ABC
print(sol.gcdOfStrings("ABABAB", "ABAB"))  # AB
