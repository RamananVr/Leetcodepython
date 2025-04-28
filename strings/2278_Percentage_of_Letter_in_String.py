"""
LeetCode Problem #2278: Percentage of Letter in String

Problem Statement:
Given a string `s` and a character `letter`, return the percentage of characters in the string `s` that are equal to `letter` rounded down to the nearest whole number.

Example 1:
Input: s = "foobar", letter = "o"
Output: 33
Explanation: The percentage of characters in `s` that are equal to `letter` is 2/6 * 100 = 33.33%. Rounded down to the nearest whole number, this is 33%.

Example 2:
Input: s = "jjjj", letter = "k"
Output: 0
Explanation: The percentage of characters in `s` that are equal to `letter` is 0/4 * 100 = 0%.

Constraints:
- 1 <= s.length <= 100
- `s` consists of lowercase English letters.
- `letter` is a lowercase English letter.
"""

def percentageLetter(s: str, letter: str) -> int:
    """
    Calculate the percentage of characters in the string `s` that are equal to `letter`,
    rounded down to the nearest whole number.
    
    :param s: The input string consisting of lowercase English letters.
    :param letter: The target letter to calculate the percentage for.
    :return: The percentage of `letter` in `s`, rounded down to the nearest whole number.
    """
    count = s.count(letter)  # Count occurrences of `letter` in `s`
    total = len(s)  # Total number of characters in `s`
    return (count * 100) // total  # Calculate percentage and round down

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "foobar"
    letter1 = "o"
    print(percentageLetter(s1, letter1))  # Output: 33

    # Test Case 2
    s2 = "jjjj"
    letter2 = "k"
    print(percentageLetter(s2, letter2))  # Output: 0

    # Test Case 3
    s3 = "aabbcc"
    letter3 = "a"
    print(percentageLetter(s3, letter3))  # Output: 33

    # Test Case 4
    s4 = "abcde"
    letter4 = "e"
    print(percentageLetter(s4, letter4))  # Output: 20

    # Test Case 5
    s5 = "zzzzzzzzzz"
    letter5 = "z"
    print(percentageLetter(s5, letter5))  # Output: 100

"""
Time Complexity Analysis:
- Counting the occurrences of `letter` in `s` using `s.count(letter)` takes O(n) time, where `n` is the length of the string `s`.
- Calculating the percentage and returning the result takes O(1) time.
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The solution uses a constant amount of extra space, as no additional data structures are used.
- Overall, the space complexity is O(1).

Topic: Strings
"""