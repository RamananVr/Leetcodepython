"""
LeetCode Problem #2914: Minimum Number of Changes to Make Binary String Beautiful

You are given a 0-indexed binary string `s` having an even length.
A string is called **beautiful** if it's possible to partition it into one or more substrings of even length such that all characters in each substring are identical. For example, the strings `"11001111"` and `"0000"` are beautiful, but `"1010"` and `"11001"` are not.
You can change any character in `s` to either `'0'` or `'1'`.
Return the minimum number of changes required to make the string `s` beautiful.
"""

# Problem Statement:
"""
Given a binary string `s` of even length, find the minimum number of character changes needed so that the string can be partitioned into substrings of even length where each substring contains only identical characters (all '0's or all '1's).

Example 1:
Input: s = "1001"
Output: 2
Explanation: Change s[1] to '1' and s[3] to '0' -> "1100". Partition: "11", "00". Cost = 2.

Example 2:
Input: s = "10"
Output: 1
Explanation: Change s[1] to '1' -> "11". Partition: "11". Cost = 1.

Example 3:
Input: s = "0000"
Output: 0
Explanation: Already beautiful. Partition: "00", "00" (or "0000"). Cost = 0.

Constraints:
- 2 <= s.length <= 10^5
- s.length is even.
- s consists only of characters '0' and '1'.
"""

# Solution:
"""
The core idea is that the simplest way to make the string beautiful is to ensure it can be partitioned into substrings of length 2, where each substring has identical characters.
We can iterate through the string in steps of 2, looking at pairs of characters (s[i], s[i+1]).
If s[i] is different from s[i+1], we need exactly one change within that pair to make them identical (e.g., change s[i+1] to match s[i], or vice-versa).
If s[i] is the same as s[i+1], no change is needed for that pair.
The total number of changes required is the count of pairs (s[i], s[i+1]) where s[i] != s[i+1].
"""


def minChanges(self, s: str) -> int:
    """
    Calculates the minimum changes to make a binary string beautiful.

    Args:
        s: The input binary string of even length.

    Returns:
        The minimum number of changes required.
    """
    changes = 0
    n = len(s)
    # Iterate through the string in steps of 2
    for i in range(0, n, 2):
        # Check pairs (s[i], s[i+1])
        if s[i] != s[i+1]:
            changes += 1
    return changes

# Example Test Cases
if __name__ == "__main__":
    

    # Test Case 1
    input_data_1 = "1001"
    expected_output_1 = 2
    result1 = minChanges(input_data_1)
    assert result1 == expected_output_1, f"Test Case 1 Failed: Expected {expected_output_1}, Got {result1}"
    print(f"Test Case 1 (s={input_data_1}): Result = {result1}")

    # Test Case 2
    input_data_2 = "10"
    expected_output_2 = 1
    result2 = minChanges(input_data_2)
    assert result2 == expected_output_2, f"Test Case 2 Failed: Expected {expected_output_2}, Got {result2}"
    print(f"Test Case 2 (s={input_data_2}): Result = {result2}")

    # Test Case 3
    input_data_3 = "0000"
    expected_output_3 = 0
    result3 = minChanges(input_data_3)
    assert result3 == expected_output_3, f"Test Case 3 Failed: Expected {expected_output_3}, Got {result3}"
    print(f"Test Case 3 (s={input_data_3}): Result = {result3}")

    # Test Case 4
    input_data_4 = "111111"
    expected_output_4 = 0
    result4 = minChanges(input_data_4)
    assert result4 == expected_output_4, f"Test Case 4 Failed: Expected {expected_output_4}, Got {result4}"
    print(f"Test Case 4 (s={input_data_4}): Result = {result4}")

    # Test Case 5
    input_data_5 = "011001" # (0,1)->1, (1,0)->1, (0,1)->1
    expected_output_5 = 3
    result5 = minChanges(input_data_5)
    assert result5 == expected_output_5, f"Test Case 5 Failed: Expected {expected_output_5}, Got {result5}"
    print(f"Test Case 5 (s={input_data_5}): Result = {result5}")

    print("\nAll provided test cases passed!")


"""
Time and Space Complexity Analysis:
Time Complexity: O(N), where N is the length of the string `s`. We iterate through the string once with a step of 2.
Space Complexity: O(1), as we only use a constant amount of extra space for variables like `changes` and the loop index `i`.

Topic: String, Greedy
"""