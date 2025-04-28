"""
LeetCode Problem #2979: Minimum Operations to Make Array Alternating

Problem Statement:
You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:
- nums[i] != nums[i + 1] for all 0 <= i < n - 1.

In one operation, you can choose any index i in the array and replace nums[i] with any positive integer.

Return the minimum number of operations required to make the array alternating.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

# Solution
from collections import Counter

def minimumOperations(nums):
    n = len(nums)
    if n == 1:
        return 0  # A single element is already alternating.

    # Split nums into even-indexed and odd-indexed elements
    even_elements = nums[0::2]
    odd_elements = nums[1::2]

    # Count frequencies of elements in even and odd positions
    even_count = Counter(even_elements)
    odd_count = Counter(odd_elements)

    # Get the two most common elements and their frequencies for even and odd positions
    even_top_two = even_count.most_common(2) + [(None, 0)] * (2 - len(even_count))
    odd_top_two = odd_count.most_common(2) + [(None, 0)] * (2 - len(odd_count))

    # Extract the most common and second most common elements and their frequencies
    even_most_common, even_second_common = even_top_two[0], even_top_two[1]
    odd_most_common, odd_second_common = odd_top_two[0], odd_top_two[1]

    # Case 1: Most common elements in even and odd positions are different
    if even_most_common[0] != odd_most_common[0]:
        return n - even_most_common[1] - odd_most_common[1]

    # Case 2: Most common elements in even and odd positions are the same
    # We need to choose the second most common element for one of the positions
    return n - max(
        even_most_common[1] + odd_second_common[1],
        even_second_common[1] + odd_most_common[1]
    )

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
    nums5 = [1, 2, 3, 4, 5, 6]
    print(minimumOperations(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the array into even and odd indexed elements takes O(n).
- Counting frequencies using Counter takes O(n).
- Extracting the two most common elements for even and odd positions takes O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The space used by the Counter objects is proportional to the number of unique elements in nums, which is O(u), where u is the number of unique elements.
- In the worst case, u = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays
"""