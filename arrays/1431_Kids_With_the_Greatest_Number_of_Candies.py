"""
LeetCode Problem #1431: Kids With the Greatest Number of Candies

Problem Statement:
Given the array `candies` and the integer `extraCandies`, where `candies[i]` represents the number of candies that the ith kid has.
For each kid, check if there is a way to distribute `extraCandies` among the kids such that the ith kid can have the greatest number of candies among them.
Notice that multiple kids can have the greatest number of candies.

Return a boolean list `result` of length `n`, where `result[i]` is `True` if, after giving the ith kid all the `extraCandies`, they can have the greatest number of candies among all the kids, or `False` otherwise.

Constraints:
- `2 <= candies.length <= 100`
- `1 <= candies[i] <= 100`
- `1 <= extraCandies <= 50`
"""

# Solution
def kidsWithCandies(candies, extraCandies):
    """
    Determines if each kid can have the greatest number of candies after receiving extraCandies.

    :param candies: List[int] - List of integers representing the number of candies each kid has.
    :param extraCandies: int - Number of extra candies to distribute.
    :return: List[bool] - Boolean list indicating if each kid can have the greatest number of candies.
    """
    max_candies = max(candies)  # Find the current maximum number of candies
    return [(candy + extraCandies) >= max_candies for candy in candies]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candies = [2, 3, 5, 1, 3]
    extraCandies = 3
    print(kidsWithCandies(candies, extraCandies))  # Output: [True, True, True, False, True]

    # Test Case 2
    candies = [4, 2, 1, 1, 2]
    extraCandies = 1
    print(kidsWithCandies(candies, extraCandies))  # Output: [True, False, False, False, False]

    # Test Case 3
    candies = [12, 1, 12]
    extraCandies = 10
    print(kidsWithCandies(candies, extraCandies))  # Output: [True, False, True]

# Time Complexity Analysis:
# - Finding the maximum value in the `candies` list takes O(n), where n is the length of the list.
# - The list comprehension iterates through the `candies` list once, which also takes O(n).
# - Overall time complexity: O(n).

# Space Complexity Analysis:
# - The space used is O(n) for the output list of booleans.
# - No additional space is used apart from the input and output.
# - Overall space complexity: O(n).

# Topic: Arrays