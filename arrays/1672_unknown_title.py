"""
LeetCode Problem #1672: Richest Customer Wealth

Problem Statement:
You are given an m x n integer grid `accounts` where `accounts[i][j]` is the amount of money the i-th customer has in the j-th bank. 
Return the wealth that the richest customer has.

A customer's wealth is the sum of money they have in all their bank accounts. 
The richest customer is the customer that has the maximum wealth.

Example 1:
Input: accounts = [[1,2,3],[3,2,1]]
Output: 6
Explanation:
1st customer has wealth = 1 + 2 + 3 = 6
2nd customer has wealth = 3 + 2 + 1 = 6
Both customers are considered the richest with a wealth of 6, so return 6.

Example 2:
Input: accounts = [[1,5],[7,3],[3,5]]
Output: 10
Explanation:
1st customer has wealth = 1 + 5 = 6
2nd customer has wealth = 7 + 3 = 10
3rd customer has wealth = 3 + 5 = 8
The 2nd customer is the richest with a wealth of 10.

Example 3:
Input: accounts = [[2,8,7],[7,1,3],[1,9,5]]
Output: 17

Constraints:
- m == accounts.length
- n == accounts[i].length
- 1 <= m, n <= 50
- 1 <= accounts[i][j] <= 100
"""

# Python Solution
def maximumWealth(accounts):
    """
    This function calculates the maximum wealth among all customers.

    :param accounts: List[List[int]] - A 2D list where accounts[i][j] represents the money
                                       the i-th customer has in the j-th bank.
    :return: int - The maximum wealth of any customer.
    """
    return max(sum(customer) for customer in accounts)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    accounts1 = [[1, 2, 3], [3, 2, 1]]
    print(maximumWealth(accounts1))  # Output: 6

    # Test Case 2
    accounts2 = [[1, 5], [7, 3], [3, 5]]
    print(maximumWealth(accounts2))  # Output: 10

    # Test Case 3
    accounts3 = [[2, 8, 7], [7, 1, 3], [1, 9, 5]]
    print(maximumWealth(accounts3))  # Output: 17

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let m be the number of customers (rows in the accounts list) and n be the number of banks (columns in the accounts list).
- For each customer, we calculate the sum of their wealth, which takes O(n) time.
- We do this for all m customers, so the total time complexity is O(m * n).

Space Complexity:
- The solution uses a generator expression to calculate the sum of each customer's wealth, which does not require additional space.
- Therefore, the space complexity is O(1) (excluding the input).

Overall:
Time Complexity: O(m * n)
Space Complexity: O(1)
"""

# Topic: Arrays