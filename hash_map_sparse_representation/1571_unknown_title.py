"""
LeetCode Problem #1571: Dot Product of Two Sparse Vectors

Problem Statement:
Given two sparse vectors, compute their dot product.

Implement class `SparseVector`:
- `SparseVector(nums: List[int])` Initializes the object with the vector `nums`.
- `dotProduct(vec: SparseVector) -> int` Returns the dot product of the two sparse vectors.

A sparse vector is a vector that has a majority of its elements as zero. Implement the `SparseVector` class such that it optimizes for space and time complexity.

The dot product of two vectors is defined as:
    dot_product = sum(A[i] * B[i] for all i)
where `A` and `B` are the two vectors.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `-100 <= nums[i] <= 100`
"""

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        """
        Initialize the sparse vector by storing only non-zero elements and their indices.
        """
        self.non_zero_elements = {i: num for i, num in enumerate(nums) if num != 0}

    def dotProduct(self, vec: 'SparseVector') -> int:
        """
        Compute the dot product of this vector with another sparse vector.
        """
        result = 0
        # Iterate through the non-zero elements of this vector
        for index, value in self.non_zero_elements.items():
            if index in vec.non_zero_elements:
                result += value * vec.non_zero_elements[index]
        return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))  # Output: 8 (2*4)

    # Test Case 2
    nums1 = [0, 1, 0, 0, 0]
    nums2 = [0, 0, 0, 0, 2]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))  # Output: 0 (no overlapping non-zero indices)

    # Test Case 3
    nums1 = [0, 1, 0, 2, 3]
    nums2 = [0, 1, 0, 2, 3]
    v1 = SparseVector(nums1)
    v2 = SparseVector(nums2)
    print(v1.dotProduct(v2))  # Output: 14 (1*1 + 2*2 + 3*3)


"""
Time and Space Complexity Analysis:

1. Initialization (`__init__`):
   - Time Complexity: O(n), where `n` is the length of the input vector. We iterate through the vector once to store non-zero elements.
   - Space Complexity: O(k), where `k` is the number of non-zero elements in the vector. We store only the non-zero elements and their indices.

2. Dot Product (`dotProduct`):
   - Time Complexity: O(min(k1, k2)), where `k1` and `k2` are the number of non-zero elements in the two vectors. We iterate through the smaller set of non-zero elements.
   - Space Complexity: O(1), as we only use a constant amount of extra space.

Overall:
- Time Complexity: O(n) for initialization and O(min(k1, k2)) for dot product computation.
- Space Complexity: O(k), where `k` is the number of non-zero elements in the vector.

Topic: Hash Map, Sparse Representation
"""