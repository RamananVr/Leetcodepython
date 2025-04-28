"""
LeetCode Problem #1186: Maximum Subarray Sum with One Deletion

Problem Statement:
Given an array of integers `arr`, return the maximum sum of the subarray in the array, 
possibly by deleting at most one element. A subarray is a contiguous subsequence of the array.

Example 1:
Input: arr = [1, -2, 0, 3]
Output: 4
Explanation: Because we can choose the subarray [1, -2, 0, 3] or [1, 0, 3] after deleting -2.

Example 2:
Input: arr = [1, -2, -2, 3]
Output: 3
Explanation: We can choose the subarray [3] or [1, 3] after deleting one of the -2's.

Example 3:
Input: arr = [-1, -1, -1, -1]
Output: -1
Explanation: The result is -1 since no subarray can have a sum larger than -1.

Constraints:
- 1 <= arr.length <= 10^5
- -10^4 <= arr[i] <= 10^4
"""

def maximumSum(arr):
    """
    Function to calculate the maximum subarray sum with at most one deletion.
    
    :param arr: List[int] - Input array of integers
    :return: int - Maximum subarray sum with at most one deletion
    """
    n = len(arr)
    if n == 1:
        return arr[0]
    
    # Initialize arrays to store the maximum subarray sum ending at each index
    # without deletion and with one deletion
    max_ending_here = [0] * n
    max_with_deletion = [0] * n
    
    # Base case: the first element
    max_ending_here[0] = arr[0]
    max_with_deletion[0] = arr[0]
    
    # Initialize the result with the first element
    result = arr[0]
    
    for i in range(1, n):
        # Maximum subarray sum ending at index i without deletion
        max_ending_here[i] = max(arr[i], max_ending_here[i - 1] + arr[i])
        
        # Maximum subarray sum ending at index i with one deletion
        max_with_deletion[i] = max(max_ending_here[i - 1], max_with_deletion[i - 1] + arr[i])
        
        # Update the result
        result = max(result, max_ending_here[i], max_with_deletion[i])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, -2, 0, 3]
    print("Test Case 1 Output:", maximumSum(arr1))  # Expected Output: 4

    # Test Case 2
    arr2 = [1, -2, -2, 3]
    print("Test Case 2 Output:", maximumSum(arr2))  # Expected Output: 3

    # Test Case 3
    arr3 = [-1, -1, -1, -1]
    print("Test Case 3 Output:", maximumSum(arr3))  # Expected Output: -1

    # Test Case 4
    arr4 = [1, 2, 3, -4, 5]
    print("Test Case 4 Output:", maximumSum(arr4))  # Expected Output: 11

    # Test Case 5
    arr5 = [10, -10, 10, -10, 10]
    print("Test Case 5 Output:", maximumSum(arr5))  # Expected Output: 20

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations at each step.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses two auxiliary arrays of size n to store intermediate results.
- Therefore, the space complexity is O(n).

Topic: Dynamic Programming (DP)
"""