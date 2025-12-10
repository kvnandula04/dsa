class Solution:
    def encode(self, s: str) -> str:
        if len(s) == 0:
            return ""

        dictionary = dict()
        prev_char = s[0]
        count = 0

        output = ""

        for i in range(len(s)):
            if s[i] == prev_char:
                count += 1
            else:
                if prev_char in dictionary:
                    dictionary[prev_char] += count
                else:
                    dictionary[prev_char] = count

                prev_char = s[i]
                count = 1

        # Add the last character to the dictionary
        if prev_char in dictionary:
            dictionary[prev_char] += count
        else:
            dictionary[prev_char] = count

        # Construct the output string
        for letter, count in dictionary.items():
            output += letter + str(count)

        return output


def test_encode_variant():
    solution = Solution()

    # Test Case 1: Simple case with repeating characters
    s1 = "aaabbcddaabb"
    expected_output1 = "a5b4c1d2"
    assert solution.encode(s1) == expected_output1, "Test Case 1 Failed"

    # Test Case 2: Mixed case with single and repeating characters
    s2 = "abbbcdddda"
    expected_output2 = "a2b3c1d4"
    assert solution.encode(s2) == expected_output2, "Test Case 2 Failed"

    # Test Case 3: All characters are the same
    s3 = "zzzzzzzzzz"
    expected_output3 = "z10"
    assert solution.encode(s3) == expected_output3, "Test Case 3 Failed"

    # Test Case 4: Alternating characters (no consecutive repeats)
    s4 = "abcd"
    expected_output4 = "a1b1c1d1"
    assert solution.encode(s4) == expected_output4, "Test Case 4 Failed"

    # Test Case 5: Empty string
    s5 = ""
    expected_output5 = ""
    assert solution.encode(s5) == expected_output5, "Test Case 5 Failed"

    # Test Case 6: Single character string
    s6 = "a"
    expected_output6 = "a1"
    assert solution.encode(s6) == expected_output6, "Test Case 6 Failed"

    # Test Case 7: String with different characters repeating
    s7 = "wwwwaaadexxxxxx"
    expected_output7 = "w4a3d1e1x6"
    assert solution.encode(s7) == expected_output7, "Test Case 7 Failed"

    # Test Case 8: Longer string with varying lengths of repeats
    s8 = "aabbccccdddddeeeffffggggg"
    expected_output8 = "a2b2c4d5e3f4g5"
    assert solution.encode(s8) == expected_output8, "Test Case 8 Failed"

    # Test Case 9: String with special characters
    s9 = "!!!$$$%%%^^^&&&"
    expected_output9 = "!3$3%3^3&3"
    assert solution.encode(s9) == expected_output9, "Test Case 9 Failed"

    # Test Case 10: Case with no repetitions but larger input
    s10 = "abcdefghij"
    expected_output10 = "a1b1c1d1e1f1g1h1i1j1"
    assert solution.encode(s10) == expected_output10, "Test Case 10 Failed"

    print("All test cases passed!")


# Run the test cases
test_encode_variant()
