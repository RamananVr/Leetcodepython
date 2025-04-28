"""
LeetCode Question #1570: Dot Product of Two Sparse Vectors

Problem Statement:
A sparse vector is a vector that has a majority of its elements as zero. Implement a class `SparseVector` that represents a sparse vector and supports the following operations:

1. `SparseVector(nums: List[int])`: Initializes the object with the vector `nums`.
2. `dotProduct(vec: SparseVector) -> int`: Returns the dot product of the instance of `SparseVector` and another `SparseVector`.

The dot product of two vectors is defined as the sum of the element-wise multiplication of their corresponding elements. Formally, given two vectors `a` and `b`, their dot product is:
    dot_product = a[0] * b[0] + a[1] * b[1] + ... + a[n-1] * b[n-1]
where `n` is the length of the vectors.

A sparse vector can be represented efficiently by storing only the non-zero elements of the vector along with their indices.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `-100 <= nums[i] <= 100`

Example:
Input:
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])
Output:
    v1.dotProduct(v2) = 8
Explanation:
    The dot product is calculated as:
    (1 * 0) + (0 * 3) + (0 * 0) + (2 * 4) + (3 * 0) = 8
"""

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Initialize the sparse vector by storing only the non-zero elements and their indices.
        """
        self.non_zero_elements = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Compute the dot product of this sparse vector with another sparse vector.
        """
        result = 0
        # Iterate through the non-zero elements of the current vector
        for index, value in self.non_zero_elements.items():
            if index in vec.non_zero_elements:
                result += value * vec.non_zero_elements[index]
        return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    v1 = SparseVector([1, 0, 0, 2, 3])
    v2 = SparseVector([0, 3, 0, 4, 0])
    print(v1.dotProduct(v2))  # Output: 8

    # Test Case 2
    v3 = SparseVector([0, 1, 0, 0, 2, 0, 0])
    v4 = SparseVector([0, 0, 0, 0, 3, 0, 4])
    print(v3.dotProduct(v4))  # Output: 6

    # Test Case 3
    v5 = SparseVector([0, 0, 0])
    v6 = SparseVector([0, 0, 0])
    print(v5.dotProduct(v6))  # Output: 0

    # Test Case 4
    v7 = SparseVector([1, 2, 3])
    v8 = SparseVector([4, 5, 6])
    print(v7.dotProduct(v8))  # Output: 32


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Initializing the SparseVector: O(n), where n is the length of the input list `nums`. This is because we iterate through the list once to store the non-zero elements.
   - Computing the dot product: O(k), where k is the number of non-zero elements in the current vector. For each non-zero element, we check if the index exists in the other vector's non-zero elements, which is an O(1) operation due to dictionary lookups.
   - Overall: O(n) for initialization and O(k) for dot product computation.

2. Space Complexity:
   - The space required to store the non-zero elements is proportional to the number of non-zero elements in the vector. Let k1 and k2 be the number of non-zero elements in the two vectors. The space complexity is O(k1 + k2).

Topic: Hash Map, Arrays
"""