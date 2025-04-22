"""
LeetCode Question #816: Ambiguous Coordinates

Problem Statement:
We are given a string `s` that represents a pair of coordinates in the form "(x, y)", 
where `x` and `y` are integers that can have leading zeros. The string `s` does not 
contain any spaces, and it is guaranteed to have the format "(a,b)" where `a` and `b` 
are non-empty strings.

You need to return all possible valid coordinates that can be formed by inserting 
a single decimal point (or none) into each of the two numbers `a` and `b`. A valid 
coordinate must not have leading zeros unless it is "0", and it must not have trailing 
zeros after the decimal point.

Return the coordinates in any order.

Example:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)", "(12, 3.0)", "(1.2, 3.0)"]

Constraints:
- 4 <= s.length <= 12
- `s` consists of digits and the characters '(' and ')'.

"""

def ambiguousCoordinates(s: str):
    def valid_parts(s):
        """Generate all valid representations of a number with optional decimal point"""
        n = len(s)
        if n == 0 or (n > 1 and s[0] == '0' and s[-1] == '0'):  # invalid leading/trailing zero
            return []
        if n > 1 and s[0] == '0':  # leading zero but not trailing
            return [f"0.{s[1:]}"]
        if s[-1] == '0':  # trailing zero but not leading
            return [s]
        return [s]+[f"{s[:i]}.{s[i:]}" for i in range(1, n)]

    s = s[1:-1]  # remove the parentheses
    n = len(s)
    result = []
    for i in range(1, n):  # split into two parts
        left, right = s[:i], s[i:]
        left_parts = valid_parts(left)
        right_parts = valid_parts(right)
        for l in left_parts:
            for r in right_parts:
                result.append(f"({l}, {r})")
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "(123)"
    print(ambiguousCoordinates(s1))  # Expected: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

    # Test Case 2
    s2 = "(00011)"
    print(ambiguousCoordinates(s2))  # Expected: ["(0.001, 1)", "(0, 0.011)"]

    # Test Case 3
    s3 = "(0123)"
    print(ambiguousCoordinates(s3))  # Expected: ["(0, 123)", "(0.1, 23)", "(0.12, 3)"]

    # Test Case 4
    s4 = "(100)"
    print(ambiguousCoordinates(s4))  # Expected: ["(10, 0)"]

"""
Time Complexity Analysis:
- Let `n` be the length of the string `s` (excluding the parentheses).
- The function `valid_parts` generates all valid representations of a number, which takes O(n) time for each part.
- Splitting the string into two parts and generating all combinations of valid parts takes O(n^2) in total.
- Therefore, the overall time complexity is O(n^3) because we iterate over all possible splits and generate combinations.

Space Complexity Analysis:
- The space complexity is O(n^2) due to the storage of intermediate results in the `result` list.

Topic: Strings, Backtracking
"""