"""
LeetCode Problem #1479: Sales by Day of the Week

Problem Statement:
You are given a 2D array `sales` where `sales[i] = [day, amount]` represents that on the `i-th` transaction, 
a sale of `amount` was made on the day `day`. The days are represented as integers from 0 to 6, where 0 is Sunday, 
1 is Monday, and so on.

Your task is to return an array `result` of size 7, where `result[i]` is the total sales made on the `i-th` day of the week.

Example:
Input: sales = [[0, 100], [1, 200], [0, 50], [6, 300], [6, 100], [2, 400]]
Output: [150, 200, 400, 0, 0, 0, 400]

Constraints:
- `1 <= sales.length <= 10^4`
- `0 <= day <= 6`
- `0 <= amount <= 10^4`
"""

def total_sales_by_day(sales):
    """
    Calculate total sales for each day of the week.

    :param sales: List[List[int]] - A list of transactions where each transaction is [day, amount].
    :return: List[int] - A list of total sales for each day of the week.
    """
    # Initialize an array of size 7 to store total sales for each day
    result = [0] * 7

    # Iterate through the sales transactions
    for day, amount in sales:
        result[day] += amount

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sales = [[0, 100], [1, 200], [0, 50], [6, 300], [6, 100], [2, 400]]
    print(total_sales_by_day(sales))  # Output: [150, 200, 400, 0, 0, 0, 400]

    # Test Case 2
    sales = [[3, 500], [3, 300], [4, 100], [0, 50]]
    print(total_sales_by_day(sales))  # Output: [50, 0, 0, 800, 100, 0, 0]

    # Test Case 3
    sales = [[0, 1000], [1, 2000], [2, 3000], [3, 4000], [4, 5000], [5, 6000], [6, 7000]]
    print(total_sales_by_day(sales))  # Output: [1000, 2000, 3000, 4000, 5000, 6000, 7000]

    # Test Case 4
    sales = []
    print(total_sales_by_day(sales))  # Output: [0, 0, 0, 0, 0, 0, 0]

    # Test Case 5
    sales = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]
    print(total_sales_by_day(sales))  # Output: [0, 0, 0, 0, 0, 0, 0]

"""
Time Complexity:
- The function iterates through the `sales` list once, performing a constant-time operation for each transaction.
- Let `n` be the length of the `sales` list.
- Time Complexity: O(n)

Space Complexity:
- The function uses a fixed-size array `result` of size 7 to store the total sales for each day.
- Space Complexity: O(1) (constant space)

Topic: Arrays
"""