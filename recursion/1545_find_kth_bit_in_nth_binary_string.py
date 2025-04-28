"""
LeetCode Question #1545: Find Kth Bit in Nth Binary String

Problem Statement:
The binary string sequence is defined as follows:
- S1 = "0"
- Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1

Where + denotes string concatenation, reverse(x) returns the reversed string x, and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

Given two integers n and k, return the kth bit in Sn. It is guaranteed that k is valid for the given n.

Constraints:
- 1 <= n <= 20
- 1 <= k <= 2^n - 1
"""

# Solution
def findKthBit(n: int, k: int) -> str:
    def helper(n: int) -> str:
        if n == 1:
            return "0"
        prev = helper(n - 1)
        return prev + "1" + invert_and_reverse(prev)
    
    def invert_and_reverse(s: str) -> str:
        return ''.join('1' if char == '0' else '0' for char in reversed(s))
    
    return helper(n)[k - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 1
    print(findKthBit(n1, k1))  # Output: "0"

    # Test Case 2
    n2, k2 = 4, 11
    print(findKthBit(n2, k2))  # Output: "1"

    # Test Case 3
    n3, k3 = 2, 3
    print(findKthBit(n3, k3))  # Output: "1"

    # Test Case 4
    n4, k4 = 5, 16
    print(findKthBit(n4, k4))  # Output: "0"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The helper function generates the binary string Sn recursively. For each level, the size of the string doubles, and the invert_and_reverse operation takes O(length of string).
- The total time complexity is exponential, O(2^n), because the size of Sn is 2^n - 1.

Space Complexity:
- The recursive calls use O(n) space due to the call stack.
- Additionally, the generated strings require O(2^n) space.
- Overall space complexity is O(2^n).

Topic: Recursion
"""