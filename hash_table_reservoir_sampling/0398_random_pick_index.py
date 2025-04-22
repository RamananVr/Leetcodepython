"""
LeetCode Question #398: Random Pick Index

Problem Statement:
Given an integer array `nums` with possible duplicates, randomly output the index of a given target number. 
You can assume that the given target number exists in the array.

Implement the `Solution` class:
- `Solution(int[] nums)` Initializes the object with the array `nums`.
- `int pick(int target)` Picks a random index `i` from `nums` where `nums[i] == target`. 
  If there are multiple valid i's, each index should have an equal probability of being returned.

Example:
Input
["Solution", "pick", "pick", "pick"]
[[[1, 2, 3, 3, 3]], [3], [1], [3]]
Output
[null, 2, 0, 4]

Explanation
Solution solution = new Solution([1, 2, 3, 3, 3]);
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability.
solution.pick(1); // It should return 0 since only nums[0] == 1.
solution.pick(3); // It should return either index 2, 3, or 4 randomly. Each index should have equal probability.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -2^31 <= nums[i] <= 2^31 - 1
- target is an integer from `nums`.
- At most 10^4 calls will be made to `pick`.
"""

import random
from collections import defaultdict

class Solution:
    def __init__(self, nums: list[int]):
        """
        Initializes the object with the array nums.
        """
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        """
        Picks a random index i from nums where nums[i] == target.
        """
        return random.choice(self.indices[target])

# Example Test Cases
if __name__ == "__main__":
    # Initialize the solution with the array
    solution = Solution([1, 2, 3, 3, 3])
    
    # Test case 1: Picking index for target 3
    print(solution.pick(3))  # Expected: Randomly 2, 3, or 4
    
    # Test case 2: Picking index for target 1
    print(solution.pick(1))  # Expected: 0 (only one occurrence of 1)
    
    # Test case 3: Picking index for target 3 again
    print(solution.pick(3))  # Expected: Randomly 2, 3, or 4

"""
Time and Space Complexity Analysis:

1. Initialization (`__init__`):
   - Time Complexity: O(n), where n is the length of the input array `nums`. 
     We iterate through the array once to build the dictionary of indices.
   - Space Complexity: O(n), as we store all indices of each unique number in the dictionary.

2. Picking an index (`pick`):
   - Time Complexity: O(1), as we use `random.choice` to pick a random index from the precomputed list.
   - Space Complexity: O(1), as no additional space is used during the pick operation.

Overall:
- Time Complexity: O(n) for initialization, O(1) for each pick operation.
- Space Complexity: O(n).

Topic: Hash Table, Reservoir Sampling
"""