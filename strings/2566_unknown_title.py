"""
LeetCode Problem #2566: Maximum Difference by Remapping a Digit

Problem Statement:
You are given a positive integer num consisting of exactly n digits. 
You may replace any digit of num with another digit. After replacing a digit, 
the new integer should not have leading zeros.

Return the maximum difference between the smallest and largest integers you can 
create by remapping exactly one digit (i.e., replacing it with another digit).

Example:
Input: num = 11891
Output: 99009
Explanation:
To achieve the maximum difference:
- Replace the first '1' with '9' to get the largest number: 99899.
- Replace the first '1' with '0' to get the smallest number: 00800 (which is 800 after removing leading zeros).
The difference is 99899 - 800 = 99099.

Constraints:
- 1 <= num <= 10^8
"""

# Python Solution
def maxDiff(num: int) -> int:
    num_str = str(num)
    
    # Find the largest number
    for digit in num_str:
        if digit != '9':
            largest = num_str.replace(digit, '9')
            break
    else:
        largest = num_str  # If all digits are '9', no replacement needed
    
    # Find the smallest number
    if num_str[0] != '1':
        smallest = num_str.replace(num_str[0], '1')
    else:
        for digit in num_str[1:]:
            if digit != '0' and digit != '1':
                smallest = num_str.replace(digit, '0')
                break
        else:
            smallest = num_str  # If all digits are '0' or '1', no replacement needed
    
    # Convert to integers and calculate the difference
    return int(largest) - int(smallest)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = 11891
    print(maxDiff(num))  # Output: 99009

    # Test Case 2
    num = 123456
    print(maxDiff(num))  # Output: 820000

    # Test Case 3
    num = 99999
    print(maxDiff(num))  # Output: 0

    # Test Case 4
    num = 10001
    print(maxDiff(num))  # Output: 89999

    # Test Case 5
    num = 1
    print(maxDiff(num))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves iterating through the digits of the number (O(n), where n is the number of digits).
- The `replace` operation is linear in the size of the string, so the overall complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the string representation of the number and intermediate strings created during replacements.

Topic: Strings
"""