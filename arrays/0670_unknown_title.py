"""
LeetCode Problem #670: Maximum Swap

Problem Statement:
You are given a non-negative integer `num`. You can swap at most two digits of `num`. 
Return the maximum valued number you can get.

Example 1:
Input: num = 2736
Output: 7236
Explanation: Swap the 2 and the 7.

Example 2:
Input: num = 9973
Output: 9973
Explanation: No swap needed since the number is already the largest possible.

Constraints:
- 0 <= num <= 10^8
"""

def maximumSwap(num: int) -> int:
    """
    Function to find the maximum number that can be obtained by swapping at most two digits of the input number.
    """
    # Convert the number to a list of characters for easy manipulation
    num_list = list(str(num))
    # Create a dictionary to store the last occurrence of each digit
    last = {int(d): i for i, d in enumerate(num_list)}
    
    # Iterate through the digits of the number
    for i, digit in enumerate(num_list):
        # Check for a larger digit to swap with, starting from 9 down to the current digit
        for d in range(9, int(digit), -1):
            # If a larger digit exists and appears later in the number
            if last.get(d, -1) > i:
                # Swap the digits
                num_list[i], num_list[last[d]] = num_list[last[d]], num_list[i]
                # Convert the list back to an integer and return the result
                return int(''.join(num_list))
    
    # If no swap is performed, return the original number
    return num

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 2736
    print(f"Input: {num1}, Output: {maximumSwap(num1)}")  # Expected Output: 7236

    # Test Case 2
    num2 = 9973
    print(f"Input: {num2}, Output: {maximumSwap(num2)}")  # Expected Output: 9973

    # Test Case 3
    num3 = 1234
    print(f"Input: {num3}, Output: {maximumSwap(num3)}")  # Expected Output: 4231

    # Test Case 4
    num4 = 98368
    print(f"Input: {num4}, Output: {maximumSwap(num4)}")  # Expected Output: 98863

    # Test Case 5
    num5 = 0
    print(f"Input: {num5}, Output: {maximumSwap(num5)}")  # Expected Output: 0

"""
Time Complexity:
- The time complexity is O(n), where n is the number of digits in the input number.
  - We iterate through the digits once to build the `last` dictionary (O(n)).
  - We iterate through the digits again to find the first valid swap (O(n)).
  - Overall, this results in O(n) time complexity.

Space Complexity:
- The space complexity is O(n), where n is the number of digits in the input number.
  - This is due to the storage of the `num_list` and the `last` dictionary.

Topic: Arrays
"""