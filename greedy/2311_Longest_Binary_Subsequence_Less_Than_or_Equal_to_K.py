"""
LeetCode Problem #2311: Longest Binary Subsequence Less Than or Equal to K

Problem Statement:
You are given a binary string `s` and a positive integer `k`.

Return the length of the longest subsequence of `s` that makes up a binary number less than or equal to `k`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Constraints:
- 1 <= s.length <= 1000
- s consists of only '0' and '1'.
- 1 <= k <= 10^9
"""

def longestSubsequence(s: str, k: int) -> int:
    """
    Finds the length of the longest subsequence of the binary string `s` 
    that represents a binary number less than or equal to `k`.
    """
    # Count all '0's since they contribute 0 to the binary value
    count_zeros = s.count('0')
    # Start with the count of zeros as they can always be included
    result = count_zeros
    value = 0
    power = 1

    # Traverse the string in reverse to consider the least significant bits first
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '1':
            # Check if adding this '1' keeps the value <= k
            if value + power <= k:
                result += 1
                value += power
            # Update the power of 2 for the next bit
            power *= 2
            # If power exceeds k, no further '1's can be added
            if power > k:
                break

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1001010"
    k1 = 5
    print(longestSubsequence(s1, k1))  # Expected Output: 5

    # Test Case 2
    s2 = "00101001"
    k2 = 1
    print(longestSubsequence(s2, k2))  # Expected Output: 6

    # Test Case 3
    s3 = "1111"
    k3 = 8
    print(longestSubsequence(s3, k3))  # Expected Output: 4

    # Test Case 4
    s4 = "0000"
    k4 = 10
    print(longestSubsequence(s4, k4))  # Expected Output: 4

    # Test Case 5
    s5 = "1010101010"
    k5 = 10
    print(longestSubsequence(s5, k5))  # Expected Output: 7

"""
Time Complexity:
- Counting zeros takes O(n), where n is the length of the string `s`.
- The reverse traversal of the string also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy
"""