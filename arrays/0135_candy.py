"""
LeetCode Question #135: Candy

Problem Statement:
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:
1. Each child must have at least one candy.
2. Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the children as follows: [2,1,2]

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the children as follows: [1,2,1]

Constraints:
- n == ratings.length
- 1 <= n <= 2 * 10^4
- 0 <= ratings[i] <= 2 * 10^4
"""

# Clean, Correct Python Solution
def candy(ratings):
    """
    Calculate the minimum number of candies required to distribute to children
    based on their ratings.

    :param ratings: List[int] - List of ratings for children
    :return: int - Minimum number of candies required
    """
    n = len(ratings)
    candies = [1] * n

    # Left-to-right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Right-to-left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ratings1 = [1, 0, 2]
    print(candy(ratings1))  # Output: 5

    # Test Case 2
    ratings2 = [1, 2, 2]
    print(candy(ratings2))  # Output: 4

    # Test Case 3
    ratings3 = [1, 3, 4, 5, 2]
    print(candy(ratings3))  # Output: 11

    # Test Case 4
    ratings4 = [1, 2, 3, 4, 5]
    print(candy(ratings4))  # Output: 15

    # Test Case 5
    ratings5 = [5, 4, 3, 2, 1]
    print(candy(ratings5))  # Output: 15

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm involves two passes over the ratings array:
  1. Left-to-right pass: O(n)
  2. Right-to-left pass: O(n)
- Total time complexity: O(n)

Space Complexity:
- The candies array requires O(n) space.
- Total space complexity: O(n)
"""

# Topic: Arrays