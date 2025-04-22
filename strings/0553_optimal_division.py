"""
LeetCode Question #553: Optimal Division

Problem Statement:
You are given an integer array `nums`. The array consists of positive integers, and its length is at least 1.

Your task is to return a string that represents the optimal division of the numbers in the array such that the result of the division is maximized.

- If there is only one number in `nums`, return the string representation of that number.
- If there are two numbers in `nums`, return the string representation of the division of the first number by the second (e.g., "a/b").
- If there are more than two numbers, you can add parentheses to ensure the division is performed in the correct order to maximize the result.

Example:
Input: nums = [1000, 100, 10, 2]
Output: "1000/(100/10/2)"
Explanation: The optimal division is 1000 / (100 / 10 / 2) = 1000 / (100 / (10 / 2)) = 1000 / (100 / 5) = 1000 / 20 = 50.

Constraints:
- 1 <= nums.length <= 10
- 2 <= nums[i] <= 1000
- There is only one unique solution for the given input.
"""

# Python Solution
def optimalDivision(nums):
    """
    Returns the optimal division of the numbers in the array as a string.

    :param nums: List[int] - List of positive integers
    :return: str - Optimal division as a string
    """
    n = len(nums)
    
    # If there's only one number, return it as a string
    if n == 1:
        return str(nums[0])
    
    # If there are two numbers, return the division as "a/b"
    if n == 2:
        return f"{nums[0]}/{nums[1]}"
    
    # For more than two numbers, maximize the result by grouping all numbers except the first
    # inside parentheses
    return f"{nums[0]}/(" + "/".join(map(str, nums[1:])) + ")"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1000, 100, 10, 2]
    print(optimalDivision(nums1))  # Output: "1000/(100/10/2)"

    # Test Case 2
    nums2 = [2]
    print(optimalDivision(nums2))  # Output: "2"

    # Test Case 3
    nums3 = [2, 3]
    print(optimalDivision(nums3))  # Output: "2/3"

    # Test Case 4
    nums4 = [6, 2, 3, 4]
    print(optimalDivision(nums4))  # Output: "6/(2/3/4)"

    # Test Case 5
    nums5 = [10, 2, 5]
    print(optimalDivision(nums5))  # Output: "10/(2/5)"

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The function iterates through the `nums` array to construct the string representation.
   - The `"/".join(map(str, nums[1:]))` operation takes O(n) time, where n is the length of the `nums` array.
   - Overall, the time complexity is O(n).

2. Space Complexity:
   - The function uses additional space to store the string representation of the result.
   - The space required for the string is proportional to the size of the input array, so the space complexity is O(n).

Topic: Strings
"""