"""
LeetCode Problem #1087: Brace Expansion

Problem Statement:
You are given a string `s` representing a list of words. Each letter in the string is either a single lowercase letter, 
or a pair of curly braces containing lowercase letters. For example, "a{b,c}" represents the list ["ab", "ac"], 
and "{a,b}c{d,e}f" represents the list ["acdf", "acef", "bcdf", "bcef"].

Return all words that can be formed in this manner, sorted in lexicographical order.

Constraints:
- 1 <= s.length <= 50
- `s` consists of curly braces `{}`, commas `,`, and lowercase English letters.
- `s` is guaranteed to be a valid input.
- There are no nested curly braces.

Example:
Input: s = "{a,b}c{d,e}f"
Output: ["acdf", "acef", "bcdf", "bcef"]

Input: s = "abcd"
Output: ["abcd"]
"""

from typing import List

def expand(s: str) -> List[str]:
    """
    Function to generate all possible words from the given string `s` and return them in lexicographical order.
    """
    def backtrack(index: int, path: List[str]):
        # If we've processed the entire string, add the current path to the result
        if index == len(parts):
            result.append("".join(path))
            return
        
        # Iterate over all options for the current part
        for char in parts[index]:
            path.append(char)  # Choose
            backtrack(index + 1, path)  # Explore
            path.pop()  # Un-choose

    # Parse the input string into parts
    parts = []
    i = 0
    while i < len(s):
        if s[i] == '{':
            j = i
            while s[j] != '}':
                j += 1
            # Extract the options inside the braces and sort them
            parts.append(sorted(s[i+1:j].split(',')))
            i = j + 1
        else:
            # Single character, add as a single option
            parts.append([s[i]])
            i += 1

    # Initialize result list and start backtracking
    result = []
    backtrack(0, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "{a,b}c{d,e}f"
    print(expand(s1))  # Output: ["acdf", "acef", "bcdf", "bcef"]

    # Test Case 2
    s2 = "abcd"
    print(expand(s2))  # Output: ["abcd"]

    # Test Case 3
    s3 = "{z,x,y}a{b,c}"
    print(expand(s3))  # Output: ["xab", "xac", "yab", "yac", "zab", "zac"]

    # Test Case 4
    s4 = "a{b,c,d}e"
    print(expand(s4))  # Output: ["abe", "ace", "ade"]

    # Test Case 5
    s5 = "{a,b,c}"
    print(expand(s5))  # Output: ["a", "b", "c"]

"""
Time Complexity:
- Parsing the string into parts takes O(n), where n is the length of the string `s`.
- Backtracking generates all possible combinations. If there are `k` parts and each part has an average of `m` options,
  the total number of combinations is O(m^k). Generating each combination takes O(k) time (to join the string).
  Thus, the total time complexity is O(k * m^k).

Space Complexity:
- The space used for storing the `parts` list is O(k * m), where `k` is the number of parts and `m` is the average number of options per part.
- The recursion stack can go as deep as `k`, so the space complexity for the stack is O(k).
- The result list stores all combinations, which is O(m^k).
- Overall space complexity: O(k * m + m^k).

Topic: Backtracking
"""