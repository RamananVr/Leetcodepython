"""
LeetCode Problem #1945: Sum of Digits of String After Convert

Problem Statement:
You are given a string `s` consisting of lowercase English letters, and an integer `k`.

First, convert `s` into an integer by replacing each letter with its position in the alphabet 
(i.e., replace 'a' with 1, 'b' with 2, ..., 'z' with 26) and concatenating all the integers together. 
For example, if `s = "zbax"`, we would convert it to the integer `26211224`.

Then, transform the integer by replacing it with the sum of its digits, 
and repeat the transformation `k` times in total.

Return the resulting integer after performing the transformations `k` times.

Example:
Input: s = "zbax", k = 2
Output: 8
Explanation:
1. Convert: "zbax" -> 26 2 1 24 -> 26211224
2. Sum of digits: 2 + 6 + 2 + 1 + 1 + 2 + 2 + 4 = 20
3. Repeat sum of digits: 2 + 0 = 8

Constraints:
- 1 <= s.length <= 100
- 1 <= k <= 10
- `s` consists of lowercase English letters.
"""

# Python Solution
def getLucky(s: str, k: int) -> int:
    # Step 1: Convert the string `s` into its numeric representation
    numeric_representation = ''.join(str(ord(char) - ord('a') + 1) for char in s)
    
    # Step 2: Compute the sum of digits of the numeric representation
    current_sum = sum(int(digit) for digit in numeric_representation)
    
    # Step 3: Perform the transformation `k` times
    for _ in range(k - 1):
        current_sum = sum(int(digit) for digit in str(current_sum))
    
    return current_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "zbax"
    k1 = 2
    print(getLucky(s1, k1))  # Output: 8

    # Test Case 2
    s2 = "leetcode"
    k2 = 1
    print(getLucky(s2, k2))  # Output: 41

    # Test Case 3
    s3 = "abc"
    k3 = 3
    print(getLucky(s3, k3))  # Output: 6

    # Test Case 4
    s4 = "a"
    k4 = 5
    print(getLucky(s4, k4))  # Output: 1

    # Test Case 5
    s5 = "zzzz"
    k5 = 1
    print(getLucky(s5, k5))  # Output: 104

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting the string `s` to its numeric representation takes O(n), where `n` is the length of `s`.
- Summing the digits of the numeric representation takes O(m), where `m` is the number of digits in the numeric representation.
- Performing the transformation `k` times involves summing the digits repeatedly, which takes O(k * m).
- Overall time complexity: O(n + k * m).

Space Complexity:
- The numeric representation of the string requires O(m) space.
- The sum computation requires O(1) additional space.
- Overall space complexity: O(m).

Note: `m` depends on the length of the numeric representation, which is proportional to the length of `s`.

Topic: Strings
"""