"""
LeetCode Problem #1370: Increasing Decreasing String

Problem Statement:
Given a string `s`. You should re-order the string using the following algorithm:
1. Pick the smallest character from `s` and append it to the result.
2. Pick the smallest character from `s` which is greater than the last appended character to the result and append it.
3. Repeat step 2 until you cannot pick more characters.
4. Pick the largest character from `s` and append it to the result.
5. Pick the largest character from `s` which is smaller than the last appended character to the result and append it.
6. Repeat step 5 until you cannot pick more characters.
7. Repeat the steps from 1 to 6 until you pick all characters from `s`.

In each step, if the smallest or largest character to be picked is already used, skip it and continue to the next one.

Return the result string after sorting `s` with this algorithm.

Constraints:
- `1 <= s.length <= 500`
- `s` contains only lowercase English letters.
"""

# Solution
def sortString(s: str) -> str:
    # Count the frequency of each character
    char_count = [0] * 26
    for char in s:
        char_count[ord(char) - ord('a')] += 1

    result = []
    while len(result) < len(s):
        # Step 1: Pick smallest characters in increasing order
        for i in range(26):
            if char_count[i] > 0:
                result.append(chr(i + ord('a')))
                char_count[i] -= 1

        # Step 2: Pick largest characters in decreasing order
        for i in range(25, -1, -1):
            if char_count[i] > 0:
                result.append(chr(i + ord('a')))
                char_count[i] -= 1

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aaaabbbbcccc"
    print(sortString(s1))  # Expected Output: "abccbaabccba"

    # Test Case 2
    s2 = "rat"
    print(sortString(s2))  # Expected Output: "art"

    # Test Case 3
    s3 = "leetcode"
    print(sortString(s3))  # Expected Output: "cdelotee"

    # Test Case 4
    s4 = "ggggggg"
    print(sortString(s4))  # Expected Output: "ggggggg"

    # Test Case 5
    s5 = "spo"
    print(sortString(s5))  # Expected Output: "ops"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of characters takes O(n), where n is the length of the string `s`.
- Constructing the result string involves iterating over the character frequency array multiple times. 
  Each iteration processes all characters in `s`, so the total complexity is O(n).
- Overall time complexity: O(n).

Space Complexity:
- The `char_count` array uses O(26) space, which is constant.
- The `result` list uses O(n) space to store the final string.
- Overall space complexity: O(n).

Topic: Strings
"""