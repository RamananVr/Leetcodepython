"""
LeetCode Problem #1432: Max Difference You Can Get From Changing an Integer

Problem Statement:
You are given an integer `num`. You will apply the following steps exactly two times:
1. Pick a digit `x` (0 <= x <= 9) and all the occurrences of `x` in the decimal representation of `num` are replaced with another digit `y` (0 <= y <= 9). The new integer cannot have leading zeros, unless the integer itself is 0. 
2. The result of the first change will be applied to the second change as well.

The maximum difference between the two integers you can get after applying the above operations is the answer.

Return the maximum difference you can get.

Constraints:
- 1 <= num <= 10^8
"""

def maxDiff(num: int) -> int:
    """
    Function to calculate the maximum difference you can get from changing an integer.
    """
    # Convert the number to a string for easier manipulation
    num_str = str(num)
    
    # Find the maximum number by replacing the first non-9 digit with 9
    for digit in num_str:
        if digit != '9':
            max_num = int(num_str.replace(digit, '9'))
            break
    else:
        max_num = num  # If all digits are 9, max_num remains the same
    
    # Find the minimum number
    if num_str[0] != '1':  # If the first digit is not 1, replace it with 1
        min_num = int(num_str.replace(num_str[0], '1'))
    else:
        # Replace the first non-1 digit with 0 (if it exists)
        for digit in num_str[1:]:
            if digit != '0' and digit != '1':
                min_num = int(num_str.replace(digit, '0'))
                break
        else:
            min_num = num  # If all digits are 0 or 1, min_num remains the same
    
    # Return the difference between the maximum and minimum numbers
    return max_num - min_num

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 555
    print(maxDiff(num))  # Expected Output: 888

    # Test Case 2
    num = 9
    print(maxDiff(num))  # Expected Output: 8

    # Test Case 3
    num = 123456
    print(maxDiff(num))  # Expected Output: 820000

    # Test Case 4
    num = 10000
    print(maxDiff(num))  # Expected Output: 80000

    # Test Case 5
    num = 9288
    print(maxDiff(num))  # Expected Output: 8700

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the digits of the number (converted to a string) a constant number of times.
- Replacing digits in a string is O(n), where n is the number of digits in the number.
- Overall, the time complexity is O(n), where n is the number of digits in the input number.

Space Complexity:
- The function uses a constant amount of extra space for variables and intermediate results.
- The space complexity is O(1).

Topic: Strings
"""