"""
LeetCode Problem #761: Special Binary String

Problem Statement:
------------------
A special binary string is defined as a binary string with the following properties:
1. It is composed of only '0's and '1's.
2. It has the same number of '0's and '1's.
3. Every prefix of the binary string has at least as many '1's as '0's.

You are given a special binary string `s`. You can swap any two special binary strings within `s` to make the string as large as possible.

Return the lexicographically largest special binary string possible.

Constraints:
- `s` is a special binary string.
- `1 <= s.length <= 50`.

Example:
---------
Input: s = "11011000"
Output: "11100100"

Explanation:
- "11011000" can be transformed into "11100100" by swapping the substrings "10" and "1100".
"""

# Python Solution
def makeLargestSpecial(s: str) -> str:
    """
    Function to return the lexicographically largest special binary string.
    """
    count = 0
    start = 0
    substrings = []
    
    for i, char in enumerate(s):
        if char == '1':
            count += 1
        else:
            count -= 1
        
        # When count becomes zero, we have a valid special binary substring
        if count == 0:
            # Recursively process the inner substring
            substrings.append("1" + makeLargestSpecial(s[start + 1:i]) + "0")
            start = i + 1
    
    # Sort substrings in descending order and concatenate them
    substrings.sort(reverse=True)
    return "".join(substrings)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "11011000"
    print(makeLargestSpecial(s1))  # Output: "11100100"

    # Test Case 2
    s2 = "101100"
    print(makeLargestSpecial(s2))  # Output: "110010"

    # Test Case 3
    s3 = "111000"
    print(makeLargestSpecial(s3))  # Output: "111000"

    # Test Case 4
    s4 = "1101001100"
    print(makeLargestSpecial(s4))  # Output: "1110011000"

"""
Time and Space Complexity Analysis:
------------------------------------
Time Complexity:
- The function processes the string recursively, splitting it into substrings and sorting them.
- Sorting the substrings takes O(k log k), where k is the number of substrings.
- The recursion depth is proportional to the number of nested special binary substrings.
- In the worst case, the complexity is O(n log n), where n is the length of the string.

Space Complexity:
- The function uses additional space to store substrings during recursion.
- The space complexity is O(n) due to the recursive call stack and the storage of substrings.

Topic: String Manipulation, Recursion
"""