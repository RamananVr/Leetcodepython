"""
LeetCode Problem #2285: Maximum Total Importance of Roads

Problem Statement:
You are given an integer `n` denoting the number of cities and a 2D integer array `roads` where 
`roads[i] = [a_i, b_i]` denotes that there exists a bidirectional road connecting cities `a_i` and `b_i`.

You need to assign each city a value from `1` to `n`, such that each value is used exactly once. 
The importance of a road is defined as the sum of the values of the two cities it connects.

Return the maximum total importance of all roads.

Constraints:
- `2 <= n <= 5 * 10^4`
- `1 <= roads.length <= 5 * 10^4`
- `roads[i].length == 2`
- `0 <= a_i, b_i <= n - 1`
- `a_i != b_i`
- There are no duplicate roads.

"""

# Solution
def maximumImportance(n: int, roads: list[list[int]]) -> int:
    # Step 1: Calculate the degree (number of connections) for each city
    degree = [0] * n
    for a, b in roads:
        degree[a] += 1
        degree[b] += 1

    # Step 2: Sort cities by their degree in descending order
    sorted_cities = sorted(range(n), key=lambda x: degree[x], reverse=True)

    # Step 3: Assign importance values from n to 1 based on sorted order
    importance = [0] * n
    for i, city in enumerate(sorted_cities):
        importance[city] = n - i

    # Step 4: Calculate the total importance of all roads
    total_importance = 0
    for a, b in roads:
        total_importance += importance[a] + importance[b]

    return total_importance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    roads1 = [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]
    print(maximumImportance(n1, roads1))  # Expected Output: 43

    # Test Case 2
    n2 = 3
    roads2 = [[0, 1], [1, 2], [0, 2]]
    print(maximumImportance(n2, roads2))  # Expected Output: 20

    # Test Case 3
    n3 = 4
    roads3 = [[0, 1], [1, 2], [2, 3]]
    print(maximumImportance(n3, roads3))  # Expected Output: 19

"""
Time and Space Complexity Analysis:

Time Complexity:
1. Calculating the degree of each city: O(m), where m is the number of roads.
2. Sorting the cities by degree: O(n log n), where n is the number of cities.
3. Assigning importance values: O(n).
4. Calculating the total importance: O(m).

Overall time complexity: O(n log n + m).

Space Complexity:
1. Degree array: O(n).
2. Sorted cities array: O(n).
3. Importance array: O(n).

Overall space complexity: O(n).

Topic: Graphs
"""