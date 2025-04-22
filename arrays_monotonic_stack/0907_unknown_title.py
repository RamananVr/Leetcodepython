"""
LeetCode Problem #907: Sum of Subarray Minimums

Problem Statement:
Given an array of integers `arr`, find the sum of `min(b)` across all non-empty subarrays `b` of `arr`.
Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:
Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 3 + 1 + 2 + 4 + 1 + 1 + 2 + 1 + 1 + 1 = 17.

Example 2:
Input: arr = [11,81,94,43,3]
Output: 444

Constraints:
- 1 <= arr.length <= 3 * 10^4
- 1 <= arr[i] <= 3 * 10^4
"""

# Python Solution
def sumSubarrayMins(arr):
    MOD = 10**9 + 7
    n = len(arr)
    
    # Arrays to store the previous and next smaller elements
    prev_smaller = [-1] * n
    next_smaller = [n] * n
    
    # Monotonic stack for previous smaller elements
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        prev_smaller[i] = stack[-1] if stack else -1
        stack.append(i)
    
    # Monotonic stack for next smaller elements
    stack = []
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] > arr[i]:
            stack.pop()
        next_smaller[i] = stack[-1] if stack else n
        stack.append(i)
    
    # Calculate the sum of subarray minimums
    result = 0
    for i in range(n):
        left_count = i - prev_smaller[i]
        right_count = next_smaller[i] - i
        result += arr[i] * left_count * right_count
        result %= MOD
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [3, 1, 2, 4]
    print(sumSubarrayMins(arr1))  # Output: 17

    # Test Case 2
    arr2 = [11, 81, 94, 43, 3]
    print(sumSubarrayMins(arr2))  # Output: 444

    # Test Case 3
    arr3 = [1, 2, 3, 4, 5]
    print(sumSubarrayMins(arr3))  # Output: 35

    # Test Case 4
    arr4 = [5, 4, 3, 2, 1]
    print(sumSubarrayMins(arr4))  # Output: 35

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses two passes to calculate the previous and next smaller elements using monotonic stacks.
- Each pass takes O(n) time, where n is the length of the array.
- The final calculation of the result also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses two arrays `prev_smaller` and `next_smaller` of size n, and a stack that can hold up to n elements.
- The space complexity is O(n).

Topic: Arrays, Monotonic Stack
"""