"""
LeetCode Problem #784: Letter Case Permutation

Problem Statement:
Given a string `s`, you can transform every letter individually to be lowercase or uppercase to create another string.
Return a list of all possible strings we could create. You can return the output in any order.

Constraints:
- `s` will consist only of letters and digits.
- `s` will have a length between 1 and 12.

Example:
Input: s = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: s = "3z4"
Output: ["3z4", "3Z4"]

Input: s = "12345"
Output: ["12345"]
"""

# Solution
def letterCasePermutation(s: str) -> list[str]:
    def backtrack(index, path):
        # If we've processed all characters, add the current path to the result
        if index == len(s):
            result.append("".join(path))
            return
        
        # If the current character is a digit, it can only be added as-is
        if s[index].isdigit():
            backtrack(index + 1, path + [s[index]])
        else:
            # Add the lowercase version of the character
            backtrack(index + 1, path + [s[index].lower()])
            # Add the uppercase version of the character
            backtrack(index + 1, path + [s[index].upper()])
    
    result = []
    backtrack(0, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "a1b2"
    print(f"Input: {s1}")
    print(f"Output: {letterCasePermutation(s1)}")
    # Expected Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

    # Test Case 2
    s2 = "3z4"
    print(f"Input: {s2}")
    print(f"Output: {letterCasePermutation(s2)}")
    # Expected Output: ["3z4", "3Z4"]

    # Test Case 3
    s3 = "12345"
    print(f"Input: {s3}")
    print(f"Output: {letterCasePermutation(s3)}")
    # Expected Output: ["12345"]

    # Test Case 4
    s4 = "C"
    print(f"Input: {s4}")
    print(f"Output: {letterCasePermutation(s4)}")
    # Expected Output: ["c", "C"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The number of permutations is 2^L, where L is the number of letters in the string `s`.
- For each permutation, we spend O(L) time to construct the string.
- Therefore, the overall time complexity is O(L * 2^L).

Space Complexity:
- The space complexity is O(L) for the recursion stack, where L is the length of the string `s`.
- Additionally, we store all permutations in the `result` list, which takes O(L * 2^L) space.
- Therefore, the overall space complexity is O(L * 2^L).
"""

# Topic: Backtracking