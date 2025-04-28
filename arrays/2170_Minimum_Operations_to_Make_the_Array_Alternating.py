"""
LeetCode Problem #2170: Minimum Operations to Make the Array Alternating

Problem Statement:
You are given a 0-indexed array `nums` consisting of `n` positive integers.

The array is called alternating if:
- `nums[i - 1] != nums[i]` for all `i` where `1 <= i < n`.

In one operation, you can choose an index `i` and change `nums[i]` to any positive integer.

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
    nums (List[int]): The input array of positive integers.

    Returns:
    int: The minimum number of operations required.
    """
    n = len(nums)
    if n == 1:
        return 0

    # Split the array into odd-indexed and even-indexed elements
    even_counts = Counter(nums[0::2])
    odd_counts = Counter(nums[1::2])

    # Get the most common elements and their counts for both even and odd indices
    even_most_common = even_counts.most_common(2) + [(None, 0)]  # Add dummy value to handle edge cases
    odd_most_common = odd_counts.most_common(2) + [(None, 0)]

    # Extract the top two most common elements and their counts
    even1, even1_count = even_most_common[0]
    even2, even2_count = even_most_common[1]
    odd1, odd1_count = odd_most_common[0]
    odd2, odd2_count = odd_most_common[1]

    # Case 1: Most common elements in even and odd indices are different
    if even1 != odd1:
        return n - (even1_count + odd1_count)

    # Case 2: Most common elements in even and odd indices are the same
    # We need to choose the second most common element for one of them
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

    # Test Case 5
    nums5 = [1, 2, 1, 2, 1, 2]
    print(minimumOperations(nums5))  # Output: 0


"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the array into even and odd indices takes O(n).
- Counting the frequencies of elements in even and odd indices takes O(n).
- Extracting the two most common elements for both even and odd indices takes O(1) (since the number of unique elements is bounded by 10^5).
- Overall, the time complexity is O(n).

Space Complexity:
- The space required for the Counter objects is proportional to the number of unique elements in the array, which is O(U), where U is the number of unique elements.
- In the worst case, U = O(n) (if all elements are unique), so the space complexity is O(n).

Primary Topic: Arrays
"""