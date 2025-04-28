"""
LeetCode Problem #1798: Maximum Number of Consecutive Values You Can Make

Problem Statement:
You are given an integer array `coins` of length `n` which represents the coins that you have. 
The value of a coin is the coin's denomination. You can make some value `x` if you can sum up 
some of your coins' denominations such that the sum equals `x`. Return the maximum number of 
consecutive integer values that you can make with your coins starting from 1.

Example:
Input: coins = [1, 3]
Output: 2
Explanation: You can make the following values:
- 1: Take the coin of denomination 1.
- 2: You cannot make this value since no combination of coins sums to 2.
- 3: Take the coin of denomination 3.
Thus, you can make 2 consecutive integer values starting from 1.

Input: coins = [1, 1, 1, 4]
Output: 8
Explanation: You can make the following values:
- 1, 2, 3: Take one coin of denomination 1 for each value.
- 4: Take the coin of denomination 4.
- 5, 6, 7, 8: Use combinations of coins to make these values.
Thus, you can make 8 consecutive integer values starting from 1.

Constraints:
- `coins.length == n`
- `1 <= n <= 4 * 10^4`
- `1 <= coins[i] <= 10^9`
"""

# Python Solution
def getMaximumConsecutive(coins):
    """
    Function to calculate the maximum number of consecutive integer values 
    that can be made starting from 1 using the given coins.

    :param coins: List[int] - List of coin denominations
    :return: int - Maximum number of consecutive values starting from 1
    """
    coins.sort()
    max_consecutive = 0

    for coin in coins:
        if coin > max_consecutive + 1:
            break
        max_consecutive += coin

    return max_consecutive + 1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    coins = [1, 3]
    print(getMaximumConsecutive(coins))  # Output: 2

    # Test Case 2
    coins = [1, 1, 1, 4]
    print(getMaximumConsecutive(coins))  # Output: 8

    # Test Case 3
    coins = [1, 2, 5]
    print(getMaximumConsecutive(coins))  # Output: 9

    # Test Case 4
    coins = [5, 7, 1, 1, 2, 3, 22]
    print(getMaximumConsecutive(coins))  # Output: 20

    # Test Case 5
    coins = [1]
    print(getMaximumConsecutive(coins))  # Output: 2


# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the coins array takes O(n log n), where n is the number of coins.
- Iterating through the sorted array takes O(n).
- Thus, the overall time complexity is O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it operates directly on the input array and uses a few variables.
- Thus, the space complexity is O(1).
"""

# Topic: Arrays, Greedy Algorithm