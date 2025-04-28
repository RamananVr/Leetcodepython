"""
LeetCode Problem #911: Online Election

Problem Statement:
You are given two integer arrays `persons` and `times`. In an election, the `i-th` vote was cast for `persons[i]` at time `times[i]`.

For each query at a time `t`, find the person that was leading the election at time `t`. Votes cast at time `t` will count towards our query. In the case of a tie, the most recent vote (among tied candidates) wins.

Implement the `TopVotedCandidate` class:
- `TopVotedCandidate(int[] persons, int[] times)` Initializes the object with the `persons` and `times` arrays.
- `int q(int t)` Returns the number of the person that was leading the election at time `t`.

Constraints:
1. `1 <= persons.length <= 5000`
2. `times.length == persons.length`
3. `0 <= persons[i] < 10^9`
4. `0 <= times[i] <= 10^9`
5. `times` is sorted in a strictly increasing order.
6. `times[0] <= t <= 10^9`
7. All queries are made on valid `t`.

Example:
Input:
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    queries = [3, 12, 25, 15, 24, 8]

Output:
    [0, 1, 1, 0, 0, 1]

Explanation:
    At time 3, the votes are [0], and 0 is leading.
    At time 12, the votes are [0, 1, 1], and 1 is leading.
    At time 25, the votes are [0, 1, 1, 0, 0, 1], and 1 is leading.
    At time 15, the votes are [0, 1, 1, 0], and 0 is leading.
    At time 24, the votes are [0, 1, 1, 0, 0], and 0 is leading.
    At time 8, the votes are [0, 1, 1], and 1 is leading.
"""

from collections import defaultdict
import bisect

class TopVotedCandidate:
    def __init__(self, persons, times):
        self.leaders = []  # Stores the leader at each time
        self.times = times  # Stores the times
        vote_count = defaultdict(int)  # Tracks the vote count for each person
        leader = -1  # Current leader
        max_votes = 0  # Maximum votes at any point

        for person in persons:
            vote_count[person] += 1
            # Update the leader if the current person has more votes or ties with the leader
            if vote_count[person] >= max_votes:
                if person != leader:  # Only update if the leader changes
                    leader = person
                    self.leaders.append(leader)
                max_votes = vote_count[person]
            else:
                self.leaders.append(leader)

    def q(self, t):
        # Use binary search to find the latest time <= t
        idx = bisect.bisect_right(self.times, t) - 1
        return self.leaders[idx]


# Example Test Cases
if __name__ == "__main__":
    persons = [0, 1, 1, 0, 0, 1, 0]
    times = [0, 5, 10, 15, 20, 25, 30]
    queries = [3, 12, 25, 15, 24, 8]

    top_voted_candidate = TopVotedCandidate(persons, times)
    results = [top_voted_candidate.q(t) for t in queries]
    print("Results:", results)  # Expected Output: [0, 1, 1, 0, 0, 1]

"""
Time Complexity:
1. Initialization (`__init__`):
   - Iterates through the `persons` array once, so O(n), where n is the length of `persons`.
   - Updates the vote count and leader, which are O(1) operations.
   - Overall: O(n).

2. Query (`q`):
   - Uses binary search on the `times` array, which takes O(log n).
   - Overall: O(log n) per query.

Space Complexity:
- The `vote_count` dictionary stores vote counts for each person, which is O(k), where k is the number of unique persons.
- The `leaders` and `times` arrays each take O(n) space.
- Overall: O(n + k).

Topic: Binary Search
"""