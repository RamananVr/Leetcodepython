"""
LeetCode Problem #2677: Chunk Array

Problem Statement:
Given an array `arr` and an integer `size`, implement a function `chunk` that splits the array into many subarrays where each subarray is of length `size`. The last subarray may be smaller if there are not enough elements to complete it.

Example:
Input: arr = [1, 2, 3, 4, 5], size = 2
Output: [[1, 2], [3, 4], [5]]

Constraints:
- `arr` is a valid list of integers.
- `size` is a positive integer.
"""

def chunk(arr, size):
    """
    Splits the input array into chunks of the given size.

    :param arr: List[int] - The input array to be chunked.
    :param size: int - The size of each chunk.
    :return: List[List[int]] - A list of subarrays (chunks).
    """
    # Use list slicing to create chunks of the given size
    return [arr[i:i + size] for i in range(0, len(arr), size)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    size1 = 2
    print(chunk(arr1, size1))  # Expected Output: [[1, 2], [3, 4], [5]]

    # Test Case 2
    arr2 = [1, 2, 3, 4, 5, 6, 7]
    size2 = 3
    print(chunk(arr2, size2))  # Expected Output: [[1, 2, 3], [4, 5, 6], [7]]

    # Test Case 3
    arr3 = [1]
    size3 = 1
    print(chunk(arr3, size3))  # Expected Output: [[1]]

    # Test Case 4
    arr4 = []
    size4 = 3
    print(chunk(arr4, size4))  # Expected Output: []

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    size5 = 10
    print(chunk(arr5, size5))  # Expected Output: [[1, 2, 3, 4, 5]]

"""
Time Complexity:
- The slicing operation `arr[i:i + size]` runs in O(k) time, where `k` is the size of the slice.
- The loop iterates approximately `len(arr) / size` times.
- Therefore, the overall time complexity is O(n), where `n` is the length of the input array.

Space Complexity:
- The space complexity is O(n) because we are creating a new list to store the chunks.

Topic: Arrays
"""