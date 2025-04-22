"""
LeetCode Question #721: Accounts Merge

Problem Statement:
Given a list of accounts where each element `accounts[i]` is a list of strings, where the first element `accounts[i][0]` is the name of the account, and the rest of the elements are emails belonging to that account. Now, we want to merge these accounts. Two accounts can be merged if they have at least one email in common. After merging the accounts, return the accounts in the following format:

1. Each account in the result should be represented by a list where the first element is the name and the rest of the elements are emails in sorted order.
2. The accounts themselves can be returned in any order.

Example:
Input: accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], 
                   ["John", "johnnybravo@mail.com"], 
                   ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
                   ["Mary", "mary@mail.com"]]
Output: [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
         ["John", "johnnybravo@mail.com"], 
         ["Mary", "mary@mail.com"]]

Constraints:
- `1 <= accounts.length <= 1000`
- `2 <= accounts[i].length <= 10`
- `1 <= accounts[i][j].length <= 30`
- `accounts[i][0]` consists of English letters.
- `accounts[i][j]` (for `j > 0`) is a valid email.
"""

# Python Solution
from collections import defaultdict

def accountsMerge(accounts):
    def dfs(email, visited, graph, merged_emails):
        visited.add(email)
        merged_emails.append(email)
        for neighbor in graph[email]:
            if neighbor not in visited:
                dfs(neighbor, visited, graph, merged_emails)

    # Step 1: Build the graph
    graph = defaultdict(list)
    email_to_name = {}
    for account in accounts:
        name = account[0]
        emails = account[1:]
        for email in emails:
            email_to_name[email] = name
            graph[emails[0]].append(email)
            graph[email].append(emails[0])

    # Step 2: Perform DFS to find connected components
    visited = set()
    result = []
    for email in email_to_name:
        if email not in visited:
            merged_emails = []
            dfs(email, visited, graph, merged_emails)
            merged_emails.sort()
            result.append([email_to_name[email]] + merged_emails)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    accounts1 = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ]
    print(accountsMerge(accounts1))
    # Expected Output:
    # [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], 
    #  ["John", "johnnybravo@mail.com"], 
    #  ["Mary", "mary@mail.com"]]

    # Test Case 2
    accounts2 = [
        ["Alice", "alice@mail.com", "alice2@mail.com"],
        ["Alice", "alice2@mail.com", "alice3@mail.com"],
        ["Bob", "bob@mail.com"]
    ]
    print(accountsMerge(accounts2))
    # Expected Output:
    # [["Alice", "alice@mail.com", "alice2@mail.com", "alice3@mail.com"], 
    #  ["Bob", "bob@mail.com"]]

    # Test Case 3
    accounts3 = [
        ["Charlie", "charlie@mail.com"],
        ["Charlie", "charlie@mail.com", "charlie2@mail.com"],
        ["Charlie", "charlie2@mail.com", "charlie3@mail.com"]
    ]
    print(accountsMerge(accounts3))
    # Expected Output:
    # [["Charlie", "charlie@mail.com", "charlie2@mail.com", "charlie3@mail.com"]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the graph takes O(N * K), where N is the number of accounts and K is the average number of emails per account.
- DFS traversal takes O(N * K) in the worst case, as we visit each email and its neighbors.
- Sorting the emails for each connected component takes O(A * log(A)), where A is the total number of unique emails.
Overall, the time complexity is O(N * K + A * log(A)).

Space Complexity:
- The graph and email_to_name dictionary use O(N * K) space.
- The visited set and merged_emails list use O(A) space.
Overall, the space complexity is O(N * K + A).
"""

# Topic: Graphs