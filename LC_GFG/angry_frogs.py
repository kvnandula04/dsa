class Solution:
    def angryFrogs(self, blocks):
        max_distance = 0
        start_for_both = 0

        while start_for_both < len(blocks):
            i_frog_position = start_for_both
            j_frog_position = start_for_both

            # Move i_frog as far to the left as possible
            for i in range(start_for_both, 0, -1):
                if (
                    i_frog_position - 1 >= 0
                    and blocks[i_frog_position - 1] >= blocks[i_frog_position]
                ):
                    i_frog_position -= 1
                else:
                    break

            # Move j_frog as far to the right as possible
            for j in range(start_for_both, len(blocks) - 1):
                if (
                    j_frog_position + 1 < len(blocks)
                    and blocks[j_frog_position + 1] >= blocks[j_frog_position]
                ):
                    j_frog_position += 1
                else:
                    break

            # Calculate the distance between the two frogs
            distance = j_frog_position - i_frog_position + 1
            max_distance = max(max_distance, distance)
            start_for_both += 1

        return max_distance

    # Linear Complexity
    def angryFrogsOptimised(self, blocks):
        N = len(blocks)

        # Step 1: Left Reach Calculation
        left = [0] * N
        left[0] = 0  # The first block can only stay at its place
        for i in range(1, N):
            if blocks[i] >= blocks[i - 1]:
                left[i] = left[i - 1]
            else:
                left[i] = i

        # Step 2: Right Reach Calculation
        right = [0] * N
        right[N - 1] = N - 1  # The last block can only stay at its place
        for i in range(N - 2, -1, -1):
            if blocks[i] >= blocks[i + 1]:
                right[i] = right[i + 1]
            else:
                right[i] = i

        print(left, right)
        # Step 3: Calculate Maximum Distance
        max_distance = 0
        for i in range(N):
            max_distance = max(max_distance, right[i] - left[i] + 1)

        return max_distance


sol = Solution()

print("Input: [1, 1] Expected Output: 2 Output:", sol.angryFrogs([1, 1]))
print("Input: [2, 6, 8, 5] Expected Output: 3 Output:", sol.angryFrogs([2, 6, 8, 5]))
print(
    "Input: [1, 5, 5, 2, 6] Expected Output: 4 Output:",
    sol.angryFrogs([1, 5, 5, 2, 6]),
)
print(sol.angryFrogs([2, 4, 4, 6, 8, 1, 7, 3, 5, 5]))
print(sol.angryFrogsOptimised([2, 4, 4, 6, 8, 1, 7, 3, 5, 5]))
