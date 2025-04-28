"""
LeetCode Problem #1583: Count Unhappy Friends

Problem Statement:
You are given a list of preferences for n friends, where n is even. Each friend is numbered from 0 to n - 1. 
You are also given a list of pairs, where pairs[i] = [xi, yi] indicates that friend xi is paired with friend yi 
and friend yi is paired with friend xi.

Friend x is unhappy if:
1. x is paired with y, and
2. there exists a friend u who is not paired with x, but:
   - x prefers u over y, and
   - u prefers x over the friend u is paired with.

Return the number of unhappy friends.

Example:
Input: n = 4, preferences = [[1,2,3],[3,2,0],[3,1,0],[1,2,0]], pairs = [[0,1],[2,3]]
Output: 2

Constraints:
- 2 <= n <= 500
- n is even.
- preferences.length == n
- preferences[i].length == n - 1
- 0 <= preferences[i][j] <= n - 1
- preferences[i] does not contain i.
- All values in preferences[i] are unique.
- pairs.length == n / 2
- pairs[i].length == 2
- xi != yi
- 0 <= xi, yi <= n - 1
- Each person is paired with exactly one other person.

"""

# Solution
def unhappyFriends(n, preferences, pairs):
    # Create a dictionary to store the pairings
    pair_map = {}
    for x, y in pairs:
        pair_map[x] = y
        pair_map[y] = x

    # Create a dictionary to store the preference rankings
    rank = [{} for _ in range(n)]
    for i in range(n):
        for j, friend in enumerate(preferences[i]):
            rank[i][friend] = j

    # Count the number of unhappy friends
    unhappy_count = 0
    for x in range(n):
        y = pair_map[x]
        for u in preferences[x]:
            if rank[x][u] < rank[x][y]:  # x prefers u over y
                v = pair_map[u]
                if rank[u][x] < rank[u][v]:  # u prefers x over v
                    unhappy_count += 1
                    break

    return unhappy_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    preferences = [[1, 2, 3], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]
    print(unhappyFriends(n, preferences, pairs))  # Output: 2

    # Test Case 2
    n = 4
    preferences = [[1, 3, 2], [3, 2, 0], [3, 1, 0], [1, 2, 0]]
    pairs = [[0, 1], [2, 3]]
    print(unhappyFriends(n, preferences, pairs))  # Output: 4

    # Test Case 3
    n = 6
    preferences = [[1, 2, 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 3, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]]
    pairs = [[0, 1], [2, 3], [4, 5]]
    print(unhappyFriends(n, preferences, pairs))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the pair_map takes O(n).
- Constructing the rank dictionary takes O(n^2) since we iterate over all preferences.
- For each friend x, we iterate over their preferences, which takes O(n) in the worst case. 
  This results in a total of O(n^2) for the nested loop.
- Overall time complexity: O(n^2).

Space Complexity:
- The pair_map dictionary takes O(n) space.
- The rank dictionary takes O(n^2) space.
- Overall space complexity: O(n^2).
"""

# Topic: Arrays