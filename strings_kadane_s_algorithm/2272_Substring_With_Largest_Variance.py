"""
LeetCode Problem #2272: Substring With Largest Variance

Problem Statement:
The variance of a string is defined as the largest difference between the number of occurrences of any two characters present in the string. 
Given a string `s` consisting of lowercase English letters only, return the largest variance of any substring of `s`.

A substring is a contiguous sequence of characters within a string.

Example 1:
Input: s = "aababbb"
Output: 3
Explanation: All possible variances are:
- "aababbb" -> Variance is 3 (b: 4, a: 1)
- "ababbb" -> Variance is 3 (b: 4, a: 1)
- "babbb" -> Variance is 3 (b: 4, a: 1)
- "abbb" -> Variance is 3 (b: 3, a: 0)
- "bbb" -> Variance is 0 (b: 3, a: 0)
- "aabab" -> Variance is 2 (a: 3, b: 1)
- And so on...

Example 2:
Input: s = "abcde"
Output: 0
Explanation: No two characters appear more than once, so the variance is 0.

Constraints:
- 1 <= s.length <= 10^4
- s consists of lowercase English letters.

Follow-up:
Can you solve the problem in O(n^2) time complexity?

"""

def largestVariance(s: str) -> int:
    """
    Function to calculate the largest variance of any substring of the given string `s`.
    """
    from itertools import permutations

    # Get all unique characters in the string
    unique_chars = set(s)
    max_variance = 0

    # Iterate over all pairs of characters (a, b)
    for a, b in permutations(unique_chars, 2):
        # Initialize variables for Kadane's algorithm
        current_variance = 0
        has_b = False
        first_b = False

        for char in s:
            if char == a:
                current_variance += 1
            elif char == b:
                current_variance -= 1
                has_b = True
                if not first_b:
                    first_b = True
                    # Reset current_variance to ensure at least one 'b' is included
                    current_variance = max(current_variance, -1)

            # Update max_variance if we have seen at least one 'b'
            if has_b:
                max_variance = max(max_variance, current_variance)

            # Reset current_variance if it drops below 0
            if current_variance < 0:
                current_variance = 0
                has_b = False

    return max_variance


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aababbb"
    print(f"Input: {s1} -> Output: {largestVariance(s1)}")  # Expected Output: 3

    # Test Case 2
    s2 = "abcde"
    print(f"Input: {s2} -> Output: {largestVariance(s2)}")  # Expected Output: 0

    # Test Case 3
    s3 = "aaaaa"
    print(f"Input: {s3} -> Output: {largestVariance(s3)}")  # Expected Output: 0

    # Test Case 4
    s4 = "ab"
    print(f"Input: {s4} -> Output: {largestVariance(s4)}")  # Expected Output: 1

    # Test Case 5
    s5 = "ababab"
    print(f"Input: {s5} -> Output: {largestVariance(s5)}")  # Expected Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all pairs of unique characters in the string. 
  There are at most 26 * 25 = 650 pairs (since there are 26 lowercase English letters).
- For each pair, we perform a single pass over the string (O(n)).
- Thus, the overall time complexity is O(650 * n) = O(n), where n is the length of the string.

Space Complexity:
- The space complexity is O(1) as we use a constant amount of extra space for variables.

Primary Topic: Strings, Kadane's Algorithm
"""