"""
LeetCode Problem #451: Sort Characters By Frequency

Problem Statement:
Given a string `s`, sort it in decreasing order based on the frequency of the characters. 
The frequency of a character is the number of times it appears in the string. 
Return the sorted string. If there are multiple answers, return any of them.

Example 1:
Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once. 
So 'e' must appear before 'r' and 't'. Therefore "eetr" is also a valid answer.

Example 2:
Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so "cccaaa" or "aaaccc" are both valid answers.

Example 3:
Input: s = "Aabb"
Output: "bbAa"
Explanation: "b" appears twice, "A" and "a" both appear once. 
Note that "A" and "a" are treated as two different characters.

Constraints:
- 1 <= s.length <= 5 * 10^5
- `s` consists of uppercase and lowercase English letters and digits.
"""

# Clean and Correct Python Solution
from collections import Counter

def frequencySort(s: str) -> str:
    # Count the frequency of each character
    freq = Counter(s)
    # Sort characters by frequency (descending) and then by character (optional for consistent output)
    sorted_chars = sorted(freq.keys(), key=lambda x: -freq[x])
    # Build the result string
    result = ''.join(char * freq[char] for char in sorted_chars)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "tree"
    print(frequencySort(s1))  # Output: "eert" or "eetr"

    # Test Case 2
    s2 = "cccaaa"
    print(frequencySort(s2))  # Output: "aaaccc" or "cccaaa"

    # Test Case 3
    s3 = "Aabb"
    print(frequencySort(s3))  # Output: "bbAa" or "bbaA"

    # Test Case 4
    s4 = "bbAa"
    print(frequencySort(s4))  # Output: "bbAa" or "bbaA"

    # Test Case 5
    s5 = "a"
    print(frequencySort(s5))  # Output: "a"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting the frequency of characters using `Counter` takes O(n), where n is the length of the string.
- Sorting the characters by frequency takes O(k log k), where k is the number of unique characters in the string.
  Since k <= n (in the worst case, all characters are unique), this step is bounded by O(n log n).
- Constructing the result string takes O(n), as we iterate through the string once to build the output.

Overall Time Complexity: O(n log n)

Space Complexity:
- The `Counter` object stores the frequency of each character, which takes O(k) space, where k is the number of unique characters.
- The sorted list of characters also takes O(k) space.
- The result string takes O(n) space.

Overall Space Complexity: O(n)

Topic: Strings
"""