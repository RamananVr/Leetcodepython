"""
LeetCode Problem #1355: Activity Participants

Problem Statement:
You are given two lists of integers `favoriteCompanies` and `people`. 
Each `favoriteCompanies[i]` is a list of strings representing the favorite companies of the i-th person. 
You need to find the smallest set of people such that their favorite companies cover all the companies in the input.

Return the indices of the people in the smallest set in ascending order.

Constraints:
1. 1 <= len(favoriteCompanies) <= 100
2. 1 <= len(favoriteCompanies[i]) <= 100
3. 1 <= len(favoriteCompanies[i][j]) <= 100
4. All strings in favoriteCompanies[i] are unique.
5. All strings in favoriteCompanies are unique across all lists.

Example:
Input: favoriteCompanies = [["google", "facebook"], ["google"], ["facebook", "amazon"], ["amazon"]]
Output: [0, 2]
Explanation: The smallest set of people is [0, 2] because their favorite companies cover all companies.
"""

# Python Solution
from typing import List

def smallestSufficientTeam(favoriteCompanies: List[List[str]]) -> List[int]:
    # Convert each person's favorite companies into a set for easier comparison
    company_sets = [set(companies) for companies in favoriteCompanies]
    n = len(company_sets)
    
    # Resultant indices of the smallest sufficient team
    result = []
    
    # Iterate through each person
    for i in range(n):
        is_subset = False
        # Check if the current person's favorite companies are a subset of another person's
        for j in range(n):
            if i != j and company_sets[i].issubset(company_sets[j]):
                is_subset = True
                break
        # If not a subset, include this person in the result
        if not is_subset:
            result.append(i)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    favoriteCompanies1 = [["google", "facebook"], ["google"], ["facebook", "amazon"], ["amazon"]]
    print(smallestSufficientTeam(favoriteCompanies1))  # Output: [0, 2]

    # Test Case 2
    favoriteCompanies2 = [["google"], ["facebook"], ["amazon"]]
    print(smallestSufficientTeam(favoriteCompanies2))  # Output: [0, 1, 2]

    # Test Case 3
    favoriteCompanies3 = [["google", "facebook", "amazon"], ["google", "facebook"], ["amazon"]]
    print(smallestSufficientTeam(favoriteCompanies3))  # Output: [0]

    # Test Case 4
    favoriteCompanies4 = [["a", "b", "c"], ["a", "b"], ["c"]]
    print(smallestSufficientTeam(favoriteCompanies4))  # Output: [0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of people and m be the average number of companies per person.
- For each person, we check if their set of companies is a subset of another person's set.
- Checking subset takes O(m) time, and we do this for all pairs of people, leading to O(n^2 * m) in the worst case.

Space Complexity:
- We store the sets of companies for each person, which takes O(n * m) space.
- The result list takes O(n) space in the worst case.
- Overall space complexity is O(n * m).

Primary Topic: Sets
"""