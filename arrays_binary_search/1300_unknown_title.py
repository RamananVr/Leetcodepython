"""
LeetCode Problem #1300: Sum of Mutated Array Closest to Target

Problem Statement:
Given an integer array `arr` and a target value `target`, return the integer `value` such that when we replace all the integers greater than `value` in the array with `value`, the sum of the array comes closest to `target`.

In case of a tie, return the smaller value.

Example:
Input: arr = [4,9,3], target = 10
Output: 3
Explanation: When using 3, the mutated array is [3,3,3] which sums to 9, closest to 10.

Constraints:
- 1 <= arr.length <= 10^4
- 1 <= arr[i], target <= 10^5
"""

# Solution
def findBestValue(arr, target):
    """
    Finds the integer value such that replacing all integers greater than value
    in the array with value results in a sum closest to the target.

    :param arr: List[int] - The input array
    :param target: int - The target sum
    :return: int - The integer value that minimizes the difference
    """
    arr.sort()
    n = len(arr)
    prefix_sum = 0

    for i in range(n):
        # Calculate the potential value
        remaining_elements = n - i
        value = (target - prefix_sum) // remaining_elements

        if value <= arr[i]:
            # If the value is less than or equal to the current element, return the best value
            diff1 = abs(prefix_sum + value * remaining_elements - target)
            diff2 = abs(prefix_sum + (value - 1) * remaining_elements - target)
            return value if diff1 <= diff2 else value - 1

        prefix_sum += arr[i]

    # If we never return in the loop, return the largest element
    return arr[-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 9, 3]
    target1 = 10
    print(findBestValue(arr1, target1))  # Output: 3

    # Test Case 2
    arr2 = [2, 3, 5]
    target2 = 10
    print(findBestValue(arr2, target2))  # Output: 5

    # Test Case 3
    arr3 = [60864, 25176, 27249, 21296, 20204]
    target3 = 56803
    print(findBestValue(arr3, target3))  # Output: 11361

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The loop iterates through the array once, performing constant-time calculations for each element. This is O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it operates directly on the input array and uses a few variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays, Binary Search