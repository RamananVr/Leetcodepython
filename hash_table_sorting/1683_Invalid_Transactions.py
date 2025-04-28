"""
LeetCode Problem #1683: Invalid Transactions

Problem Statement:
A transaction is possibly invalid if:
- the amount exceeds $1000, or;
- if it occurs within (and including) 60 minutes of another transaction with the same name in a different city.

You are given an array of strings `transactions` where transactions[i] consists of comma-separated values representing the name, time (in minutes), amount, and city of the transaction.

Return a list of transactions that are possibly invalid. You may return the answer in any order.

Constraints:
- 1 <= transactions.length <= 1000
- Each `transactions[i]` consists of comma-separated values: name, time, amount, and city.
- Each `name` and `city` consist of lowercase English letters, and have lengths between 1 and 10.
- Each `time` and `amount` consist of digits, and have lengths between 1 and 4.
- The input is guaranteed to be valid.

Example:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]

Input: transactions = ["alice,20,800,mtv","alice,50,1200,mtv"]
Output: ["alice,50,1200,mtv"]

Input: transactions = ["alice,20,800,mtv","bob,50,1200,mtv"]
Output: ["bob,50,1200,mtv"]
"""

from collections import defaultdict

def invalidTransactions(transactions):
    # Parse transactions into structured data
    parsed_transactions = []
    for i, transaction in enumerate(transactions):
        name, time, amount, city = transaction.split(',')
        parsed_transactions.append((name, int(time), int(amount), city, i))
    
    # Identify invalid transactions
    invalid = set()
    transactions_by_name = defaultdict(list)
    
    for name, time, amount, city, idx in parsed_transactions:
        # Add transaction to the name-based dictionary
        transactions_by_name[name].append((time, amount, city, idx))
        
        # Check if the transaction itself is invalid due to amount
        if amount > 1000:
            invalid.add(idx)
    
    # Check for transactions within 60 minutes in different cities
    for name, records in transactions_by_name.items():
        records.sort()  # Sort by time
        for i in range(len(records)):
            for j in range(i + 1, len(records)):
                time1, amount1, city1, idx1 = records[i]
                time2, amount2, city2, idx2 = records[j]
                if abs(time1 - time2) > 60:
                    break  # No need to check further as records are sorted by time
                if city1 != city2:
                    invalid.add(idx1)
                    invalid.add(idx2)
    
    # Return the invalid transactions
    return [transactions[i] for i in invalid]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions1 = ["alice,20,800,mtv","alice,50,100,beijing"]
    print(invalidTransactions(transactions1))  # Output: ["alice,20,800,mtv","alice,50,100,beijing"]

    # Test Case 2
    transactions2 = ["alice,20,800,mtv","alice,50,1200,mtv"]
    print(invalidTransactions(transactions2))  # Output: ["alice,50,1200,mtv"]

    # Test Case 3
    transactions3 = ["alice,20,800,mtv","bob,50,1200,mtv"]
    print(invalidTransactions(transactions3))  # Output: ["bob,50,1200,mtv"]

    # Test Case 4
    transactions4 = ["alice,20,800,mtv","alice,50,100,mtv","alice,51,100,beijing"]
    print(invalidTransactions(transactions4))  # Output: ["alice,51,100,beijing"]

"""
Time Complexity Analysis:
- Parsing the transactions takes O(n), where n is the number of transactions.
- Sorting the transactions for each name takes O(k log k) for each name, where k is the number of transactions for that name.
  In the worst case, all transactions belong to the same name, so this step is O(n log n).
- The nested loop to compare transactions for each name takes O(k^2) for each name. In the worst case, this is O(n^2).
- Overall time complexity: O(n^2) in the worst case.

Space Complexity Analysis:
- The space used for storing parsed transactions and the dictionary is O(n).
- Overall space complexity: O(n).

Topic: Hash Table, Sorting
"""