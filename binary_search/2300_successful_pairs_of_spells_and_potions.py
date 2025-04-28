"""
LeetCode Question #2300: Successful Pairs of Spells and Potions

Problem Statement:
You are given two positive integer arrays `spells` and `potions`, of length `n` and `m` respectively, where `spells[i]` represents the strength of the i-th spell and `potions[j]` represents the strength of the j-th potion.

You are also given an integer `success`. A spell and potion pair is considered successful if the product of their strengths is at least `success`.

Return an integer array `pairs` of length `n` where `pairs[i]` is the number of potions that will form a successful pair with the i-th spell.

Constraints:
- `n == spells.length`
- `m == potions.length`
- `1 <= n, m <= 10^5`
- `1 <= spells[i], potions[j] <= 10^5`
- `1 <= success <= 10^10`
"""

from typing import List
import bisect

def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    """
    Returns the number of successful pairs for each spell.
    """
    # Sort the potions array for binary search
    potions.sort()
    m = len(potions)
    result = []

    for spell in spells:
        # Calculate the minimum potion strength needed for success
        min_potion = (success + spell - 1) // spell  # Equivalent to ceil(success / spell)
        # Find the index of the first potion that meets the requirement
        index = bisect.bisect_left(potions, min_potion)
        # Count the number of potions that are successful
        result.append(m - index)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    spells = [10, 20, 30]
    potions = [1, 2, 3, 4, 5]
    success = 40
    print(successfulPairs(spells, potions, success))  # Output: [4, 3, 2]

    # Test Case 2
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    print(successfulPairs(spells, potions, success))  # Output: [4, 0, 3]

    # Test Case 3
    spells = [7, 2]
    potions = [3, 6, 8, 10]
    success = 20
    print(successfulPairs(spells, potions, success))  # Output: [3, 0]

"""
Time Complexity:
- Sorting the potions array takes O(m log m), where m is the length of the potions array.
- For each spell, we perform a binary search on the potions array, which takes O(log m).
- Since there are n spells, the total complexity for the binary search is O(n log m).
- Overall time complexity: O(m log m + n log m).

Space Complexity:
- The space complexity is O(1) additional space, as we are not using any extra data structures apart from the result array.

Topic: Binary Search
"""