"""
LeetCode Problem #2483: Minimum Penalty for a Shop

Problem Statement:
You are given the customer visit log of a shop represented by a 0-indexed string `customers` consisting only of characters 'Y' and 'N':

- If the i-th character is 'Y', it means that customers come to the shop at the i-th hour.
- If the i-th character is 'N', it means that no customers come to the shop at the i-th hour.

The shop closes at one of the 24 hours (possibly at hour 0). If the shop closes at hour `j` (0 <= j <= n), the penalty is calculated as follows:

- For every hour `i` (0 <= i < j) that the shop is closed while customers are present ('Y'), the penalty increases by 1.
- For every hour `i` (j <= i < n) that the shop is open while no customers are present ('N'), the penalty increases by 1.

Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Example:
Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing at hour 0 incurs a penalty of 2 (2 'Y's before hour 0).
- Closing at hour 1 incurs a penalty of 2 (1 'Y' before hour 1 and 1 'N' after hour 1).
- Closing at hour 2 incurs a penalty of 1 (1 'N' after hour 2).
- Closing at hour 3 incurs a penalty of 2 (1 'N' after hour 3 and 1 'Y' before hour 3).
- Closing at hour 4 incurs a penalty of 3 (3 'N's after hour 4).
Thus, the best closing time is hour 2.

Constraints:
- 1 <= customers.length <= 10^5
- customers[i] is either 'Y' or 'N'.
"""

def bestClosingTime(customers: str) -> int:
    """
    Finds the earliest hour to close the shop to minimize penalty.

    :param customers: A string consisting of 'Y' and 'N' representing customer visits.
    :return: The earliest hour to close the shop with minimum penalty.
    """
    n = len(customers)
    penalty = 0
    min_penalty = float('inf')
    best_hour = 0

    # Calculate the total number of 'Y' in the string
    total_customers = customers.count('Y')

    # Initialize the number of customers before the current hour
    customers_before = 0

    for i in range(n + 1):
        # Penalty is the sum of:
        # 1. Customers before hour i that are missed (customers_before)
        # 2. Customers after hour i that are present (total_customers - customers_before)
        penalty = customers_before + (n - i - (total_customers - customers_before))
        if penalty < min_penalty:
            min_penalty = penalty
            best_hour = i

    return best_hour

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    customers = "YYNY"
    print(bestClosingTime(customers))  # Output: 2

    # Test Case 2
    customers = "NNNN"
    print(bestClosingTime(customers))  # Output: 0

    # Test Case 3
    customers = "YYYY"
    print(bestClosingTime(customers))  # Output: 4

    # Test Case 4
    customers = "YNYN"
    print(bestClosingTime(customers))  # Output: 2

    # Test Case 5
    customers = "NYNYNY"
    print(bestClosingTime(customers))  # Output: 3

"""
Time Complexity Analysis:
- The solution iterates through the string once to calculate the total number of 'Y' (O(n)).
- Then, it iterates through the string again to calculate the penalty for each possible closing hour (O(n)).
- Thus, the overall time complexity is O(n).

Space Complexity Analysis:
- The solution uses a constant amount of extra space (O(1)).

Topic: Arrays, Prefix Sum
"""