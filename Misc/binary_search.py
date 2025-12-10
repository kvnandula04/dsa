class Solution:
    def search(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        mid = left + (right - left) // 2

        while left <= right:
            if nums[mid] == target:
                return mid
            elif target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

            mid = left + (right - left) // 2

        return -1


# Test case 1: Target is present in the middle of the list
test_case_1 = {"nums": [1, 2, 3, 4, 5, 6, 7, 8, 9], "target": 5}
print(Solution().search(test_case_1["nums"], test_case_1["target"]))
# Expected output: 4 (index of target)

# Test case 2: Target is the first element
test_case_2 = {"nums": [1, 3, 5, 7, 9, 11], "target": 1}
print(Solution().search(test_case_2["nums"], test_case_2["target"]))
# Expected output: 0 (index of target)

# Test case 3: Target is the last element
test_case_3 = {"nums": [10, 20, 30, 40, 50], "target": 50}
print(Solution().search(test_case_3["nums"], test_case_3["target"]))
# Expected output: 4 (index of target)

# Test case 4: Target is not in the list
test_case_4 = {"nums": [2, 4, 6, 8, 10], "target": 7}
print(Solution().search(test_case_4["nums"], test_case_4["target"]))
# Expected output: -1 (target not found)

# Test case 5: List has only one element, and it's the target
test_case_5 = {"nums": [7], "target": 7}
print(Solution().search(test_case_5["nums"], test_case_5["target"]))
# Expected output: 0 (index of target)

# Test case 6: List has only one element, but it's not the target
test_case_6 = {"nums": [10], "target": 5}
print(Solution().search(test_case_6["nums"], test_case_6["target"]))
# Expected output: -1 (target not found)

# Test case 7: Target is not in the list, and the list is empty
test_case_7 = {"nums": [], "target": 3}
print(Solution().search(test_case_7["nums"], test_case_7["target"]))
# Expected output: -1 (target not found)

# Test case 8: Target is present at the beginning of a large list
test_case_8 = {"nums": list(range(1000)), "target": 0}
print(Solution().search(test_case_8["nums"], test_case_8["target"]))
# Expected output: 0 (index of target)

# Test case 9: Target is present at the end of a large list
test_case_9 = {"nums": list(range(1000)), "target": 999}
print(Solution().search(test_case_9["nums"], test_case_9["target"]))
# Expected output: 999 (index of target)

# Test case 10: Target is present somewhere in the middle of a large list
test_case_10 = {"nums": list(range(1000)), "target": 500}
print(Solution().search(test_case_10["nums"], test_case_10["target"]))
# Expected output: 500 (index of target)
