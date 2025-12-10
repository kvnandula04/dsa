class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        divisor = 1
        while x >= 10 * divisor:
            divisor *= 10

        while x:
            left = x // divisor  # left most digit
            right = x % 10  # right most digit

            if left != right:
                return False

            # remove both the left and right most digits to test again with the remaining digits
            x = (x % divisor) // 10
            divisor /= 100

        return True
