"""
LeetCode Problem #384: Shuffle an Array

Problem Statement:
Given an integer array `nums`, design an algorithm to randomly shuffle the array. All permutations of the array should be equally likely as a result of the shuffling.

Implement the `Solution` class:
1. `Solution(int[] nums)` Initializes the object with the integer array `nums`.
2. `int[] reset()` Resets the array to its original configuration and returns it.
3. `int[] shuffle()` Returns a random shuffling of the array.

Constraints:
- 1 <= nums.length <= 50
- -10^6 <= nums[i] <= 10^6
- All the elements of `nums` are unique.

Example:
Input:
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
Output:
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

Explanation:
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // Shuffle the array and return its result. Any permutation of [1, 2, 3] must be equally likely to be returned. Example: return [3, 1, 2]
solution.reset();      // Resets the array back to its original configuration [1, 2, 3]. Return [1, 2, 3]
solution.shuffle();    // Returns the random shuffling of the array. Example: return [1, 3, 2]
"""

import random

class Solution:
    def __init__(self, nums: list[int]):
        """
        Initializes the object with the integer array nums.
        """
        self.original = nums[:]  # Store a copy of the original array
        self.current = nums[:]   # Create a mutable copy for shuffling

    def reset(self) -> list[int]:
        """
        Resets the array to its original configuration and returns it.
        """
        self.current = self.original[:]  # Reset to the original array
        return self.current

    def shuffle(self) -> list[int]:
        """
        Returns a random shuffling of the array.
        """
        shuffled = self.current[:]
        n = len(shuffled)
        for i in range(n):
            # Pick a random index from i to n-1
            swap_idx = random.randint(i, n - 1)
            # Swap the elements at i and swap_idx
            shuffled[i], shuffled[swap_idx] = shuffled[swap_idx], shuffled[i]
        return shuffled


# Example Test Cases
if __name__ == "__main__":
    # Initialize the Solution object with the array [1, 2, 3]
    solution = Solution([1, 2, 3])

    # Test shuffle method
    print("Shuffled Array:", solution.shuffle())  # Output: Random permutation of [1, 2, 3]

    # Test reset method
    print("Reset Array:", solution.reset())  # Output: [1, 2, 3]

    # Test shuffle method again
    print("Shuffled Array:", solution.shuffle())  # Output: Random permutation of [1, 2, 3]


"""
Time and Space Complexity Analysis:

1. `__init__`:
   - Time Complexity: O(n), where n is the length of the input array `nums`, as we make a copy of the array.
   - Space Complexity: O(n), for storing the original and current arrays.

2. `reset`:
   - Time Complexity: O(n), as we copy the original array to reset the current array.
   - Space Complexity: O(n), for the returned array.

3. `shuffle`:
   - Time Complexity: O(n), as we iterate through the array once and perform constant-time operations (swapping) for each element.
   - Space Complexity: O(n), for the shuffled array.

Overall:
- Time Complexity: O(n) for each method.
- Space Complexity: O(n) for storing the arrays.

Topic: Arrays
"""