from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(remaining, combination, start):
            if remaining == 0:
                # If we hit the target, add the combination to the result
                result.append(list(combination))
                return
            elif remaining < 0:
                # If the sum exceeds the target, stop exploring this path
                return

            for i in range(start, len(candidates)):
                candidate = candidates[i]
                combination.append(candidate)  # Choose the candidate
                # Recursively explore further with the chosen candidate
                backtrack(
                    remaining - candidate, combination, i
                )  # Not i + 1 because we can reuse the same element
                combination.pop()  # Un-choose the candidate (backtrack)

        candidates.sort()  # Sort to optimize the process
        backtrack(target, [], 0)

        return result


sol = Solution()
sol.combinationSum([2, 3, 6, 7], 7)
