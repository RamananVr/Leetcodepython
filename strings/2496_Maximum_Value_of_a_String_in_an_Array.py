"""
LeetCode Problem #2496: Maximum Value of a String in an Array

Problem Statement:
You are given an array of strings `strs`. Each string can be either a numeric string or a non-numeric string.

- A numeric string is a string consisting only of digits.
- A non-numeric string is a string that contains at least one letter.

The value of a string is defined as follows:
- If the string is a numeric string, its value is its numeric value (i.e., the integer representation of the string).
- If the string is a non-numeric string, its value is the length of the string.

Return the maximum value among all the strings in the array.

Example:
Input: strs = ["123", "abc", "456", "de"]
Output: 456

Constraints:
- 1 <= strs.length <= 100
- 1 <= strs[i].length <= 10
- strs[i] consists of only lowercase English letters and digits.
"""

# Solution
def maximumValue(strs):
    """
    Function to find the maximum value of a string in an array.

    :param strs: List[str] - Array of strings
    :return: int - Maximum value among all strings
    """
    def get_value(s):
        # Check if the string is numeric
        if s.isdigit():
            return int(s)
        else:
            return len(s)
    
    # Compute the maximum value using the helper function
    return max(get_value(s) for s in strs)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["123", "abc", "456", "de"]
    print(maximumValue(strs1))  # Output: 456

    # Test Case 2
    strs2 = ["1", "a", "22", "bb", "333"]
    print(maximumValue(strs2))  # Output: 333

    # Test Case 3
    strs3 = ["hello", "world", "42", "9999"]
    print(maximumValue(strs3))  # Output: 9999

    # Test Case 4
    strs4 = ["a", "b", "c", "1", "2", "3"]
    print(maximumValue(strs4))  # Output: 1

    # Test Case 5
    strs5 = ["12345", "abcde", "678", "xyz"]
    print(maximumValue(strs5))  # Output: 12345

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through each string in the array `strs` (O(n), where n is the number of strings).
- For each string, it checks if the string is numeric (O(k), where k is the length of the string).
- Therefore, the overall time complexity is O(n * k), where n is the number of strings and k is the average length of the strings.

Space Complexity:
- The function uses constant space for computation (O(1)).
- The generator expression used in `max()` does not store intermediate results, so no additional space is required.
- Therefore, the space complexity is O(1).

Topic: Strings
"""