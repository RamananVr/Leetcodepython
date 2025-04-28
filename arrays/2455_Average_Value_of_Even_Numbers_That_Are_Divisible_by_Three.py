"""
LeetCode Problem #2455: Average Value of Even Numbers That Are Divisible by Three

Problem Statement:
Given an integer array `nums` of positive integers, return the average value of all even integers 
that are divisible by 3. If there are no such integers, return 0.

The average of `n` elements is the sum of the `n` elements divided by `n` and rounded down to the 
nearest integer (i.e., the floor of the average). The test cases are generated such that the 
answer will fit in a 32-bit integer.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def averageValue(nums):
    """
    Calculate the average value of all even integers in the array that are divisible by 3.
    
    :param nums: List[int] - List of positive integers
    :return: int - The floor of the average value of the qualifying integers, or 0 if none exist
    """
    # Filter the numbers that are both even and divisible by 3
    valid_numbers = [num for num in nums if num % 2 == 0 and num % 3 == 0]
    
    # If no valid numbers exist, return 0
    if not valid_numbers:
        return 0
    
    # Calculate the average and return the floor of the result
    return sum(valid_numbers) // len(valid_numbers)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case with valid numbers
    nums1 = [1, 3, 6, 10, 12, 15]
    print(averageValue(nums1))  # Output: 9 (6 and 12 are valid, average is (6+12)//2 = 9)

    # Test Case 2: No numbers divisible by 3
    nums2 = [1, 2, 4, 5, 7]
    print(averageValue(nums2))  # Output: 0 (no valid numbers)

    # Test Case 3: All numbers are valid
    nums3 = [6, 12, 18]
    print(averageValue(nums3))  # Output: 12 (average is (6+12+18)//3 = 12)

    # Test Case 4: Single valid number
    nums4 = [6]
    print(averageValue(nums4))  # Output: 6 (only one valid number)

    # Test Case 5: Large input with no valid numbers
    nums5 = [1] * 1000
    print(averageValue(nums5))  # Output: 0 (no valid numbers)

    # Test Case 6: Large input with all valid numbers
    nums6 = [6] * 1000
    print(averageValue(nums6))  # Output: 6 (all numbers are 6, average is 6)

"""
Time Complexity:
- Filtering the list takes O(n), where n is the length of the input array `nums`.
- Calculating the sum and length of the filtered list also takes O(n) in the worst case.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(k), where k is the number of valid numbers in the filtered list.
- In the worst case, if all numbers are valid, k = n, so the space complexity is O(n).

Topic: Arrays
"""