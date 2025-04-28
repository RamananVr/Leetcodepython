"""
LeetCode Problem #2082: The Number of Rich Customers Who Made Purchases

Problem Statement:
You are given a 0-indexed 2D integer array `accounts` where `accounts[i][j]` is the amount of money the i-th customer has in the j-th bank. 
Return the number of customers that are considered "rich." A customer is considered "rich" if the sum of their money across all banks is strictly greater than the wealth of every other customer.

Constraints:
- `1 <= accounts.length <= 100`
- `1 <= accounts[i].length <= 50`
- `0 <= accounts[i][j] <= 10^6`
"""

def numberOfRichCustomers(accounts):
    """
    Function to calculate the number of rich customers.

    Args:
    accounts (List[List[int]]): A 2D list where accounts[i][j] represents the money
                                the i-th customer has in the j-th bank.

    Returns:
    int: The number of rich customers.
    """
    # Calculate the wealth of each customer
    wealths = [sum(account) for account in accounts]
    
    # Find the maximum wealth
    max_wealth = max(wealths)
    
    # Count the number of customers with wealth greater than max_wealth
    rich_count = sum(1 for wealth in wealths if wealth > max_wealth)
    
    return rich_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    accounts1 = [[1, 2, 3], [3, 2, 1], [4, 5, 6]]
    print(numberOfRichCustomers(accounts1))  # Expected Output: 1

    # Test Case 2
    accounts2 = [[10, 20, 30], [5, 5, 5], [15, 15, 15]]
    print(numberOfRichCustomers(accounts2))  # Expected Output: 1

    # Test Case 3
    accounts3 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
    print(numberOfRichCustomers(accounts3))  # Expected Output: 0

    # Test Case 4
    accounts4 = [[100], [200], [300], [400]]
    print(numberOfRichCustomers(accounts4))  # Expected Output: 1

"""
Time Complexity Analysis:
- Calculating the wealth of each customer takes O(m * n), where m is the number of customers and n is the number of banks.
- Finding the maximum wealth takes O(m).
- Counting the number of customers with wealth greater than max_wealth takes O(m).
- Overall time complexity: O(m * n).

Space Complexity Analysis:
- The `wealths` list stores the wealth of each customer, which takes O(m) space.
- Overall space complexity: O(m).

Topic: Arrays
"""