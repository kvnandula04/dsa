class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        x_y_count, y_x_count = 0, 0

        for i in range(len(s1)):
            if s1[i] == s2[i]:
                s1.replace(s1[i], "", 1)
                s2.replace(s2[i], "", 1)
            elif s1[i] == "x" and s2[i] == "y":
                x_y_count += 1
            elif s1[i] == "y" and s2[i] == "x":
                y_x_count += 1
            else:
                return -1

        total_count = x_y_count + y_x_count

        if total_count % 2 != 0:  # odd
            return -1
        else:
            swaps = (x_y_count // 2) + (y_x_count // 2)
            swaps += (
                2 if (x_y_count % 2) or (y_x_count % 2) else 0
            )  # 2 swaps required if 1 of each left

        return swaps


sol = Solution()
print(sol.minimumSwap("xx", "yy"))
