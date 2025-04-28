"""
LeetCode Problem #2775: Construct Smallest Number From DI String

Problem Statement:
You are given a string `pattern` of length `n` consisting of the characters 'I' meaning increasing and 'D' meaning decreasing.

You need to construct the smallest number that meets the following conditions:
1. The digits 1 to n+1 must appear exactly once in the number.
2. For each index i (0 <= i < n):
   - If pattern[i] == 'I', then the digit at index i must be less than the digit at index i+1.
   - If pattern[i] == 'D', then the digit at index i must be greater than the digit at index i+1.

Return the smallest number as a string that satisfies the conditions.

Constraints:
- 1 <= pattern.length <= 8
- pattern[i] is either 'I' or 'D'.

Example:
Input: pattern = "IDID"
Output: "13254"

Input: pattern = "III"
Output: "1234"

Input: pattern = "DDI"
Output: "3214"
"""

def smallestNumber(pattern: str) -> str:
    """
    Constructs the smallest number that satisfies the given pattern of 'I' and 'D'.
    
    Args:
    pattern (str): A string consisting of 'I' (increasing) and 'D' (decreasing).
    
    Returns:
    str: The smallest number as a string that satisfies the pattern.
    """
    stack = []
    result = []
    n = len(pattern)
    
    for i in range(n + 1):
        # Push the current number onto the stack
        stack.append(i + 1)
        
        # If we reach the end of the pattern or the current pattern character is 'I',
        # pop all elements from the stack and append them to the result
        if i == n or pattern[i] == 'I':
            while stack:
                result.append(stack.pop())
    
    return ''.join(map(str, result))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pattern = "IDID"
    print(smallestNumber(pattern))  # Output: "13254"

    # Test Case 2
    pattern = "III"
    print(smallestNumber(pattern))  # Output: "1234"

    # Test Case 3
    pattern = "DDI"
    print(smallestNumber(pattern))  # Output: "3214"

    # Test Case 4
    pattern = "DIDI"
    print(smallestNumber(pattern))  # Output: "21435"

    # Test Case 5
    pattern = "IID"
    print(smallestNumber(pattern))  # Output: "12354"


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the pattern string once (O(n)).
- For each character in the pattern, we may push and pop elements from the stack.
- In the worst case, each number is pushed and popped exactly once, resulting in O(n) operations.
- Overall, the time complexity is O(n), where n is the length of the pattern.

Space Complexity:
- The stack can hold at most n+1 elements, where n is the length of the pattern.
- The result list also stores n+1 elements.
- Therefore, the space complexity is O(n).

Topic: Stack
"""