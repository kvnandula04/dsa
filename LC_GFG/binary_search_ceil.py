class Solution:
    def findCeil(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        smallest_num_index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] >= target:
                smallest_num_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return smallest_num_index


# Test case 1: Target is smaller than the smallest element in the array
test_case_1 = {"nums": [1, 2, 8, 10, 11, 12, 19], "target": 0}
print(Solution().findCeil(test_case_1["nums"], test_case_1["target"]))
# Expected output: 0 (index of 1, which is the smallest number larger than or equal to 0)

# Test case 2: Target is larger than the largest element in the array
test_case_2 = {"nums": [1, 2, 8, 10, 11, 12, 19], "target": 20}
print(Solution().findCeil(test_case_2["nums"], test_case_2["target"]))
# Expected output: -1 (no element in the array is larger than or equal to 20)

# Test case 3: Target is equal to an element in the array
test_case_3 = {"nums": [1, 2, 8, 10, 11, 12, 19], "target": 8}
print(Solution().findCeil(test_case_3["nums"], test_case_3["target"]))
# Expected output: 2 (index of 8, which is the smallest number larger than or equal to 8)

# Test case 4: Target is between two elements in the array
test_case_4 = {"nums": [1, 2, 8, 10, 11, 12, 19], "target": 9}
print(Solution().findCeil(test_case_4["nums"], test_case_4["target"]))
# Expected output: 3 (index of 10, which is the smallest number larger than or equal to 9)

# Test case 5: Target is the smallest element in the array
test_case_5 = {"nums": [1, 2, 8, 10, 11, 12, 19], "target": 1}
print(Solution().findCeil(test_case_5["nums"], test_case_5["target"]))
# Expected output: 0 (index of 1, which is the smallest number larger than or equal to 1)

# Test case 6: Target is the largest element in the array
test_case_6 = {"nums": [1, 2, 8, 10, 11, 12, 19], "target": 19}
print(Solution().findCeil(test_case_6["nums"], test_case_6["target"]))
# Expected output: 6 (index of 19, which is the smallest number larger than or equal to 19)

# Test case 7: Array contains only one element, and it's smaller than the target
test_case_7 = {"nums": [5], "target": 6}
print(Solution().findCeil(test_case_7["nums"], test_case_7["target"]))
# Expected output: -1 (no element is larger than or equal to 6)

# Test case 8: Array contains only one element, and it's equal to the target
test_case_8 = {"nums": [7], "target": 7}
print(Solution().findCeil(test_case_8["nums"], test_case_8["target"]))
# Expected output: 0 (index of 7, which is the smallest number larger than or equal to 7)

# Test case 9: Array contains only one element, and it's larger than the target
test_case_9 = {"nums": [10], "target": 5}
print(Solution().findCeil(test_case_9["nums"], test_case_9["target"]))
# Expected output: 0 (index of 10, which is the smallest number larger than or equal to 5)

# Test case 10: Target is not in the list, and all elements are smaller
test_case_10 = {"nums": [2, 4, 6, 8, 10], "target": 11}
print(Solution().findCeil(test_case_10["nums"], test_case_10["target"]))
# Expected output: -1 (no element is larger than or equal to 11)
