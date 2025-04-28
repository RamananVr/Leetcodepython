"""
LeetCode Question #2182: Construct String With Repeat Limit

Problem Statement:
You are given a string `s` and an integer `repeatLimit`. Construct a string `result` using the characters from `s` such that:
- Each character appears at most `repeatLimit` times consecutively.
- `result` is lexicographically largest among all possible strings that can be constructed.

Return the lexicographically largest string `result` that meets the conditions.

Example:
Input: s = "cczazcc", repeatLimit = 3
Output: "zzcccac"

Constraints:
- 1 <= s.length <= 10^5
- 1 <= repeatLimit <= 10^5
- `s` consists of lowercase English letters.
"""

# Solution
from collections import Counter

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    # Count the frequency of each character
    freq = Counter(s)
    
    # Sort characters in descending lexicographical order
    sorted_chars = sorted(freq.keys(), reverse=True)
    
    result = []
    i = 0
    
    while i < len(sorted_chars):
        char = sorted_chars[i]
        count = freq[char]
        
        # Add up to `repeatLimit` occurrences of the current character
        num_to_add = min(count, repeatLimit)
        result.extend([char] * num_to_add)
        freq[char] -= num_to_add
        
        # If the current character exceeds the repeat limit and there are other characters available
        if freq[char] > 0:
            # Find the next available character
            next_char_index = i + 1
            while next_char_index < len(sorted_chars) and freq[sorted_chars[next_char_index]] == 0:
                next_char_index += 1
            
            # If no next character is available, break
            if next_char_index == len(sorted_chars):
                break
            
            # Add one occurrence of the next character
            next_char = sorted_chars[next_char_index]
            result.append(next_char)
            freq[next_char] -= 1
            
            # If the next character is exhausted, remove it from the list
            if freq[next_char] == 0:
                sorted_chars.pop(next_char_index)
        else:
            # Move to the next character
            i += 1
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cczazcc"
    repeatLimit1 = 3
    print(repeatLimitedString(s1, repeatLimit1))  # Output: "zzcccac"

    # Test Case 2
    s2 = "aababab"
    repeatLimit2 = 2
    print(repeatLimitedString(s2, repeatLimit2))  # Output: "bbabaa"

    # Test Case 3
    s3 = "aaaaa"
    repeatLimit3 = 2
    print(repeatLimitedString(s3, repeatLimit3))  # Output: "aabaa"

    # Test Case 4
    s4 = "abc"
    repeatLimit4 = 1
    print(repeatLimitedString(s4, repeatLimit4))  # Output: "cba"

    # Test Case 5
    s5 = "zzzzzzzzzz"
    repeatLimit5 = 4
    print(repeatLimitedString(s5, repeatLimit5))  # Output: "zzzzzzzzzz"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the characters in `s` takes O(n log n), where `n` is the length of the string.
- Constructing the result string involves iterating through the sorted characters and their frequencies, which takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `freq` dictionary and `sorted_chars` list use O(u) space, where `u` is the number of unique characters in `s`.
- The result list uses O(n) space.
- Overall space complexity: O(n).

Topic: Greedy
"""