"""
LeetCode Question #1539: Kth Missing Positive Number

Problem Statement:
Given an array `arr` of positive integers sorted in a strictly increasing order, and an integer `k`.

Return the `k`th positive integer that is missing from this array.

Example 1:
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,...]. The 5th missing number is 9.

Example 2:
Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers are [5,6,7,...]. The 2nd missing number is 6.

Constraints:
- 1 <= arr.length <= 1000
- 1 <= arr[i] <= 1000
- 1 <= k <= 1000
- `arr` is sorted in strictly increasing order.

Follow up:
Can you solve it in less than O(n) time complexity?
"""

# Solution
def findKthPositive(arr, k):
    """
    Finds the kth missing positive integer from the sorted array `arr`.

    :param arr: List[int] - A sorted array of positive integers.
    :param k: int - The kth missing positive integer to find.
    :return: int - The kth missing positive integer.
    """
    missing_count = 0
    current = 1
    index = 0

    while True:
        if index < len(arr) and arr[index] == current:
            index += 1
        else:
            missing_count += 1
            if missing_count == k:
                return current
        current += 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 3, 4, 7, 11]
    k1 = 5
    print(findKthPositive(arr1, k1))  # Output: 9

    # Test Case 2
    arr2 = [1, 2, 3, 4]
    k2 = 2
    print(findKthPositive(arr2, k2))  # Output: 6

    # Test Case 3
    arr3 = [3, 10, 20]
    k3 = 5
    print(findKthPositive(arr3, k3))  # Output: 8

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    k4 = 1
    print(findKthPositive(arr4, k4))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- The solution iterates through the numbers starting from 1 until the kth missing number is found.
- In the worst case, we may iterate up to `k + len(arr)` numbers.
- Therefore, the time complexity is O(k + n), where n is the length of the array.

Space Complexity:
- The solution uses a constant amount of extra space.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays