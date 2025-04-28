"""
LeetCode Problem #2980: Minimum Operations to Make Array Alternating

Problem Statement:
You are given a 0-indexed integer array `nums` consisting of `n` elements. You can perform the following operation on the array any number of times:

- Choose two indices `i` and `j` such that `i % 2 == j % 2` and `nums[i] != nums[j]`.
- Swap the values of `nums[i]` and `nums[j]`.

An array is called alternating if:
- Every element at an even index is equal, and
- Every element at an odd index is equal.

Return the minimum number of operations required to make the array alternating.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
"""

from collections import Counter

def minimumOperations(nums):
    """
    Function to calculate the minimum number of operations to make the array alternating.
    
    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum number of operations required.
    """
    if len(nums) == 1:
        return 0

    # Separate even-indexed and odd-indexed elements
    even_counts = Counter(nums[i] for i in range(0, len(nums), 2))
    odd_counts = Counter(nums[i] for i in range(1, len(nums), 2))

    # Get the most common elements and their counts for even and odd indices
    even_most_common = even_counts.most_common(2) + [(None, 0)]
    odd_most_common = odd_counts.most_common(2) + [(None, 0)]

    # Extract the top two most common elements and their counts
    even1, even1_count = even_most_common[0]
    even2, even2_count = even_most_common[1]
    odd1, odd1_count = odd_most_common[0]
    odd2, odd2_count = odd_most_common[1]

    n = len(nums)
    # Case 1: Most common even and odd elements are different
    if even1 != odd1:
        return n - even1_count - odd1_count
    # Case 2: Most common even and odd elements are the same
    else:
        return n - max(even1_count + odd2_count, even2_count + odd1_count)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 3, 2, 4, 3]
    print(minimumOperations(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 2, 2, 2]
    print(minimumOperations(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1]
    print(minimumOperations(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1, 1]
    print(minimumOperations(nums4))  # Output: 3

"""
Time Complexity Analysis:
- Separating even-indexed and odd-indexed elements takes O(n).
- Counting the frequencies of elements using Counter takes O(n).
- Extracting the most common elements and calculating the result is O(1).
Overall, the time complexity is O(n).

Space Complexity Analysis:
- The space used by the Counter objects is proportional to the number of unique elements in `nums`, which is O(u), where `u` is the number of unique elements.
- In the worst case, `u` can be O(n) if all elements are unique.
Overall, the space complexity is O(u), where `u` is the number of unique elements.

Topic: Arrays, Hash Table
"""