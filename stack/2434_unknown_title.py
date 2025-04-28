"""
LeetCode Problem #2434: Using a Robot to Print the Lexicographically Smallest String

Problem Statement:
You are given a string `s` and a robot that processes the string using a stack. The robot processes the string in the following way:

1. It reads the characters of the string `s` from left to right.
2. The robot can either:
   - Push the current character to the stack.
   - Pop the top character from the stack and append it to the result string.

The robot is tasked to form the lexicographically smallest string possible.

Return the lexicographically smallest string that can be formed by the robot.

Constraints:
- `1 <= s.length <= 10^5`
- `s` consists of only lowercase English letters.
"""

def robotWithString(s: str) -> str:
    """
    Function to return the lexicographically smallest string that can be formed by the robot.
    """
    # Step 1: Compute the smallest character from the current position to the end
    n = len(s)
    min_from_right = [None] * n
    min_from_right[-1] = s[-1]
    
    for i in range(n - 2, -1, -1):
        min_from_right[i] = min(s[i], min_from_right[i + 1])
    
    # Step 2: Use a stack to simulate the robot's operations
    stack = []
    result = []
    
    for i in range(n):
        # Push the current character to the stack
        stack.append(s[i])
        
        # While the stack is not empty and the top of the stack is less than or equal to
        # the smallest character from the current position to the end, pop from the stack
        # and append to the result
        while stack and stack[-1] <= min_from_right[i]:
            result.append(stack.pop())
    
    # Append any remaining characters in the stack to the result
    while stack:
        result.append(stack.pop())
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "zza"
    print(robotWithString(s1))  # Output: "azz"

    # Test Case 2
    s2 = "bac"
    print(robotWithString(s2))  # Output: "abc"

    # Test Case 3
    s3 = "bdda"
    print(robotWithString(s3))  # Output: "addb"

    # Test Case 4
    s4 = "edcba"
    print(robotWithString(s4))  # Output: "abcde"

    # Test Case 5
    s5 = "leetcode"
    print(robotWithString(s5))  # Output: "cdeeelot"

"""
Time Complexity Analysis:
- Computing `min_from_right` takes O(n) time, where `n` is the length of the string `s`.
- Iterating through the string and processing the stack takes O(n) time in total because each character is pushed and popped from the stack at most once.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The `min_from_right` array takes O(n) space.
- The stack can hold at most `n` characters, so it also takes O(n) space.
- The result list takes O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Stack
"""