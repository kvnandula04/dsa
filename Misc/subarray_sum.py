class BruteForceSolution:
    def subArraySum(self, arr, n, s):
        # Iterate through the array starting from each index
        for start_index in range(n):
            current_sum = arr[start_index]

            # Check if the single element matches the sum
            if current_sum == s:
                return [start_index + 1, start_index + 1]

            # Now try to expand the subarray by adding more elements to the right
            for end_index in range(start_index + 1, n):
                current_sum += arr[end_index]

                # If we find the required sum, return the indices (1-based)
                if current_sum == s:
                    return [start_index + 1, end_index + 1]

                # If the current sum exceeds the target sum, break out of the inner loop
                if current_sum > s:
                    break

        # If no subarray with the required sum is found, return [-1]
        return [-1]


class OptimisedSolution:
    def subArraySum(self, arr, n, s):
        start = 0
        current_sum = arr[0]

        for end in range(1, n + 1):
            # Remove elements from the start if current_sum exceeds the target sum `s`
            while current_sum > s and start < end - 1:
                current_sum -= arr[start]
                start += 1

            # If current_sum becomes equal to `s`, return the indices (1-based)
            if current_sum == s:
                return [start + 1, end]  # 1-based indexing

            # Add the current element to `current_sum` if `end` is still within array bounds
            if end < n:
                current_sum += arr[end]

        # If no subarray with sum `s` is found, return [-1]
        return [-1]


sol = OptimisedSolution()

# 1. Single Element Matching the Sum
print("1. ", sol.subArraySum([10], 1, 10) == [1, 1])

# 2. Single Element Not Matching the Sum
print("2. ", sol.subArraySum([10], 1, 5) == [-1])

# 3. Multiple Elements, Subarray at the Beginning
print("3. ", sol.subArraySum([5, 5, 5, 10], 4, 10) == [1, 2])

# 4. Multiple Elements, Subarray in the Middle
print("4. ", sol.subArraySum([1, 2, 4, 3, 7], 5, 9) == [2, 4])

# 5. Multiple Elements, Subarray at the End
print("5. ", sol.subArraySum([1, 2, 3, 7, 5], 5, 12) == [2, 4])

# 6. No Subarray Matching the Sum
print("6. ", sol.subArraySum([1, 2, 3, 4, 5], 5, 20) == [-1])

# 7. All Elements Are the Same, Sum Matches Part of the Array
print("7. ", sol.subArraySum([5, 5, 5, 5, 5], 5, 15) == [1, 3])

# 8. Large Array with the Subarray at the End
print("8. ", sol.subArraySum([1] * 999 + [1000], 1000, 1000) == [1000, 1000])

# 9. Sum Formed by Non-Consecutive Elements
print("9. ", sol.subArraySum([1, 4, 20, 3, 10, 5], 6, 33) == [3, 5])

# 10. Sum Requires the Whole Array
print("10. ", sol.subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10, 55) == [1, 10])

# 11. Array Contains Zeroes
print("11. ", sol.subArraySum([0, 0, 3, 0, 0], 5, 3) == [3, 3])

# 12. Subarray with Zero Sum
print("12. ", sol.subArraySum([0, 0, 0, 0], 4, 0) == [1, 1])

# 13. Long Subarray Near the End
print("13. ", sol.subArraySum([1, 2, 3, 4, 5, 10], 6, 22) == [3, 6])

# 14. Subarray with Repeating Numbers
print("14. ", sol.subArraySum([1, 2, 2, 2, 2, 2, 2], 7, 8) == [2, 5])

# 15. Complex Large Array
print("15. ", sol.subArraySum(list(range(1, 101)), 100, 5050) == [1, 100])

# 16. Edge Case with Very Large Numbers
print(
    "16. ",
    sol.subArraySum([1000000000, 1000000000, 1000000000], 3, 2000000000) == [1, 2],
)

# 17. Subarray Sum Is at the Very Beginning
print("17. ", sol.subArraySum([5, 1, 2, 3, 4, 5], 6, 5) == [1, 1])
