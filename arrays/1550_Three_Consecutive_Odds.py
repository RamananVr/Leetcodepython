"""
LeetCode Problem #1550: Three Consecutive Odds

Problem Statement:
Given an integer array `arr`, return `true` if there are three consecutive odd numbers in the array. Otherwise, return `false`.

Example 1:
Input: arr = [2,6,4,1]
Output: false
Explanation: There are no three consecutive odds.

Example 2:
Input: arr = [1,2,34,3,4,5,7,23,12]
Output: true
Explanation: [5, 7, 23] are three consecutive odds.

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
"""

def three_consecutive_odds(arr):
    """
    Function to check if there are three consecutive odd numbers in the array.

    :param arr: List[int] - The input array of integers.
    :return: bool - True if there are three consecutive odd numbers, False otherwise.
    """
    count = 0
    for num in arr:
        if num % 2 == 1:  # Check if the number is odd
            count += 1
            if count == 3:  # If we find three consecutive odds, return True
                return True
        else:
            count = 0  # Reset the count if the number is even
    return False  # Return False if no three consecutive odds are found

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 6, 4, 1]
    print(three_consecutive_odds(arr1))  # Output: False

    # Test Case 2
    arr2 = [1, 2, 34, 3, 4, 5, 7, 23, 12]
    print(three_consecutive_odds(arr2))  # Output: True

    # Test Case 3
    arr3 = [1, 3, 5]
    print(three_consecutive_odds(arr3))  # Output: True

    # Test Case 4
    arr4 = [2, 4, 6, 8, 10]
    print(three_consecutive_odds(arr4))  # Output: False

    # Test Case 5
    arr5 = [1, 3, 5, 7, 9]
    print(three_consecutive_odds(arr5))  # Output: True

"""
Time Complexity:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a constant amount of extra space (a single integer variable `count`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""