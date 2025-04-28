"""
LeetCode Problem #769: Max Chunks To Make Sorted

Problem Statement:
You are given an integer array `arr` of length `n` that represents a permutation of the numbers in the range `[0, n - 1]`.

We split `arr` into some number of "chunks" (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the maximum number of chunks we can make to sort the array.

Example 1:
Input: arr = [4, 3, 2, 1, 0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the sorted array. For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn't sorted.

Example 2:
Input: arr = [1, 0, 2, 3, 4]
Output: 4
Explanation:
We can split into chunks like this: [1, 0], [2], [3], [4].

Constraints:
- `n == arr.length`
- `1 <= n <= 10^4`
- `0 <= arr[i] < n`
- All the elements of `arr` are unique.
"""

def maxChunksToSorted(arr):
    """
    Function to calculate the maximum number of chunks to make the array sorted.
    
    :param arr: List[int] - Input array representing a permutation of numbers [0, n-1]
    :return: int - Maximum number of chunks
    """
    max_so_far = 0
    chunks = 0
    
    for i, num in enumerate(arr):
        max_so_far = max(max_so_far, num)
        if max_so_far == i:
            chunks += 1
    
    return chunks

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 3, 2, 1, 0]
    print(maxChunksToSorted(arr1))  # Output: 1

    # Test Case 2
    arr2 = [1, 0, 2, 3, 4]
    print(maxChunksToSorted(arr2))  # Output: 4

    # Test Case 3
    arr3 = [0, 1, 2, 3, 4]
    print(maxChunksToSorted(arr3))  # Output: 5

    # Test Case 4
    arr4 = [2, 0, 1, 3, 4]
    print(maxChunksToSorted(arr4))  # Output: 2

"""
Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables `max_so_far` and `chunks`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""