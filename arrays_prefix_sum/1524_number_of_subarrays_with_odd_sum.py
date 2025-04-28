"""
LeetCode Question #1524: Number of Subarrays With Odd Sum

Problem Statement:
Given an array of integers `arr`, return the number of subarrays with an odd sum.

Since the answer can be very large, return it modulo 10^9 + 7.

Example 1:
Input: arr = [1,3,5]
Output: 4
Explanation: All subarrays are [1], [1,3], [1,3,5], [3], [3,5], [5].
All subarrays with odd sums are [1], [1,3], [3], [5].

Example 2:
Input: arr = [2,4,6]
Output: 0
Explanation: All subarrays are [2], [2,4], [2,4,6], [4], [4,6], [6].
All subarrays have even sums, so the answer is 0.

Example 3:
Input: arr = [1,2,3,4,5,6,7]
Output: 16

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i] <= 100
"""

# Python Solution
def numOfSubarrays(arr):
    MOD = 10**9 + 7
    odd_count = 0
    even_count = 1  # Start with 1 to account for the empty prefix sum
    prefix_sum = 0
    result = 0

    for num in arr:
        prefix_sum += num
        if prefix_sum % 2 == 0:
            result += odd_count
            even_count += 1
        else:
            result += even_count
            odd_count += 1
        result %= MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 3, 5]
    print(numOfSubarrays(arr1))  # Output: 4

    # Test Case 2
    arr2 = [2, 4, 6]
    print(numOfSubarrays(arr2))  # Output: 0

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5, 6, 7]
    print(numOfSubarrays(arr3))  # Output: 16

    # Test Case 4
    arr4 = [1]
    print(numOfSubarrays(arr4))  # Output: 1

    # Test Case 5
    arr5 = [100, 99, 98, 97, 96]
    print(numOfSubarrays(arr5))  # Output: 9

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The solution uses a few integer variables (prefix_sum, odd_count, even_count, result) and does not use any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Arrays, Prefix Sum
"""