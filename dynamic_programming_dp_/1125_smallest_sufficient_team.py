"""
LeetCode Question #1125: Smallest Sufficient Team

Problem Statement:
In a project, you have a list of required skills `req_skills`, and a list of people. The `i-th` person has a subset of skills `people[i]`. 
Consider a sufficient team: a set of people such that for every required skill in `req_skills`, there is at least one person in the team who has that skill. 
We can represent a team by the indices of the people in it.

Return any sufficient team of the smallest possible size, represented by the indices of the people.

It is guaranteed an answer exists.

Example 1:
Input: req_skills = ["java", "nodejs", "reactjs"], people = [["java"],["nodejs"],["nodejs","reactjs"]]
Output: [0,2]

Example 2:
Input: req_skills = ["algorithms","math","java","reactjs","csharp","aws"], 
people = [["algorithms","math","java"],["algorithms","math","reactjs"],["java","csharp","aws"],["reactjs","csharp"],["csharp","math"],["aws","java"]]
Output: [1,2]

Constraints:
- 1 <= req_skills.length <= 16
- 1 <= people.length <= 60
- 1 <= people[i].length <= 16
- req_skills and people[i] consist of lowercase English letters.
- Every skill in people[i] is a skill in req_skills.
- It is guaranteed a sufficient team exists.
"""

# Python Solution
from typing import List

def smallestSufficientTeam(req_skills: List[str], people: List[List[str]]) -> List[int]:
    n = len(req_skills)
    skill_to_index = {skill: i for i, skill in enumerate(req_skills)}
    dp = {0: []}  # dp[mask] = list of indices of people forming the team for skill mask
    
    for i, person_skills in enumerate(people):
        person_mask = 0
        for skill in person_skills:
            if skill in skill_to_index:
                person_mask |= (1 << skill_to_index[skill])
        
        new_dp = dp.copy()
        for skill_mask, team in dp.items():
            combined_mask = skill_mask | person_mask
            if combined_mask not in new_dp or len(new_dp[combined_mask]) > len(team) + 1:
                new_dp[combined_mask] = team + [i]
        dp = new_dp
    
    return dp[(1 << n) - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    req_skills = ["java", "nodejs", "reactjs"]
    people = [["java"], ["nodejs"], ["nodejs", "reactjs"]]
    print(smallestSufficientTeam(req_skills, people))  # Output: [0, 2]

    # Test Case 2
    req_skills = ["algorithms", "math", "java", "reactjs", "csharp", "aws"]
    people = [["algorithms", "math", "java"], ["algorithms", "math", "reactjs"], ["java", "csharp", "aws"], 
              ["reactjs", "csharp"], ["csharp", "math"], ["aws", "java"]]
    print(smallestSufficientTeam(req_skills, people))  # Output: [1, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the number of required skills and `m` be the number of people.
- The number of skill masks is `2^n` since each skill can either be included or not.
- For each person, we iterate over all existing masks in the DP table, which can be up to `2^n`.
- Therefore, the time complexity is O(m * 2^n).

Space Complexity:
- The DP table stores up to `2^n` masks, each associated with a list of indices of people.
- The space complexity is O(2^n * k), where `k` is the average size of the team stored for each mask.
"""
# Topic: Dynamic Programming (DP)