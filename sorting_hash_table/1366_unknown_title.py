"""
LeetCode Problem #1366: Rank Teams by Votes

Problem Statement:
In a special ranking system, each voter gives a rank from highest to lowest to all teams participated in the competition. 
The ranking is represented by a string, where each character is a team. 
The i-th position in the string represents the i-th rank (1-indexed) of that voter. 

For example, "ABC" means that the voter likes team A the most, team B the second most, and team C the least.

Given an array of strings `votes` which represents the votes of all voters in the ranking system, 
return a string of all teams sorted by their rank based on the votes.

The ranking should be based on the following rules:
1. The primary ranking criteria is the number of votes each team received for the 1st position, 2nd position, etc.
2. If two teams have the same rank, the team with the lexicographically smaller letter ranks higher.

Return the final ranking as a single string.

Constraints:
- `1 <= votes.length <= 1000`
- `1 <= votes[i].length <= 26`
- `votes[i].length == votes[j].length` for all `i, j`.
- All characters in `votes[i]` are unique.
- All the characters in `votes[i]` will be uppercase English letters.
"""

# Python Solution
from collections import defaultdict

def rankTeams(votes):
    # Initialize a dictionary to store the rank counts for each team
    rank_count = defaultdict(lambda: [0] * len(votes[0]))
    
    # Populate the rank_count dictionary based on votes
    for vote in votes:
        for i, team in enumerate(vote):
            rank_count[team][i] += 1
    
    # Sort the teams based on rank counts and lexicographical order
    sorted_teams = sorted(rank_count.keys(), key=lambda team: (rank_count[team], -ord(team)), reverse=True)
    
    # Return the final ranking as a string
    return ''.join(sorted_teams)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    votes1 = ["ABC", "ACB", "ABC", "ACB", "ACB"]
    print(rankTeams(votes1))  # Output: "ACB"

    # Test Case 2
    votes2 = ["WXYZ", "XYZW"]
    print(rankTeams(votes2))  # Output: "XWYZ"

    # Test Case 3
    votes3 = ["ZMNAGUEDSJYLBOPHRQICWFXTVK"]
    print(rankTeams(votes3))  # Output: "ZMNAGUEDSJYLBOPHRQICWFXTVK"

    # Test Case 4
    votes4 = ["BCA", "CAB", "CBA", "ABC", "ACB", "BAC"]
    print(rankTeams(votes4))  # Output: "ABC"

    # Test Case 5
    votes5 = ["M", "M", "M", "M"]
    print(rankTeams(votes5))  # Output: "M"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the rank_count dictionary takes O(n * m), where n is the number of votes and m is the length of each vote.
- Sorting the teams takes O(t * log(t)), where t is the number of unique teams (at most 26).
- Overall time complexity: O(n * m + t * log(t)).

Space Complexity:
- The rank_count dictionary uses O(t * m) space, where t is the number of unique teams and m is the length of each vote.
- Overall space complexity: O(t * m).
"""

# Topic: Sorting, Hash Table