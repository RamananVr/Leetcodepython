"""
LeetCode Problem #1733: Minimum Number of People to Teach

Problem Statement:
On a social media platform, there are `n` users numbered from `1` to `n`. Each user has a list of languages they know, and a list of friends. You are given an integer `n` and two arrays `languages` and `friendships` where:
- `languages[i]` is a list of languages the `i-th` user knows.
- `friendships[j] = [u, v]` indicates that user `u` and user `v` are friends.

The platform allows users to communicate only if they know at least one common language. You want to teach some users a new language so that all friends can communicate with each other. Return the minimum number of users you need to teach. Note that:
- You can teach a user any language, and the cost of teaching one language to one user is the same for all users.
- It is guaranteed that you can teach a language to a user.

Constraints:
- `2 <= n <= 500`
- `1 <= languages.length <= n`
- `1 <= languages[i].length <= 500`
- `1 <= languages[i][j] <= 500`
- `1 <= friendships.length <= 500`
- `1 <= friendships[j][0] < friendships[j][1] <= n`
- All the arrays are 1-indexed.

"""

from collections import defaultdict

def minimumTeachings(n, languages, friendships):
    # Convert languages to a set for each user for faster lookup
    languages = [set(lang) for lang in languages]
    
    # Find all pairs of friends who cannot communicate
    cannot_communicate = []
    for u, v in friendships:
        if not (languages[u - 1] & languages[v - 1]):  # No common language
            cannot_communicate.append((u, v))
    
    # If everyone can already communicate, no teaching is needed
    if not cannot_communicate:
        return 0
    
    # Count the number of users who need to learn each language
    teach_count = defaultdict(int)
    for lang in range(1, n + 1):
        users_to_teach = set()
        for u, v in cannot_communicate:
            if lang not in languages[u - 1]:
                users_to_teach.add(u)
            if lang not in languages[v - 1]:
                users_to_teach.add(v)
        teach_count[lang] = len(users_to_teach)
    
    # Return the minimum number of users to teach for any language
    return min(teach_count.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    languages = [[1], [2], [1, 2]]
    friendships = [[1, 2], [1, 3], [2, 3]]
    print(minimumTeachings(n, languages, friendships))  # Output: 1

    # Test Case 2
    n = 3
    languages = [[2], [1, 3], [1, 2], [3]]
    friendships = [[1, 4], [1, 2], [3, 4]]
    print(minimumTeachings(n, languages, friendships))  # Output: 2

    # Test Case 3
    n = 4
    languages = [[1, 2], [3, 4], [1, 4], [2, 3]]
    friendships = [[1, 2], [3, 4]]
    print(minimumTeachings(n, languages, friendships))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `L` be the maximum number of languages a user knows, `F` be the number of friendships, and `n` be the number of users.
- Checking if two users can communicate takes O(L) for each friendship, so finding all pairs of friends who cannot communicate takes O(F * L).
- For each language, we iterate over all friendships and users, resulting in O(F * n) for each language. Since there are `n` languages, this step takes O(F * n^2).
- Overall time complexity: O(F * L + F * n^2).

Space Complexity:
- Storing the set of languages for each user takes O(n * L).
- Storing the `cannot_communicate` list takes O(F).
- Storing the `teach_count` dictionary takes O(n).
- Overall space complexity: O(n * L + F).

Topic: Hash Table, Set, Simulation
"""