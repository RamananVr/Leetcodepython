"""
LeetCode Question #1717: Maximum Score From Removing Substrings

Problem Statement:
You are given a string `s` and two integers `x` and `y`. You can perform two types of operations any number of times:
1. Remove the substring "ab" and gain `x` points.
2. Remove the substring "ba" and gain `y` points.

Note that removing a substring may lead to new substrings forming. For example, after removing "ab" from "cabba", it becomes "cba", and you can then remove "ba".

Return the maximum score you can gain after removing substrings from `s`.

Constraints:
- `1 <= s.length <= 10^5`
- `1 <= x, y <= 10^4`
- `s` consists of lowercase English letters.
"""

# Solution
def maximumGain(s: str, x: int, y: int) -> int:
    # Helper function to calculate score for a specific substring
    def calculate_score(s: str, first: str, second: str, points: int) -> int:
        stack = []
        score = 0
        for char in s:
            if stack and stack[-1] == first and char == second:
                stack.pop()
                score += points
            else:
                stack.append(char)
        return score, ''.join(stack)

    # Determine the order of operations based on the points
    if x > y:
        score_ab, remaining = calculate_score(s, 'a', 'b', x)
        score_ba, _ = calculate_score(remaining, 'b', 'a', y)
    else:
        score_ba, remaining = calculate_score(s, 'b', 'a', y)
        score_ab, _ = calculate_score(remaining, 'a', 'b', x)

    return score_ab + score_ba

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cdbab"
    x1, y1 = 4, 5
    print(maximumGain(s1, x1, y1))  # Expected Output: 9

    # Test Case 2
    s2 = "aabbaaxybbaabb"
    x2, y2 = 5, 4
    print(maximumGain(s2, x2, y2))  # Expected Output: 20

    # Test Case 3
    s3 = "ababa"
    x3, y3 = 3, 2
    print(maximumGain(s3, x3, y3))  # Expected Output: 7

    # Test Case 4
    s4 = "aaaa"
    x4, y4 = 10, 10
    print(maximumGain(s4, x4, y4))  # Expected Output: 0

    # Test Case 5
    s5 = "abababab"
    x5, y5 = 6, 7
    print(maximumGain(s5, x5, y5))  # Expected Output: 28

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `calculate_score` function iterates through the string `s` once, performing stack operations in O(1) time.
   - Since we call `calculate_score` twice, the overall time complexity is O(n), where `n` is the length of the string `s`.

2. Space Complexity:
   - The stack used in `calculate_score` can grow up to the size of the string `s` in the worst case, resulting in O(n) space complexity.
   - The remaining string after the first operation also takes O(n) space.
   - Overall space complexity is O(n).

Topic: String Manipulation
"""