"""
LeetCode Problem #528: Random Pick with Weight

Problem Statement:
You are given a list of positive integers `w` where `w[i]` describes the weight of index `i` (0-indexed).
We need to implement a solution that allows us to randomly pick an index in proportion to its weight.

Specifically, the probability of picking index `i` is `w[i] / sum(w)`.

Implement the `Solution` class:
- `Solution(int[] w)` Initializes the object with the given integer array `w`.
- `int pickIndex()` Returns a random index chosen with the probability proportional to its weight.

Constraints:
- 1 <= w.length <= 10^4
- 1 <= w[i] <= 10^5
- pickIndex will be called at most 10^4 times.

Example:
Input:
["Solution", "pickIndex", "pickIndex", "pickIndex", "pickIndex", "pickIndex"]
[[[1, 3]], [], [], [], [], []]
Output:
[null, 1, 1, 1, 0, 1]

Explanation:
Solution solution = new Solution([1, 3]);
solution.pickIndex(); // returns 1, probability of picking index 1 is 3/4.
solution.pickIndex(); // returns 1
solution.pickIndex(); // returns 1
solution.pickIndex(); // returns 0, probability of picking index 0 is 1/4.
solution.pickIndex(); // returns 1
"""

import random
from itertools import accumulate

class Solution:
    def __init__(self, w: list[int]):
        """
        Initializes the Solution object with the given weights.
        Precomputes the prefix sums for efficient random index picking.
        """
        self.prefix_sums = list(accumulate(w))
        self.total_sum = self.prefix_sums[-1]

    def pickIndex(self) -> int:
        """
        Picks an index randomly with probability proportional to its weight.
        Uses binary search to find the appropriate index.
        """
        target = random.randint(1, self.total_sum)
        # Binary search to find the smallest index such that prefix_sums[index] >= target
        low, high = 0, len(self.prefix_sums) - 1
        while low < high:
            mid = (low + high) // 2
            if self.prefix_sums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    solution = Solution([1, 3])
    results = [solution.pickIndex() for _ in range(10)]
    print("Test Case 1 Results:", results)  # Expected: More 1s than 0s (probability 3/4 for index 1, 1/4 for index 0)

    # Test Case 2
    solution = Solution([10, 20, 30])
    results = [solution.pickIndex() for _ in range(10)]
    print("Test Case 2 Results:", results)  # Expected: More 2s than 1s, and more 1s than 0s

    # Test Case 3
    solution = Solution([5, 5, 5, 5])
    results = [solution.pickIndex() for _ in range(10)]
    print("Test Case 3 Results:", results)  # Expected: Uniform distribution among indices 0, 1, 2, 3

"""
Time Complexity:
- Initialization (__init__): O(n), where n is the length of the weights array `w`. This is due to the computation of the prefix sums.
- pickIndex(): O(log n), where n is the length of the weights array `w`. This is due to the binary search on the prefix sums.

Space Complexity:
- O(n), where n is the length of the weights array `w`. This is for storing the prefix sums.

Topic: Arrays, Binary Search, Prefix Sum, Randomization
"""