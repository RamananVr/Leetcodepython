"""
LeetCode Problem #2168: Unique Substrings With Equal Digit Frequency

Problem Statement:
You are given a string `s` consisting of digits from '0' to '9'. A substring of `s` is called unique if all the digits in the substring have the same frequency. Your task is to find the number of unique substrings in `s`.

A substring is a contiguous sequence of characters within a string. For example, the substrings of "123" are "1", "2", "3", "12", "23", and "123".

Constraints:
- 1 <= s.length <= 100
- s consists of digits from '0' to '9'.

Write a function `equalDigitFrequency(s: str) -> int` that returns the number of unique substrings of `s` where all digits have the same frequency.
"""

from collections import Counter

def equalDigitFrequency(s: str) -> int:
    """
    Function to find the number of unique substrings where all digits have the same frequency.
    """
    unique_substrings = set()
    
    # Iterate over all possible substrings
    for i in range(len(s)):
        freq = Counter()
        for j in range(i, len(s)):
            freq[s[j]] += 1
            # Check if all frequencies are the same
            if len(set(freq.values())) == 1:
                # Add the substring to the set
                unique_substrings.add(s[i:j+1])
    
    return len(unique_substrings)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "1212"
    print(equalDigitFrequency(s1))  # Expected Output: 5

    # Test Case 2
    s2 = "123"
    print(equalDigitFrequency(s2))  # Expected Output: 6

    # Test Case 3
    s3 = "111"
    print(equalDigitFrequency(s3))  # Expected Output: 3

    # Test Case 4
    s4 = "112233"
    print(equalDigitFrequency(s4))  # Expected Output: 15

    # Test Case 5
    s5 = "1"
    print(equalDigitFrequency(s5))  # Expected Output: 1

"""
Time Complexity Analysis:
- The outer loop runs `O(n)` times, where `n` is the length of the string.
- The inner loop runs `O(n)` times in the worst case for each iteration of the outer loop.
- Inside the inner loop, updating the frequency counter and checking the condition takes `O(1)` for each character.
- Therefore, the overall time complexity is `O(n^2)`.

Space Complexity Analysis:
- The space complexity is `O(n)` for the frequency counter and the set of unique substrings.

Topic: Strings, Hashing
"""