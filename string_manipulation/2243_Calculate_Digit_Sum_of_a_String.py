"""
LeetCode Problem #2243: Calculate Digit Sum of a String

Problem Statement:
You are given a string `s` consisting of digits and an integer `k`.

A round consists of processing the string `s` as follows:
1. Divide `s` into consecutive groups of size `k`. The last group may be smaller than `k`.
2. Replace each group of `s` with the sum of its digits. Convert the resulting sums into a new string.
3. Repeat the process until the string's length is less than or equal to `k`.

Return `s` after all rounds have been completed.

Example:
Input: s = "1111122222", k = 3
Output: "36"

Constraints:
- 1 <= s.length <= 100
- 1 <= k <= 100
- s consists of digits only.
"""

def digitSum(s: str, k: int) -> str:
    """
    Calculate the digit sum of a string until its length is less than or equal to k.

    :param s: A string consisting of digits.
    :param k: An integer representing the group size.
    :return: The resulting string after all rounds.
    """
    while len(s) > k:
        new_s = ""
        for i in range(0, len(s), k):
            group = s[i:i+k]
            group_sum = sum(int(char) for char in group)
            new_s += str(group_sum)
        s = new_s
    return s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1111122222"
    k1 = 3
    print(digitSum(s1, k1))  # Expected Output: "36"

    # Test Case 2
    s2 = "987654321"
    k2 = 2
    print(digitSum(s2, k2))  # Expected Output: "46"

    # Test Case 3
    s3 = "123456789"
    k3 = 4
    print(digitSum(s3, k3))  # Expected Output: "30"

    # Test Case 4
    s4 = "1"
    k4 = 1
    print(digitSum(s4, k4))  # Expected Output: "1"

    # Test Case 5
    s5 = "99999"
    k5 = 2
    print(digitSum(s5, k5))  # Expected Output: "45"

"""
Time and Space Complexity Analysis:

Time Complexity:
- In each round, we iterate through the string `s` in chunks of size `k`.
- The number of rounds is proportional to the logarithm of the length of `s` (base k), as the string size reduces significantly in each round.
- Therefore, the time complexity is O(n), where `n` is the initial length of the string.

Space Complexity:
- The space complexity is O(n), as we create a new string `new_s` in each round to store the intermediate results.

Topic: String Manipulation
"""