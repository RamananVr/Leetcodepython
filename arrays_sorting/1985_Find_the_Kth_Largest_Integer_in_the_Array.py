"""
LeetCode Problem #1985: Find the Kth Largest Integer in the Array

Problem Statement:
You are given an array of strings `nums` and an integer `k`. Each string in `nums` represents an integer without leading zeros.

Return the string that represents the kth largest integer in `nums`.

Note:
- The strings in `nums` may be very large, so you need to treat them as integers for comparison.
- `k` is guaranteed to be valid, meaning 1 ≤ k ≤ nums.length.

Constraints:
- 1 ≤ nums.length ≤ 10^4
- 1 ≤ nums[i].length ≤ 100
- nums[i] consists of only digits.
- nums[i] does not have leading zeros.
- All the integers in `nums` are unique.
"""

# Solution
from typing import List

def kthLargestNumber(nums: List[str], k: int) -> str:
    # Sort the numbers based on their integer value
    nums.sort(key=lambda x: int(x), reverse=True)
    # Return the k-th largest number
    return nums[k - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = ["3", "6", "7", "10"]
    k1 = 4
    print(kthLargestNumber(nums1, k1))  # Output: "3"

    # Test Case 2
    nums2 = ["2", "21", "12", "1"]
    k2 = 3
    print(kthLargestNumber(nums2, k2))  # Output: "2"

    # Test Case 3
    nums3 = ["0", "0", "0"]
    k3 = 1
    print(kthLargestNumber(nums3, k3))  # Output: "0"

    # Test Case 4
    nums4 = ["123", "456", "789", "1000"]
    k4 = 2
    print(kthLargestNumber(nums4, k4))  # Output: "456"

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Sorting the array takes O(n log n), where n is the length of the `nums` array.
   - Converting each string to an integer during sorting takes O(m), where m is the average length of the strings.
   - Overall time complexity: O(n * m + n log n), which simplifies to O(n log n) for large n.

2. Space Complexity:
   - The sorting operation may require O(n) additional space for the sorting algorithm.
   - No additional data structures are used, so the space complexity is O(n).

Topic: Arrays, Sorting
"""