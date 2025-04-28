"""
LeetCode Problem #2800: Shortest String That Contains Three Strings

Problem Statement:
You are given three strings: `a`, `b`, and `c`. Your task is to find the shortest string that contains all three strings as substrings. 
If there are multiple answers, return any of them.

Constraints:
- 1 <= len(a), len(b), len(c) <= 100
- `a`, `b`, and `c` consist of lowercase English letters.

The problem requires finding the shortest string that contains all three input strings as substrings. 
The solution should be efficient and handle edge cases properly.
"""

from itertools import permutations

def shortest_string_with_three_strings(a: str, b: str, c: str) -> str:
    """
    Finds the shortest string that contains all three input strings as substrings.
    
    Args:
    a (str): First input string.
    b (str): Second input string.
    c (str): Third input string.
    
    Returns:
    str: The shortest string containing all three strings as substrings.
    """
    def merge_strings(s1: str, s2: str) -> str:
        """
        Merges two strings into the shortest string that contains both as substrings.
        """
        if s2 in s1:
            return s1
        for i in range(len(s1)):
            if s1[i:] == s2[:len(s1) - i]:
                return s1 + s2[len(s1) - i:]
        return s1 + s2

    # Generate all permutations of the three strings
    permutations_of_strings = permutations([a, b, c])
    shortest = None

    for perm in permutations_of_strings:
        merged = merge_strings(merge_strings(perm[0], perm[1]), perm[2])
        if shortest is None or len(merged) < len(shortest):
            shortest = merged

    return shortest


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b, c = "abc", "bca", "cab"
    print(shortest_string_with_three_strings(a, b, c))  # Output: "abcab"

    # Test Case 2
    a, b, c = "ab", "bc", "cd"
    print(shortest_string_with_three_strings(a, b, c))  # Output: "abcd"

    # Test Case 3
    a, b, c = "a", "b", "c"
    print(shortest_string_with_three_strings(a, b, c))  # Output: "abc"

    # Test Case 4
    a, b, c = "abc", "def", "ghi"
    print(shortest_string_with_three_strings(a, b, c))  # Output: "abcdefghi"

    # Test Case 5
    a, b, c = "abc", "cde", "eab"
    print(shortest_string_with_three_strings(a, b, c))  # Output: "abcdeab"


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The function generates all permutations of the three strings, which is 3! = 6 permutations.
   - For each permutation, it merges strings twice using the `merge_strings` function.
   - The `merge_strings` function has a complexity of O(n + m), where n and m are the lengths of the two strings being merged.
   - Therefore, the overall time complexity is O(6 * (n + m + p)), where n, m, and p are the lengths of the three strings.

2. Space Complexity:
   - The space complexity is dominated by the storage of the permutations (constant size for three strings) and the merged strings.
   - The space complexity is O(n + m + p), where n, m, and p are the lengths of the three strings.

Topic: Strings
"""