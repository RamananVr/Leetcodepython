"""
LeetCode Problem #1282: Group the People Given the Group Size They Belong To

Problem Statement:
There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is assigned to.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person must be in exactly one group, and every person in a group must have the same group size.

If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the input.

Example:
Input: groupSizes = [3,3,3,3,3,1,3]
Output: [[5],[0,1,2],[3,4,6]]

Constraints:
- groupSizes.length == n
- 1 <= n <= 500
- 1 <= groupSizes[i] <= n
"""

# Solution
def groupThePeople(groupSizes):
    """
    Groups people based on their group sizes.

    Args:
    groupSizes (List[int]): List where groupSizes[i] is the size of the group person i belongs to.

    Returns:
    List[List[int]]: A list of groups where each group contains people with the same group size.
    """
    from collections import defaultdict

    # Dictionary to store people by group size
    size_to_people = defaultdict(list)
    result = []

    # Group people by their group size
    for person, size in enumerate(groupSizes):
        size_to_people[size].append(person)
        # Once we have enough people for a group, add it to the result
        if len(size_to_people[size]) == size:
            result.append(size_to_people[size])
            size_to_people[size] = []  # Reset the list for this group size

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    groupSizes = [3, 3, 3, 3, 3, 1, 3]
    print(groupThePeople(groupSizes))  # Output: [[5], [0, 1, 2], [3, 4, 6]]

    # Test Case 2
    groupSizes = [2, 1, 3, 3, 3, 2]
    print(groupThePeople(groupSizes))  # Output: [[1], [0, 5], [2, 3, 4]]

    # Test Case 3
    groupSizes = [1, 1, 1, 1]
    print(groupThePeople(groupSizes))  # Output: [[0], [1], [2], [3]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the groupSizes array once, which takes O(n) time.
- Appending groups to the result and resetting the list for a group size are constant-time operations.
- Overall, the time complexity is O(n).

Space Complexity:
- The size_to_people dictionary stores at most n elements (one for each person), so its space complexity is O(n).
- The result list also stores all the groups, which collectively contain n elements, so its space complexity is O(n).
- Overall, the space complexity is O(n).
"""

# Topic: Arrays