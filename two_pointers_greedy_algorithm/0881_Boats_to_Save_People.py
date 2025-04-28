"""
LeetCode Problem #881: Boats to Save People

Problem Statement:
You are given an array `people` where `people[i]` is the weight of the i-th person, and an integer `limit` which represents the maximum weight a boat can carry. Each boat can carry at most two people at the same time, provided the sum of their weights is at most `limit`.

Return the minimum number of boats required to carry every given person.

Example 1:
Input: people = [1, 2], limit = 3
Output: 1
Explanation: 1 boat (1, 2)

Example 2:
Input: people = [3, 2, 2, 1], limit = 3
Output: 3
Explanation: 3 boats (1, 2), (2), (3)

Example 3:
Input: people = [3, 5, 3, 4], limit = 5
Output: 4
Explanation: 4 boats (3), (3), (4), (5)

Constraints:
- 1 <= people.length <= 5 * 10^4
- 1 <= people[i] <= limit <= 3 * 10^4
"""

# Clean and Correct Python Solution
def numRescueBoats(people, limit):
    """
    Calculate the minimum number of boats required to save all people.

    :param people: List[int] - List of weights of people
    :param limit: int - Maximum weight a boat can carry
    :return: int - Minimum number of boats required
    """
    # Sort the weights of people
    people.sort()
    
    # Initialize two pointers
    left, right = 0, len(people) - 1
    boats = 0

    # Use a two-pointer approach
    while left <= right:
        # If the lightest and heaviest person can share a boat
        if people[left] + people[right] <= limit:
            left += 1  # Move the left pointer to the next lightest person
        # Always move the right pointer (heaviest person gets on a boat)
        right -= 1
        # Increment the boat count
        boats += 1

    return boats

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    people = [1, 2]
    limit = 3
    print(numRescueBoats(people, limit))  # Output: 1

    # Test Case 2
    people = [3, 2, 2, 1]
    limit = 3
    print(numRescueBoats(people, limit))  # Output: 3

    # Test Case 3
    people = [3, 5, 3, 4]
    limit = 5
    print(numRescueBoats(people, limit))  # Output: 4

    # Test Case 4
    people = [5, 1, 4, 2]
    limit = 6
    print(numRescueBoats(people, limit))  # Output: 2

    # Test Case 5
    people = [3, 2, 2, 1, 1]
    limit = 3
    print(numRescueBoats(people, limit))  # Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the number of people.
- The two-pointer traversal takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring input storage).
- Overall space complexity: O(1).
"""

# Topic: Two Pointers, Greedy Algorithm