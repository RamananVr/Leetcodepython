"""
LeetCode Question #347: Top K Frequent Elements

Problem Statement:
Given an integer array `nums` and an integer `k`, return the `k` most frequent elements. 
You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
- k is in the range [1, the number of unique elements in the array].

Follow up:
Your algorithm's time complexity must be better than O(n log n), where n is the array's length.
"""

# Solution
from collections import Counter
import heapq

def topKFrequent(nums, k):
    """
    Returns the k most frequent elements from the input array nums.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The number of most frequent elements to return.

    Returns:
    List[int]: The k most frequent elements.
    """
    # Step 1: Count the frequency of each element
    freq_map = Counter(nums)
    
    # Step 2: Use a heap to find the k most frequent elements
    # The heap will store tuples of (-frequency, element) to create a max-heap behavior
    return [element for element, _ in heapq.nlargest(k, freq_map.items(), key=lambda x: x[1])]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    print(topKFrequent(nums1, k1))  # Output: [1, 2]

    # Test Case 2
    nums2 = [1]
    k2 = 1
    print(topKFrequent(nums2, k2))  # Output: [1]

    # Test Case 3
    nums3 = [4, 4, 4, 6, 6, 7, 7, 7, 7]
    k3 = 2
    print(topKFrequent(nums3, k3))  # Output: [7, 4]

    # Test Case 4
    nums4 = [5, 5, 5, 5, 6, 6, 6, 7]
    k4 = 3
    print(topKFrequent(nums4, k4))  # Output: [5, 6, 7]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting frequencies using `Counter(nums)` takes O(n), where n is the length of nums.
- Using `heapq.nlargest` to find the k most frequent elements takes O(k log u), where u is the number of unique elements in nums.
- Overall time complexity: O(n + k log u).

Space Complexity:
- The frequency map `freq_map` takes O(u) space, where u is the number of unique elements in nums.
- The heap used by `heapq.nlargest` takes O(u) space.
- Overall space complexity: O(u).

Note: In the worst case, u = n (all elements are unique), so the space complexity becomes O(n).
"""

# Topic: Hash Table, Heap, Sorting