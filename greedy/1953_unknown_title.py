"""
LeetCode Problem #1953: Maximum Number of Weeks for Which You Can Work

Problem Statement:
You are given an integer array milestones where each element represents the number of milestones in a project. 
The goal is to maximize the number of weeks you can work on the projects without working on two milestones 
from the same project consecutively.

In one week, you can work on one milestone from any project. You must work on a milestone every week unless 
there are no milestones left to work on.

Return the maximum number of weeks you can work on the projects.

Constraints:
- 1 <= milestones.length <= 10^5
- 1 <= milestones[i] <= 10^9
"""

# Solution
def numberOfWeeks(milestones):
    """
    Calculate the maximum number of weeks you can work on the projects.

    :param milestones: List[int] - List of milestones for each project
    :return: int - Maximum number of weeks you can work
    """
    total_milestones = sum(milestones)
    max_milestones = max(milestones)
    
    # If the largest project can be balanced with the rest
    if max_milestones <= total_milestones - max_milestones:
        return total_milestones
    else:
        # Otherwise, we can only work for 2 * (total_milestones - max_milestones) + 1 weeks
        return 2 * (total_milestones - max_milestones) + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    milestones = [1, 2, 3]
    print(numberOfWeeks(milestones))  # Output: 6

    # Test Case 2
    milestones = [5, 2, 1]
    print(numberOfWeeks(milestones))  # Output: 7

    # Test Case 3
    milestones = [9, 3, 3]
    print(numberOfWeeks(milestones))  # Output: 15

    # Test Case 4
    milestones = [10]
    print(numberOfWeeks(milestones))  # Output: 1

    # Test Case 5
    milestones = [7, 7, 7]
    print(numberOfWeeks(milestones))  # Output: 21

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the sum of milestones takes O(n), where n is the length of the milestones array.
- Finding the maximum milestone also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space (variables `total_milestones` and `max_milestones`).
- Therefore, the space complexity is O(1).

Topic: Greedy
"""