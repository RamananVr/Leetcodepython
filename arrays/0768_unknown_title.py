"""
LeetCode Problem #768: Max Chunks To Make Sorted II

Problem Statement:
You are given an integer array `arr`.

We split `arr` into some number of "chunks" (partitions), and individually sort each chunk. 
After concatenating them, the result should equal the sorted array.

Return the maximum number of chunks we can make to sort the array.

Example 1:
Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the sorted array. For example, splitting into [5, 4] and [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn't sorted.

Example 2:
Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into [2, 1], [3], [4], [4].

Note:
- `arr` will have length in the range [1, 2000].
- `arr[i]` will be an integer in the range [0, 10^8].
"""

def maxChunksToSorted(arr):
    """
    Function to calculate the maximum number of chunks to make the array sorted.
    
    Args:
    arr (List[int]): The input array.

    Returns:
    int: The maximum number of chunks.
    """
    n = len(arr)
    max_left = [0] * n
    min_right = [0] * n

    # Fill max_left array
    max_left[0] = arr[0]
    for i in range(1, n):
        max_left[i] = max(max_left[i - 1], arr[i])

    # Fill min_right array
    min_right[n - 1] = arr[n - 1]
    for i in range(n - 2, -1, -1):
        min_right[i] = min(min_right[i + 1], arr[i])

    # Count chunks
    chunks = 0
    for i in range(n - 1):
        if max_left[i] <= min_right[i + 1]:
            chunks += 1

    # Add the last chunk
    return chunks + 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [5, 4, 3, 2, 1]
    print(maxChunksToSorted(arr1))  # Output: 1

    # Test Case 2
    arr2 = [2, 1, 3, 4, 4]
    print(maxChunksToSorted(arr2))  # Output: 4

    # Test Case 3
    arr3 = [1, 0, 2, 3, 4]
    print(maxChunksToSorted(arr3))  # Output: 4

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    print(maxChunksToSorted(arr4))  # Output: 5

    # Test Case 5
    arr5 = [2, 1, 2, 1, 2]
    print(maxChunksToSorted(arr5))  # Output: 2


"""
Time Complexity Analysis:
- Filling the `max_left` array takes O(n) time.
- Filling the `min_right` array takes O(n) time.
- Iterating through the array to count chunks takes O(n) time.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `max_left` and `min_right` arrays each take O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""