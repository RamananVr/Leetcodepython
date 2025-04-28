"""
LeetCode Problem #1169: Invalid Transactions

Problem Statement:
A transaction is represented as a string array `transactions` where each transaction is in the format:
`"name,time,amount,city"`. Each transaction consists of:
- `name`: a string of lowercase English letters.
- `time`: an integer representing the time in minutes from 00:00.
- `amount`: an integer representing the transaction amount in dollars.
- `city`: a string of lowercase English letters.

A transaction is considered invalid if:
1. The amount exceeds $1000, or;
2. There exists another transaction with the same name within 60 minutes (inclusive) of the current transaction, but in a different city.

You need to return a list of all invalid transactions. You may return the answer in any order.

Constraints:
- `transactions.length <= 1000`
- Each `transactions[i]` consists of `name`, `time`, `amount`, and `city` separated by commas.
- Each `name` and `city` consist of lowercase English letters only.
- `1 <= name.length, city.length <= 10`
- `0 <= time <= 1000`
- `1 <= amount <= 2000`

Example:
Input: transactions = ["alice,20,800,mtv","alice,50,100,beijing"]
Output: ["alice,20,800,mtv","alice,50,100,beijing"]

Explanation:
- The first transaction is valid because the amount is less than $1000 and there is no conflicting transaction.
- The second transaction is invalid because it occurs within 60 minutes of the first transaction but in a different city.

"""

# Python Solution
from collections import defaultdict

def invalidTransactions(transactions):
    parsed_transactions = []
    for i, transaction in enumerate(transactions):
        name, time, amount, city = transaction.split(',')
        parsed_transactions.append((name, int(time), int(amount), city, i))
    
    invalid = set()
    transactions_by_name = defaultdict(list)
    
    for name, time, amount, city, idx in parsed_transactions:
        transactions_by_name[name].append((time, amount, city, idx))
    
    for name, trans_list in transactions_by_name.items():
        trans_list.sort()  # Sort by time
        for i, (time1, amount1, city1, idx1) in enumerate(trans_list):
            if amount1 > 1000:
                invalid.add(idx1)
            for j in range(i + 1, len(trans_list)):
                time2, amount2, city2, idx2 = trans_list[j]
                if time2 - time1 > 60:
                    break
                if city1 != city2:
                    invalid.add(idx1)
                    invalid.add(idx2)
    
    return [transactions[i] for i in invalid]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    transactions1 = ["alice,20,800,mtv", "alice,50,100,beijing"]
    print(invalidTransactions(transactions1))  # Output: ["alice,20,800,mtv", "alice,50,100,beijing"]

    # Test Case 2
    transactions2 = ["alice,20,800,mtv", "bob,50,1200,mtv"]
    print(invalidTransactions(transactions2))  # Output: ["bob,50,1200,mtv"]

    # Test Case 3
    transactions3 = ["alice,20,800,mtv", "alice,50,1200,mtv", "alice,51,100,beijing"]
    print(invalidTransactions(transactions3))  # Output: ["alice,50,1200,mtv", "alice,51,100,beijing"]

    # Test Case 4
    transactions4 = ["bob,689,1910,barcelona", "bob,832,1726,barcelona", "bob,820,596,bangkok"]
    print(invalidTransactions(transactions4))  # Output: ["bob,689,1910,barcelona", "bob,820,596,bangkok"]

# Time and Space Complexity Analysis
# Time Complexity:
# - Parsing the transactions takes O(n), where n is the number of transactions.
# - Grouping transactions by name takes O(n).
# - Sorting each group of transactions by time takes O(k * log(k)) for each group, where k is the size of the group.
#   In the worst case, all transactions belong to the same name, so sorting takes O(n * log(n)).
# - Comparing transactions within each group takes O(n) in the worst case.
# Overall, the time complexity is O(n * log(n)).

# Space Complexity:
# - Storing the parsed transactions and the grouped transactions takes O(n).
# - The invalid set takes O(n) in the worst case.
# Overall, the space complexity is O(n).

# Topic: Arrays, Sorting, Hash Table