"""
LeetCode Problem #2522: Partition String Into Substrings With Values at Most K

Problem Statement:
You are given a string `s` consisting of digits from '1' to '9' and an integer `k`.

A partition of the string `s` is called valid if:

1. Each substring in the partition is a positive integer and does not have leading zeros.
2. The value of each substring is less than or equal to `k`.

Return the minimum number of substrings in a valid partition. If it is not possible to partition the string `s` as described, return -1.

Example 1:
Input: s = "165462", k = 60
Output: 4
Explanation: We can partition the string into "16", "54", "6", "2". Each substring has a value less than or equal to k = 60.

Example 2:
Input: s = "238182", k = 5
Output: -1
Explanation: There is no valid partition because the value of each substring must be at most k = 5.

Constraints:
- 1 <= s.length <= 1000
- s consists of digits from '1' to '9'.
- 1 <= k <= 10^9
"""

def minimumPartition(s: str, k: int) -> int:
    """
    Function to find the minimum number of substrings in a valid partition of the string `s`.
    If it's not possible to partition the string, return -1.
    """
    n = len(s)
    count = 0
    current_value = 0

    for char in s:
        digit = int(char)
        if digit > k:
            return -1  # If any single digit is greater than k, partitioning is impossible.
        
        # Try to extend the current substring
        if current_value * 10 + digit <= k:
            current_value = current_value * 10 + digit
        else:
            # Start a new substring
            count += 1
            current_value = digit

    # Count the last substring
    return count + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1 = "165462", 60
    print(minimumPartition(s1, k1))  # Expected Output: 4

    # Test Case 2
    s2, k2 = "238182", 5
    print(minimumPartition(s2, k2))  # Expected Output: -1

    # Test Case 3
    s3, k3 = "123456789", 100
    print(minimumPartition(s3, k3))  # Expected Output: 9

    # Test Case 4
    s4, k4 = "11111", 10
    print(minimumPartition(s4, k4))  # Expected Output: 5

    # Test Case 5
    s5, k5 = "1", 1
    print(minimumPartition(s5, k5))  # Expected Output: 1

"""
Time Complexity Analysis:
- The function iterates through the string `s` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string `s`.

Space Complexity Analysis:
- The function uses a constant amount of extra space for variables like `current_value` and `count`.
- Therefore, the space complexity is O(1).

Topic: Greedy Algorithm
"""