"""
LeetCode Question #1436: Destination City

Problem Statement:
You are given the array `paths`, where `paths[i] = [cityA, cityB]` means there exists a direct path going from `cityA` to `cityB`.
Return the destination city, that is, the city without any outgoing paths.

It is guaranteed that the graph of paths forms a line without any loops, meaning there will be exactly one destination city.

Example 1:
Input: paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
Output: "Sao Paulo"
Explanation: Starting at "London" -> "New York" -> "Lima" -> "Sao Paulo", there are no more outgoing paths from "Sao Paulo".

Example 2:
Input: paths = [["B", "C"], ["D", "B"], ["C", "A"]]
Output: "A"
Explanation: Starting at "D" -> "B" -> "C" -> "A", there are no more outgoing paths from "A".

Example 3:
Input: paths = [["A", "Z"]]
Output: "Z"

Constraints:
- 1 <= paths.length <= 100
- paths[i].length == 2
- 1 <= cityA.length, cityB.length <= 10
- cityA != cityB
- All strings consist of lowercase and uppercase English letters and are guaranteed to be unique.
"""

# Clean and Correct Python Solution
def destCity(paths):
    """
    Finds the destination city from the given paths.

    :param paths: List[List[str]] - List of paths where each path is [cityA, cityB]
    :return: str - The destination city
    """
    outgoing_cities = set(cityA for cityA, cityB in paths)
    for cityA, cityB in paths:
        if cityB not in outgoing_cities:
            return cityB

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    paths1 = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
    print(destCity(paths1))  # Output: "Sao Paulo"

    # Test Case 2
    paths2 = [["B", "C"], ["D", "B"], ["C", "A"]]
    print(destCity(paths2))  # Output: "A"

    # Test Case 3
    paths3 = [["A", "Z"]]
    print(destCity(paths3))  # Output: "Z"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the set of outgoing cities takes O(n), where n is the number of paths.
- Iterating through the paths to find the destination city takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The set `outgoing_cities` stores all cities with outgoing paths, which takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Hash Table
"""