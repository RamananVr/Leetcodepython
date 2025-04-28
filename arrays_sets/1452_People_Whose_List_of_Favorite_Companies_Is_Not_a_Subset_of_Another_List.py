"""
LeetCode Problem #1452: People Whose List of Favorite Companies Is Not a Subset of Another List

Problem Statement:
Given the array `favoriteCompanies` where `favoriteCompanies[i]` is the list of favorite companies for the ith person (indexed from 0), return a list of indices of people whose list of favorite companies is not a subset of any other list of favorite companies. You must return the indices in increasing order.

A list `a` is a subset of list `b` if all elements of `a` are also elements of `b`.

Constraints:
1. 1 <= favoriteCompanies.length <= 100
2. 1 <= favoriteCompanies[i].length <= 500
3. 1 <= favoriteCompanies[i][j].length <= 20
4. All strings in `favoriteCompanies[i]` are distinct.
5. All lists of favorite companies are distinct, i.e., if `i != j`, then `favoriteCompanies[i] != favoriteCompanies[j]`.

Example:
Input: favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
Output: [0,1,4]
Explanation:
- Person with index 0 has favorite companies ["leetcode","google","facebook"], which is not a subset of any other list.
- Person with index 1 has favorite companies ["google","microsoft"], which is not a subset of any other list.
- Person with index 2 has favorite companies ["google","facebook"], which is a subset of the list of person 0.
- Person with index 3 has favorite companies ["google"], which is a subset of the list of person 0.
- Person with index 4 has favorite companies ["amazon"], which is not a subset of any other list.

"""

# Python Solution
def peopleIndexes(favoriteCompanies):
    # Convert each list of favorite companies to a set for efficient subset checking
    favoriteSets = [set(companies) for companies in favoriteCompanies]
    result = []

    for i in range(len(favoriteSets)):
        isSubset = False
        for j in range(len(favoriteSets)):
            if i != j and favoriteSets[i].issubset(favoriteSets[j]):
                isSubset = True
                break
        if not isSubset:
            result.append(i)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    favoriteCompanies1 = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
    print(peopleIndexes(favoriteCompanies1))  # Output: [0, 1, 4]

    # Test Case 2
    favoriteCompanies2 = [["apple","google"],["google"],["amazon"],["apple","google","amazon"]]
    print(peopleIndexes(favoriteCompanies2))  # Output: [0, 2, 3]

    # Test Case 3
    favoriteCompanies3 = [["a","b","c"],["a","b"],["c"],["a","b","c","d"]]
    print(peopleIndexes(favoriteCompanies3))  # Output: [0, 2, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of people (length of favoriteCompanies) and m be the average number of companies in each list.
- For each person i, we compare their list with every other person j, resulting in O(n^2) comparisons.
- Checking if one set is a subset of another takes O(m) time in the worst case.
- Overall time complexity: O(n^2 * m).

Space Complexity:
- We store the favorite companies as sets, which takes O(n * m) space in the worst case.
- The result list takes O(n) space.
- Overall space complexity: O(n * m).
"""

# Topic: Arrays, Sets