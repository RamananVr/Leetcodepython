"""
LeetCode Question #202: Happy Number

Problem Statement:
A happy number is a number defined by the following process:
- Starting with any positive integer, replace the number by the sum of the squares of its digits.
- Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
- Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example 1:
Input: n = 19
Output: True
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

Example 2:
Input: n = 2
Output: False
"""

def isHappy(n: int) -> bool:
    def get_next(number: int) -> int:
        """Helper function to calculate the sum of the squares of the digits of a number."""
        return sum(int(digit) ** 2 for digit in str(number))
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    return n == 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Happy number
    n1 = 19
    print(f"Input: {n1}, Output: {isHappy(n1)}")  # Expected: True

    # Test Case 2: Not a happy number
    n2 = 2
    print(f"Input: {n2}, Output: {isHappy(n2)}")  # Expected: False

    # Test Case 3: Edge case (smallest happy number)
    n3 = 1
    print(f"Input: {n3}, Output: {isHappy(n3)}")  # Expected: True

    # Test Case 4: Larger happy number
    n4 = 7
    print(f"Input: {n4}, Output: {isHappy(n4)}")  # Expected: True

    # Test Case 5: Larger non-happy number
    n5 = 20
    print(f"Input: {n5}, Output: {isHappy(n5)}")  # Expected: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of iterations in the while loop is proportional to the number of unique numbers encountered before either reaching 1 or entering a cycle.
- The sum of the squares of the digits operation takes O(log(n)) time, where log(n) is the number of digits in n.
- In practice, the numbers quickly reduce to smaller values, and the cycle detection ensures the process terminates efficiently.
- Therefore, the time complexity is approximately O(k * log(n)), where k is the number of unique numbers encountered.

Space Complexity:
- We use a set to store the numbers encountered during the process, which can grow up to k unique numbers.
- The space complexity is O(k), where k is the number of unique numbers encountered.

Topic: Hashing, Math
"""