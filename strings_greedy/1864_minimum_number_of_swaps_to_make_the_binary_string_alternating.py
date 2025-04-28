"""
LeetCode Question #1864: Minimum Number of Swaps to Make the Binary String Alternating

Problem Statement:
A binary string is a string consisting only of the characters '0' and '1'. 
A binary string is alternating if no two adjacent characters are equal. 
For example, "010" and "101" are alternating, while "0100" and "1010" are not.

Given a binary string `s`, return the minimum number of swaps required to make it alternating, 
or -1 if it is impossible. A swap consists of choosing two indices `i` and `j` (0-indexed) 
and swapping `s[i]` with `s[j]`.

Example 1:
Input: s = "111000"
Output: 1
Explanation: Swap s[1] and s[4] to make s = "101010".

Example 2:
Input: s = "010"
Output: 0
Explanation: The string is already alternating.

Example 3:
Input: s = "1110"
Output: -1
Explanation: No matter how many swaps you make, it is impossible to make the string alternating.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

# Python Solution
def minSwaps(s: str) -> int:
    def count_mismatches(s: str, pattern: str) -> int:
        """Helper function to count mismatches with a given pattern."""
        mismatches = 0
        for i in range(len(s)):
            if s[i] != pattern[i % 2]:
                mismatches += 1
        return mismatches

    # Count the number of 0s and 1s in the string
    count_0 = s.count('0')
    count_1 = len(s) - count_0

    # If the difference between counts is greater than 1, it's impossible to make the string alternating
    if abs(count_0 - count_1) > 1:
        return -1

    # Generate alternating patterns
    pattern1 = "01" * (len(s) // 2) + "0" * (len(s) % 2)  # Alternating starting with '0'
    pattern2 = "10" * (len(s) // 2) + "1" * (len(s) % 2)  # Alternating starting with '1'

    # Calculate mismatches for both patterns
    if count_0 == count_1:
        mismatches1 = count_mismatches(s, pattern1)
        mismatches2 = count_mismatches(s, pattern2)
        return min(mismatches1, mismatches2) // 2
    elif count_0 > count_1:
        mismatches1 = count_mismatches(s, pattern1)
        return mismatches1 // 2
    else:
        mismatches2 = count_mismatches(s, pattern2)
        return mismatches2 // 2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "111000"
    print(minSwaps(s1))  # Output: 1

    # Test Case 2
    s2 = "010"
    print(minSwaps(s2))  # Output: 0

    # Test Case 3
    s3 = "1110"
    print(minSwaps(s3))  # Output: -1

    # Test Case 4
    s4 = "1001"
    print(minSwaps(s4))  # Output: 1

    # Test Case 5
    s5 = "000111"
    print(minSwaps(s5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the number of '0's and '1's in the string takes O(n).
- Generating the alternating patterns takes O(n).
- Counting mismatches with the patterns takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables and not allocating extra space proportional to the input size.

Topic: Strings, Greedy
"""