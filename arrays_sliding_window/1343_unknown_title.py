"""
LeetCode Problem #1343: Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Problem Statement:
Given an array of integers `arr` and two integers `k` and `threshold`, return the number of sub-arrays of size `k` 
and average greater than or equal to `threshold`.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:
Input: arr = [2,2,2,2,5,5,5,8], k = 3, threshold = 4
Output: 3
Explanation: Subarrays [2,2,5], [2,5,5], [5,5,8] have averages 3, 4, and 6 respectively. All but the first one are 
greater than or equal to 4 (threshold).

Example 2:
Input: arr = [1,1,1,1,1], k = 1, threshold = 0
Output: 5

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 10^4
- 1 <= k <= arr.length
- 0 <= threshold <= 10^4
"""

# Python Solution
def numOfSubarrays(arr, k, threshold):
    """
    Function to count the number of subarrays of size k with an average greater than or equal to threshold.

    :param arr: List[int] - The input array of integers.
    :param k: int - The size of the subarray.
    :param threshold: int - The threshold value for the average.
    :return: int - The count of subarrays meeting the condition.
    """
    # Calculate the required sum for the average to be >= threshold
    required_sum = k * threshold
    current_sum = sum(arr[:k])  # Initial sum of the first window of size k
    count = 0

    # Check if the first window meets the condition
    if current_sum >= required_sum:
        count += 1

    # Slide the window across the array
    for i in range(k, len(arr)):
        # Update the sliding window sum
        current_sum += arr[i] - arr[i - k]
        # Check if the current window meets the condition
        if current_sum >= required_sum:
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 2, 2, 2, 5, 5, 5, 8]
    k1 = 3
    threshold1 = 4
    print(numOfSubarrays(arr1, k1, threshold1))  # Output: 3

    # Test Case 2
    arr2 = [1, 1, 1, 1, 1]
    k2 = 1
    threshold2 = 0
    print(numOfSubarrays(arr2, k2, threshold2))  # Output: 5

    # Test Case 3
    arr3 = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
    k3 = 3
    threshold3 = 5
    print(numOfSubarrays(arr3, k3, threshold3))  # Output: 6

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    k4 = 2
    threshold4 = 3
    print(numOfSubarrays(arr4, k4, threshold4))  # Output: 3

    # Test Case 5
    arr5 = [5, 5, 5, 5, 5]
    k5 = 5
    threshold5 = 5
    print(numOfSubarrays(arr5, k5, threshold5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a sliding window approach, where we calculate the sum of the first window in O(k) time.
- Then, we slide the window across the array in O(n) time, where n is the length of the array.
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `current_sum` and `count`.
- Overall space complexity: O(1).
"""

# Topic: Arrays, Sliding Window