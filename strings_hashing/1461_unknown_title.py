"""
LeetCode Problem #1461: Check If a String Contains All Binary Codes of Size K

Problem Statement:
Given a binary string `s` and an integer `k`, return `True` if every binary code of length `k` is a substring of `s`. Otherwise, return `False`.

Example 1:
Input: s = "00110110", k = 2
Output: True
Explanation: The binary codes of length 2 are "00", "01", "10", and "11". They can all be found as substrings at indices 0, 1, 3, and 2 respectively.

Example 2:
Input: s = "0110", k = 1
Output: True
Explanation: The binary codes of length 1 are "0" and "1", and they both exist as substrings.

Example 3:
Input: s = "0110", k = 2
Output: False
Explanation: The binary code "00" is missing.

Constraints:
- 1 <= s.length <= 5 * 10^5
- s[i] is either '0' or '1'.
- 1 <= k <= 20
"""

def hasAllCodes(s: str, k: int) -> bool:
    """
    Check if a binary string contains all binary codes of size k.

    Args:
    s (str): The binary string.
    k (int): The size of binary codes to check.

    Returns:
    bool: True if all binary codes of size k are substrings of s, False otherwise.
    """
    # The total number of unique binary codes of size k
    total_codes = 1 << k  # Equivalent to 2^k

    # A set to store all unique substrings of length k
    seen = set()

    # Iterate through the string to extract all substrings of length k
    for i in range(len(s) - k + 1):
        # Add the substring of length k to the set
        seen.add(s[i:i + k])

        # If we've seen all possible codes, return True early
        if len(seen) == total_codes:
            return True

    # If we exit the loop and haven't seen all codes, return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "00110110"
    k1 = 2
    print(hasAllCodes(s1, k1))  # Expected Output: True

    # Test Case 2
    s2 = "0110"
    k2 = 1
    print(hasAllCodes(s2, k2))  # Expected Output: True

    # Test Case 3
    s3 = "0110"
    k3 = 2
    print(hasAllCodes(s3, k3))  # Expected Output: False

    # Test Case 4
    s4 = "0000000001011100"
    k4 = 4
    print(hasAllCodes(s4, k4))  # Expected Output: False

    # Test Case 5
    s5 = "1111000011110000"
    k5 = 3
    print(hasAllCodes(s5, k5))  # Expected Output: True

"""
Time Complexity Analysis:
- Extracting all substrings of length k takes O(n), where n is the length of the string `s`.
- Adding each substring to the set and checking its size is O(1) on average.
- In the worst case, we iterate through the entire string, so the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(2^k) because the set `seen` can store at most 2^k unique binary codes of length k.
- In addition, the input string `s` and integer `k` are stored, but their space usage is negligible compared to the set.

Primary Topic: Strings, Hashing
"""