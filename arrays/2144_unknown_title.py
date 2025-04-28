"""
LeetCode Problem #2144: Minimum Cost of Buying Candies With Discount

Problem Statement:
A shop is selling candies at a discount. For every three candies you buy, the shop gives you the cheapest one for free.

You are given a 0-indexed integer array `cost`, where `cost[i]` denotes the cost of the ith candy. Return the minimum cost of buying all the candies.

Example 1:
Input: cost = [1,2,3]
Output: 5
Explanation: Buy candies with costs 2 and 3, and get the candy with cost 1 for free.
The total cost = 2 + 3 = 5.

Example 2:
Input: cost = [6,5,7,9,2,2]
Output: 23
Explanation: Buy candies with costs 9, 7, and 6, and get the candy with cost 2 for free.
The total cost = 9 + 7 + 6 + 5 + 2 = 23.

Example 3:
Input: cost = [5,5]
Output: 10
Explanation: There are only two candies, so you buy both without any discount.
The total cost = 5 + 5 = 10.

Constraints:
- 1 <= cost.length <= 100
- 1 <= cost[i] <= 100
"""

# Python Solution
def minimumCost(cost):
    """
    Calculate the minimum cost of buying all candies with the discount.

    :param cost: List[int] - List of candy costs
    :return: int - Minimum cost to buy all candies
    """
    # Sort the costs in descending order
    cost.sort(reverse=True)
    
    # Initialize total cost
    total_cost = 0
    
    # Iterate through the sorted costs
    for i in range(len(cost)):
        # Add the cost only if the candy is not the third one in a group
        if i % 3 != 2:
            total_cost += cost[i]
    
    return total_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost1 = [1, 2, 3]
    print(minimumCost(cost1))  # Output: 5

    # Test Case 2
    cost2 = [6, 5, 7, 9, 2, 2]
    print(minimumCost(cost2))  # Output: 23

    # Test Case 3
    cost3 = [5, 5]
    print(minimumCost(cost3))  # Output: 10

    # Test Case 4
    cost4 = [3, 3, 3, 3]
    print(minimumCost(cost4))  # Output: 9

    # Test Case 5
    cost5 = [1]
    print(minimumCost(cost5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so no additional space is used apart from a few variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays