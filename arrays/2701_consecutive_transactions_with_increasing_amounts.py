"""
LeetCode Problem #2701: Consecutive Transactions with Increasing Amounts

Problem Statement:
Table: Transactions
+------------------+------+
| Column Name      | Type |
+------------------+------+
| transaction_id   | int  |
| customer_id      | int  |
| transaction_date | date |
| amount           | int  |
+------------------+------+
transaction_id is the primary key for this table.
Each row contains information about one transaction.

Write an SQL query to find all customers who have made at least three consecutive transactions with increasing amounts.

Return the result table ordered by customer_id in ascending order.

Constraints:
- 1 <= transaction_id <= 10^5
- 1 <= customer_id <= 1000
- 1 <= amount <= 10^6
"""

def consecutive_transactions_with_increasing_amounts(transactions):
    """
    Find customers who have made at least three consecutive transactions with increasing amounts.

    :param transactions: List[List] - List of transactions [transaction_id, customer_id, transaction_date, amount].
    :return: List[int] - List of customer_ids who meet the criteria.
    """
    from collections import defaultdict
    
    # Group transactions by customer_id and sort by transaction_date
    customer_transactions = defaultdict(list)
    
    for transaction in transactions:
        transaction_id, customer_id, transaction_date, amount = transaction
        customer_transactions[customer_id].append((transaction_date, amount))
    
    result = set()
    
    for customer_id, txns in customer_transactions.items():
        # Sort transactions by date
        txns.sort()
        
        # Check for consecutive increasing amounts
        consecutive_count = 1
        
        for i in range(1, len(txns)):
            if txns[i][1] > txns[i-1][1]:  # amount is increasing
                consecutive_count += 1
                if consecutive_count >= 3:
                    result.add(customer_id)
                    break
            else:
                consecutive_count = 1
    
    return sorted(list(result))

def consecutive_transactions_optimized(transactions):
    """
    Optimized solution using sliding window approach.

    :param transactions: List[List] - List of transactions.
    :return: List[int] - List of customer_ids who meet the criteria.
    """
    from collections import defaultdict
    
    customer_transactions = defaultdict(list)
    
    for transaction in transactions:
        transaction_id, customer_id, transaction_date, amount = transaction
        customer_transactions[customer_id].append((transaction_date, amount))
    
    result = set()
    
    for customer_id, txns in customer_transactions.items():
        txns.sort()
        
        if len(txns) < 3:
            continue
        
        # Use sliding window to find consecutive increasing sequences
        for i in range(len(txns) - 2):
            if (txns[i][1] < txns[i+1][1] < txns[i+2][1]):
                result.add(customer_id)
                break
    
    return sorted(list(result))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions1 = [
        [1, 101, "2023-05-01", 100],
        [2, 101, "2023-05-02", 150],
        [3, 101, "2023-05-03", 200],
        [4, 102, "2023-05-01", 100],
        [5, 102, "2023-05-02", 50],
        [6, 102, "2023-05-03", 75]
    ]
    print(consecutive_transactions_with_increasing_amounts(transactions1))  # Output: [101]
    print(consecutive_transactions_optimized(transactions1))  # Output: [101]

    # Test Case 2
    transactions2 = [
        [1, 201, "2023-05-01", 100],
        [2, 201, "2023-05-02", 200],
        [3, 201, "2023-05-03", 300],
        [4, 201, "2023-05-04", 400],
        [5, 202, "2023-05-01", 500],
        [6, 202, "2023-05-02", 400],
        [7, 202, "2023-05-03", 600]
    ]
    print(consecutive_transactions_with_increasing_amounts(transactions2))  # Output: [201]

    # Test Case 3
    transactions3 = [
        [1, 301, "2023-05-01", 100],
        [2, 301, "2023-05-02", 50],
        [3, 301, "2023-05-03", 75],
        [4, 301, "2023-05-04", 100]
    ]
    print(consecutive_transactions_with_increasing_amounts(transactions3))  # Output: []

"""
Time Complexity Analysis:
- Sorting transactions for each customer takes O(T log T) where T is the number of transactions per customer.
- Checking consecutive increasing amounts takes O(T) for each customer.
- Overall time complexity is O(N * T log T) where N is the number of customers.

Space Complexity Analysis:
- We store transactions grouped by customer_id, which takes O(T) space.
- Therefore, the space complexity is O(T).

Topic: Arrays, Sorting, Sliding Window
"""
