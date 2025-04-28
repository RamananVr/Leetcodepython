"""
LeetCode Question #1951: All Unique Candies

Problem Statement:
You are given an array `candies` where each element represents a type of candy. 
Your task is to determine the number of unique types of candies in the array.

Write a function `countUniqueCandies(candies: List[int]) -> int` that returns the count of unique candy types.

Constraints:
- 1 <= len(candies) <= 10^5
- -10^9 <= candies[i] <= 10^9
"""

from typing import List

def countUniqueCandies(candies: List[int]) -> int:
    """
    Function to count the number of unique candy types in the given list.

    Args:
    candies (List[int]): List of integers representing candy types.

    Returns:
    int: Number of unique candy types.
    """
    # Use a set to store unique candy types
    return len(set(candies))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: All candies are unique
    candies1 = [1, 2, 3, 4, 5]
    print(countUniqueCandies(candies1))  # Expected Output: 5

    # Test Case 2: Some candies are repeated
    candies2 = [1, 1, 2, 2, 3, 3]
    print(countUniqueCandies(candies2))  # Expected Output: 3

    # Test Case 3: All candies are the same
    candies3 = [7, 7, 7, 7, 7]
    print(countUniqueCandies(candies3))  # Expected Output: 1

    # Test Case 4: Large input with mixed values
    candies4 = [i % 100 for i in range(100000)]
    print(countUniqueCandies(candies4))  # Expected Output: 100

    # Test Case 5: Negative and positive values
    candies5 = [-1, -2, -3, 1, 2, 3, -1, 1]
    print(countUniqueCandies(candies5))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function uses the `set` data structure to store unique elements from the input list.
- Constructing a set from a list takes O(n) time, where n is the length of the list.
- Therefore, the time complexity is O(n).

Space Complexity:
- The space complexity is O(u), where u is the number of unique elements in the list.
- In the worst case, all elements in the list are unique, so u = n.
- Therefore, the space complexity is O(n).

Topic: Hashing
"""