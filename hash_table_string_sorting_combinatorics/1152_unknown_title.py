"""
LeetCode Problem #1152: Analyze User Website Visit Pattern

Problem Statement:
You are given two string arrays `username` and `website` and an integer array `timestamp`. All the given arrays are of the same length and the tuple `[username[i], timestamp[i], website[i]]` indicates that the user `username[i]` visited the website `website[i]` at time `timestamp[i]`.

A 3-sequence is a list of three websites (not necessarily distinct) and such a sequence is associated with a user if the user visited all the websites in the sequence in the same order. For example, the sequence `["home", "about", "career"]` is associated with the user if the user visited `home` then `about` then `career` at different timestamps.

The score of a 3-sequence is defined as the number of users who have that 3-sequence associated with them. Return the 3-sequence with the highest score. If there is a tie, return the lexicographically smallest sequence.

Example 1:
Input: 
username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"],
timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
Output: ["home", "about", "career"]

Example 2:
Input:
username = ["ua", "ua", "ua", "ub", "ub", "ub"],
timestamp = [1, 2, 3, 4, 5, 6],
website = ["a", "b", "a", "a", "b", "c"]
Output: ["a", "b", "a"]

Constraints:
- 3 <= username.length <= 50
- 1 <= username[i].length <= 10
- timestamp.length == username.length
- 1 <= timestamp[i] <= 10^9
- website.length == username.length
- 1 <= website[i].length <= 10
- It is guaranteed that there is at least one user who visited at least three websites.
- All the tuples `[username[i], timestamp[i], website[i]]` are unique.
"""

from collections import defaultdict, Counter
from itertools import combinations

def mostVisitedPattern(username, timestamp, website):
    # Step 1: Combine the data and sort by timestamp
    data = sorted(zip(timestamp, username, website))
    
    # Step 2: Group websites visited by each user
    user_visits = defaultdict(list)
    for _, user, site in data:
        user_visits[user].append(site)
    
    # Step 3: Count all 3-sequences across all users
    pattern_count = Counter()
    for user, sites in user_visits.items():
        # Generate all unique 3-sequences for the current user
        patterns = set(combinations(sites, 3))
        for pattern in patterns:
            pattern_count[pattern] += 1
    
    # Step 4: Find the 3-sequence with the highest score
    max_pattern = max(sorted(pattern_count), key=lambda p: pattern_count[p])
    return list(max_pattern)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    username1 = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
    timestamp1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    website1 = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
    print(mostVisitedPattern(username1, timestamp1, website1))  # Output: ["home", "about", "career"]

    # Test Case 2
    username2 = ["ua", "ua", "ua", "ub", "ub", "ub"]
    timestamp2 = [1, 2, 3, 4, 5, 6]
    website2 = ["a", "b", "a", "a", "b", "c"]
    print(mostVisitedPattern(username2, timestamp2, website2))  # Output: ["a", "b", "a"]

# Time Complexity Analysis:
# - Sorting the data takes O(n log n), where n is the length of the input arrays.
# - Grouping websites by user takes O(n).
# - Generating all 3-sequences for each user takes O(k * C(m, 3)), where k is the number of users and m is the average number of websites visited by a user.
# - Counting the patterns takes O(total_patterns), where total_patterns is the total number of unique 3-sequences.
# Overall, the time complexity is approximately O(n log n + k * m^3), assuming m is small.

# Space Complexity Analysis:
# - Storing the sorted data takes O(n).
# - Storing user visits and pattern counts takes O(n + total_patterns).
# Overall, the space complexity is O(n + total_patterns).

# Topic: Hash Table, String, Sorting, Combinatorics