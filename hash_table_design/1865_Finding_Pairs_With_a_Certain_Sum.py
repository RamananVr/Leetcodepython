"""
LeetCode Problem #1865: Finding Pairs With a Certain Sum

Problem Statement:
You are given two integer arrays nums1 and nums2. You are tasked to implement a class `FindSumPairs` that supports the following operations:

1. `FindSumPairs(nums1: List[int], nums2: List[int])`: Initializes the object with two integer arrays nums1 and nums2.
2. `add(index: int, val: int) -> None`: Adds val to nums2[index], i.e., applies nums2[index] += val.
3. `count(tot: int) -> int`: Returns the number of pairs (i, j) such that nums1[i] + nums2[j] == tot.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 1 <= nums1[i], nums2[i] <= 10^5
- 0 <= index < nums2.length
- -10^5 <= val <= 10^5
- -10^9 <= tot <= 10^9
- At most 1000 calls are made to add and count.

"""

from collections import Counter
from typing import List

class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_counter = Counter(nums2)  # Precompute frequency of elements in nums2

    def add(self, index: int, val: int) -> None:
        # Update the frequency counter for nums2
        old_value = self.nums2[index]
        self.nums2_counter[old_value] -= 1
        if self.nums2_counter[old_value] == 0:
            del self.nums2_counter[old_value]
        
        self.nums2[index] += val
        new_value = self.nums2[index]
        self.nums2_counter[new_value] += 1

    def count(self, tot: int) -> int:
        # Count the number of valid pairs
        result = 0
        for num in self.nums1:
            complement = tot - num
            if complement in self.nums2_counter:
                result += self.nums2_counter[complement]
        return result


# Example Test Cases
if __name__ == "__main__":
    # Initialize the object
    nums1 = [1, 1, 2, 2]
    nums2 = [2, 3, 4, 5]
    find_sum_pairs = FindSumPairs(nums1, nums2)

    # Test count method
    print(find_sum_pairs.count(5))  # Output: 4 (pairs: (1,4), (1,4), (2,3), (2,3))

    # Test add method
    find_sum_pairs.add(3, 2)  # nums2 becomes [2, 3, 4, 7]
    print(find_sum_pairs.count(8))  # Output: 2 (pairs: (1,7), (1,7))

    find_sum_pairs.add(0, 1)  # nums2 becomes [3, 3, 4, 7]
    print(find_sum_pairs.count(6))  # Output: 4 (pairs: (1,3), (1,3), (2,4), (2,4))


"""
Time and Space Complexity Analysis:

1. Initialization (`__init__`):
   - Time Complexity: O(n2), where n2 is the length of nums2, to build the frequency counter.
   - Space Complexity: O(n2), for storing the frequency counter.

2. `add` method:
   - Time Complexity: O(1), as updating the frequency counter and nums2[index] is constant time.
   - Space Complexity: O(1), as no additional space is used.

3. `count` method:
   - Time Complexity: O(n1), where n1 is the length of nums1, as we iterate through nums1 and perform O(1) operations for each element.
   - Space Complexity: O(1), as no additional space is used.

Overall:
- Time Complexity: O(n2) for initialization, O(1) for `add`, and O(n1) for `count`.
- Space Complexity: O(n2).

Topic: Hash Table, Design
"""