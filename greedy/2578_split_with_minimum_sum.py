"""
LeetCode Question #2578: Split With Minimum Sum

Problem Statement:
Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
- The concatenation of num1 and num2 is equal to num (i.e., if num1 = 123 and num2 = 456, then num = 123456).
- The sum of num1 and num2 is minimized.

Return the minimum possible sum of num1 and num2.

Notes:
- num1 and num2 must not contain leading zeros.
- num1 and num2 can be empty strings, and their sum is still valid.

Constraints:
- 1 <= num <= 10^9
"""

def splitNum(num: int) -> int:
    """
    Function to split the number into two integers num1 and num2 such that their sum is minimized.
    """
    # Convert the number to a sorted list of digits
    digits = sorted(str(num))
    
    # Distribute digits alternately to num1 and num2
    num1, num2 = "", ""
    for i, digit in enumerate(digits):
        if i % 2 == 0:
            num1 += digit
        else:
            num2 += digit
    
    # Convert num1 and num2 to integers and return their sum
    return int(num1) + int(num2


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 4325
    print(splitNum(num))  # Expected Output: 59 (num1 = 24, num2 = 35)

    # Test Case 2
    num = 687
    print(splitNum(num))  # Expected Output: 75 (num1 = 68, num2 = 7)

    # Test Case 3
    num = 123456
    print(splitNum(num))  # Expected Output: 246 (num1 = 135, num2 = 246)

    # Test Case 4
    num = 10
    print(splitNum(num))  # Expected Output: 1 (num1 = 0, num2 = 1)

    # Test Case 5
    num = 987654321
    print(splitNum(num))  # Expected Output: 2469 (num1 = 13579, num2 = 2468)


"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the digits of the number takes O(n log n), where n is the number of digits in the input num.
- Distributing the digits alternately into num1 and num2 takes O(n).
- Overall time complexity: O(n log n), where n is the number of digits in num.

Space Complexity:
- The space required to store the sorted list of digits is O(n).
- The space required for num1 and num2 is also O(n).
- Overall space complexity: O(n), where n is the number of digits in num.

Topic: Greedy
"""