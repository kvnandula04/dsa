class Solution:
    def findFloor(self, nums, target) -> int:
        left = 0
        right = len(nums) - 1
        largest_num_index = -1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] <= target:
                largest_num_index = mid
                left = mid + 1
            else:
                right = mid - 1

        return largest_num_index


# Test case 1: Target is smaller than all elements in the array
test_case_1 = {"arr": [1, 2, 8, 10, 11, 12, 19], "x": 0}
print(Solution().findFloor(test_case_1["arr"], test_case_1["x"]))
# Expected output: -1 (no element <= 0)

# Test case 2: Target is between two elements in the array
test_case_2 = {"arr": [1, 2, 8, 10, 11, 12, 19], "x": 5}
print(Solution().findFloor(test_case_2["arr"], test_case_2["x"]))
# Expected output: 1 (index of element 2, as 2 is the largest element <= 5)

# Test case 3: Target is larger than all elements in the array
test_case_3 = {"arr": [1, 2, 8, 10, 11, 12, 19], "x": 20}
print(Solution().findFloor(test_case_3["arr"], test_case_3["x"]))
# Expected output: 6 (index of element 19, as 19 is the largest element <= 20)

# Test case 4: Target is equal to an element in the array
test_case_4 = {"arr": [1, 2, 8, 10, 11, 12, 19], "x": 8}
print(Solution().findFloor(test_case_4["arr"], test_case_4["x"]))
# Expected output: 2 (index of element 8, as 8 is the largest element <= 8)

# Test case 5: Array has only one element, and it is less than target
test_case_5 = {"arr": [7], "x": 10}
print(Solution().findFloor(test_case_5["arr"], test_case_5["x"]))
# Expected output: 0 (index of element 7, as 7 is the largest element <= 10)

# Test case 6: Array has only one element, and it is greater than target
test_case_6 = {"arr": [10], "x": 5}
print(Solution().findFloor(test_case_6["arr"], test_case_6["x"]))
# Expected output: -1 (no element <= 5)

# Test case 7: Target is not in the list and smaller than all elements in a large array
test_case_7 = {"arr": list(range(100, 200)), "x": 50}
print(Solution().findFloor(test_case_7["arr"], test_case_7["x"]))
# Expected output: -1 (no element <= 50)

# Test case 8: Target is present at the beginning of a large array
test_case_8 = {"arr": list(range(1000)), "x": 0}
print(Solution().findFloor(test_case_8["arr"], test_case_8["x"]))
# Expected output: 0 (index of element 0, as 0 is the largest element <= 0)

# Test case 9: Target is present at the end of a large array
test_case_9 = {"arr": list(range(1000)), "x": 999}
print(Solution().findFloor(test_case_9["arr"], test_case_9["x"]))
# Expected output: 999 (index of element 999, as 999 is the largest element <= 999)

# Test case 10: Target is in the middle of a large array
test_case_10 = {"arr": list(range(1000)), "x": 500}
print(Solution().findFloor(test_case_10["arr"], test_case_10["x"]))
# Expected output: 500 (index of element 500, as 500 is the largest element <= 500)
