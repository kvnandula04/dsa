class Solution:
    def reverse(self, x: int) -> int:
        reverse = ""

        if x < 0:
            reverse += "-"
            x = abs(x)

        for i in range(len(str(x))):
            digit = x % 10
            x //= 10
            reverse += str(digit)

        return int(reverse) if -(2**31) <= int(reverse) <= 2**31 - 1 else 0


sol = Solution()
print(sol.reverse(123))  # 321
print(sol.reverse(-123))  # -321
print(sol.reverse(120))  # 21
