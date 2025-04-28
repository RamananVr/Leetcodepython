"""
LeetCode Question #2222: Number of Ways to Select Buildings

Problem Statement:
You are given a 0-indexed binary string `s` which represents the types of buildings along a street where:
- `s[i] = '0'` indicates that the ith building is an office.
- `s[i] = '1'` indicates that the ith building is a restaurant.

As a city planner, you would like to select 3 buildings to form a valid sequence. A valid sequence is any sequence of buildings that contains exactly one office and two restaurants or exactly two offices and one restaurant. 

Return the number of valid sequences of buildings.

Constraints:
- `3 <= s.length <= 10^5`
- `s[i]` is either `'0'` or `'1'`.

"""

# Solution
def numberOfWays(s: str) -> int:
    # Initialize counters
    count_0 = 0  # Count of '0's seen so far
    count_1 = 0  # Count of '1's seen so far
    count_01 = 0  # Count of "01" pairs
    count_10 = 0  # Count of "10" pairs
    result = 0  # Final result

    # Iterate through the string
    for char in s:
        if char == '0':
            # If current character is '0', it can form "10" pairs with previous '1's
            result += count_10
            # Update "01" pairs count since this '0' can form "01" pairs with previous '1's
            count_01 += count_1
            # Increment count of '0's
            count_0 += 1
        elif char == '1':
            # If current character is '1', it can form "01" pairs with previous '0's
            result += count_01
            # Update "10" pairs count since this '1' can form "10" pairs with previous '0's
            count_10 += count_0
            # Increment count of '1's
            count_1 += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "001101"
    print(numberOfWays(s1))  # Expected Output: 6

    # Test Case 2
    s2 = "11100"
    print(numberOfWays(s2))  # Expected Output: 0

    # Test Case 3
    s3 = "010101"
    print(numberOfWays(s3))  # Expected Output: 12

    # Test Case 4
    s4 = "000111"
    print(numberOfWays(s4))  # Expected Output: 0

    # Test Case 5
    s5 = "10101"
    print(numberOfWays(s5))  # Expected Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the string `s` exactly once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where `n` is the length of the string.

Space Complexity:
- The solution uses a constant amount of extra space to store counters (`count_0`, `count_1`, `count_01`, `count_10`, and `result`).
- Therefore, the space complexity is O(1).

Topic: Strings, Prefix Sums
"""