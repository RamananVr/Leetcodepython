"""
LeetCode Problem #710: Random Pick with Blacklist

Problem Statement:
You are given an integer `n` and an array `blacklist`. Design an algorithm to pick a random integer in the range `[0, n - 1]` that is NOT in the `blacklist`. Any integer that is not in the blacklist should be equally likely to be returned.

Implement the `Solution` class:
- `Solution(int n, int[] blacklist)` Initializes the object with the integer `n` and the blacklist `blacklist`.
- `int pick()` Returns a random integer in the range `[0, n - 1]` and not in the blacklist.

Constraints:
- `1 <= n <= 10^9`
- `0 <= blacklist.length <= min(10^5, n - 1)`
- `0 <= blacklist[i] < n`
- All the values of `blacklist` are unique.
- At most `2 * 10^4` calls will be made to `pick`.

Example:
Input:
    ["Solution", "pick", "pick", "pick"]
    [[7, [2, 3, 5]], [], [], []]
Output:
    [null, 0, 4, 1]

Explanation:
    Solution solution = new Solution(7, [2, 3, 5]);
    solution.pick(); // Returns 0, as 0 is not in blacklist.
    solution.pick(); // Returns 4, as 4 is not in blacklist.
    solution.pick(); // Returns 1, as 1 is not in blacklist.
    All the returned values are equally likely to be returned.
"""

import random

class Solution:
    def __init__(self, n: int, blacklist: list[int]):
        # Calculate the size of the whitelist
        self.whitelist_size = n - len(blacklist)
        
        # Create a set of blacklisted numbers for quick lookup
        blacklist_set = set(blacklist)
        
        # Map blacklisted numbers in the range [0, whitelist_size - 1] to valid numbers
        self.mapping = {}
        last = n - 1
        for b in blacklist:
            if b < self.whitelist_size:
                # Find the next valid number to map to
                while last in blacklist_set:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self) -> int:
        # Generate a random number in the range [0, whitelist_size - 1]
        rand = random.randint(0, self.whitelist_size - 1)
        # Return the mapped value if it's blacklisted, otherwise return the number itself
        return self.mapping.get(rand, rand)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the solution with n = 7 and blacklist = [2, 3, 5]
    solution = Solution(7, [2, 3, 5])
    
    # Call pick() multiple times and print the results
    print(solution.pick())  # Expected: Random number from {0, 1, 4, 6}
    print(solution.pick())  # Expected: Random number from {0, 1, 4, 6}
    print(solution.pick())  # Expected: Random number from {0, 1, 4, 6}

"""
Time Complexity:
- Initialization (__init__): O(B), where B is the length of the blacklist. This is because we iterate over the blacklist to create the mapping.
- pick(): O(1), as generating a random number and checking the mapping is constant time.

Space Complexity:
- O(B), where B is the length of the blacklist. This is due to the mapping dictionary that stores at most B entries.

Topic: Hashing, Randomization
"""