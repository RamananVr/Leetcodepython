"""
LeetCode Problem #1881: Maximum Value after Insertion

Problem Statement:
You are given a string `n` representing a positive or negative integer, and a digit `x`.

- You want to maximize the numerical value of `n` by inserting `x` anywhere in the integer (including at the beginning or end).
- The inserted digit can only appear once in the resulting number.

Return a string representing the maximum value of `n` after the insertion.

Example 1:
Input: n = "99", x = 9
Output: "999"

Example 2:
Input: n = "-13", x = 2
Output: "-123"

Constraints:
- `1 <= n.length <= 10^5`
- `n` consists of digits and may have a leading '-'.
- `1 <= x <= 9`
"""

def maxValue(n: str, x: int) -> str:
    """
    Function to maximize the numerical value of n by inserting x.
    
    Args:
    n (str): The input number as a string (can be positive or negative).
    x (int): The digit to insert.

    Returns:
    str: The resulting number as a string after inserting x.
    """
    x = str(x)
    if n[0] == '-':  # Negative number case
        for i in range(1, len(n)):
            if x < n[i]:  # Insert x where it minimizes the negative value
                return n[:i] + x + n[i:]
        return n + x  # If no smaller digit is found, append x at the end
    else:  # Positive number case
        for i in range(len(n)):
            if x > n[i]:  # Insert x where it maximizes the positive value
                return n[:i] + x + n[i:]
        return n + x  # If no larger digit is found, append x at the end

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Positive number
    n1, x1 = "99", 9
    print(maxValue(n1, x1))  # Expected Output: "999"

    # Test Case 2: Negative number
    n2, x2 = "-13", 2
    print(maxValue(n2, x2))  # Expected Output: "-123"

    # Test Case 3: Positive number with insertion in the middle
    n3, x3 = "123", 5
    print(maxValue(n3, x3))  # Expected Output: "1523"

    # Test Case 4: Negative number with insertion at the end
    n4, x4 = "-456", 7
    print(maxValue(n4, x4))  # Expected Output: "-4567"

    # Test Case 5: Large positive number
    n5, x5 = "987654321", 6
    print(maxValue(n5, x5))  # Expected Output: "9876543216"

    # Test Case 6: Large negative number
    n6, x6 = "-987654321", 6
    print(maxValue(n6, x6))  # Expected Output: "-6987654321"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `n` once to find the optimal position to insert `x`.
- Therefore, the time complexity is O(n), where `n` is the length of the string `n`.

Space Complexity:
- The function uses O(1) additional space, as it performs operations directly on the input string and constructs the result using slicing.
- The space complexity is O(1).

Topic: Strings
"""