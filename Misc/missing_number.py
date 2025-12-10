class Solution:

    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        our_sum = 0
        expected_sum = (n * (n + 1)) / 2
        for i in range(n - 1):
            our_sum += arr[i]

        return expected_sum - our_sum


def test_find_missing_number():
    sol = Solution()
    # Test Case 1: Missing middle element
    arr1 = [1, 2, 4, 5, 6]
    n1 = 6
    assert sol.missingNumber(n1, arr1) == 3, f"Test Case 1 Failed"

    # # Test Case 2: Missing first element
    # arr2 = [2, 3, 4, 5]
    # n2 = 5
    # assert sol.missingNumber(n2, arr2) == 1, f"Test Case 2 Failed"

    # # Test Case 3: Missing last element
    # arr3 = [1, 2, 3, 4]
    # n3 = 5
    # assert sol.missingNumber(n3, arr3) == 5, f"Test Case 3 Failed"

    # Test Case 4: Missing element in larger array
    arr4 = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    n4 = 10
    assert sol.missingNumber(n4, arr4) == 4, f"Test Case 4 Failed"

    # Test Case 5: Array with only two elements (edge case)
    arr5 = [2]
    n5 = 2
    assert sol.missingNumber(n5, arr5) == 1, f"Test Case 5 Failed"

    # Test Case 6: Missing random element
    arr6 = [3, 7, 1, 2, 8, 4, 5]
    n6 = 8
    assert sol.missingNumber(n6, arr6) == 6, f"Test Case 6 Failed"

    print("All test cases passed!")


# Run the test cases
test_find_missing_number()
