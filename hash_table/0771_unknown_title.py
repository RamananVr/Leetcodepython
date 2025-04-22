"""
LeetCode Problem #771: Jewels and Stones

Problem Statement:
You're given strings `jewels` representing the types of stones that are jewels, and `stones` representing the stones you have. 
Each character in `stones` is a type of stone you have. You want to know how many of the stones you have are also jewels.

Letters are case-sensitive, so "a" is different from "A".

Example 1:
Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

Example 2:
Input: jewels = "z", stones = "ZZ"
Output: 0

Constraints:
- `jewels` and `stones` consist of only English letters.
- All characters in `jewels` are unique.
- `1 <= jewels.length, stones.length <= 50`
"""

# Solution
def numJewelsInStones(jewels: str, stones: str) -> int:
    """
    This function counts how many stones are jewels.

    :param jewels: A string representing the types of jewels.
    :param stones: A string representing the stones you have.
    :return: The number of stones that are jewels.
    """
    jewel_set = set(jewels)  # Convert jewels to a set for O(1) lookup
    return sum(stone in jewel_set for stone in stones)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    jewels = "aA"
    stones = "aAAbbbb"
    print(numJewelsInStones(jewels, stones))  # Output: 3

    # Test Case 2
    jewels = "z"
    stones = "ZZ"
    print(numJewelsInStones(jewels, stones))  # Output: 0

    # Test Case 3
    jewels = "abc"
    stones = "aabbcc"
    print(numJewelsInStones(jewels, stones))  # Output: 6

    # Test Case 4
    jewels = "xyz"
    stones = "xyxyxy"
    print(numJewelsInStones(jewels, stones))  # Output: 6

    # Test Case 5
    jewels = "A"
    stones = "aA"
    print(numJewelsInStones(jewels, stones))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting `jewels` to a set takes O(J), where J is the length of the `jewels` string.
- Iterating through `stones` and checking membership in the set takes O(S), where S is the length of the `stones` string.
- Overall time complexity: O(J + S).

Space Complexity:
- The set `jewel_set` requires O(J) space, where J is the length of the `jewels` string.
- Overall space complexity: O(J).
"""

# Topic: Hash Table