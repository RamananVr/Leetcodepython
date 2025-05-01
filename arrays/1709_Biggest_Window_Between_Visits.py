"""
LeetCode Problem #1709: "Biggest Window Between Visits"

Problem Statement:
You are given an array `visits` where `visits[i]` represents the timestamp of the i-th visit to a website. 
Your task is to find the maximum difference between any two consecutive visits in the array. 
If there are fewer than two visits, return 0.

Constraints:
- 1 <= len(visits) <= 10^5
- 1 <= visits[i] <= 10^9
- The timestamps in `visits` are not necessarily sorted.

Example:
Input: visits = [1, 3, 7, 2, 8]
Output: 5
Explanation: The maximum difference is between 3 and 8.

Input: visits = [10]
Output: 0
Explanation: There is only one visit, so the result is 0.
"""

# Solution
def max_difference_between_visits(visits):
    """
    Finds the maximum difference between any two consecutive visits in the array.

    :param visits: List[int] - List of timestamps of visits.
    :return: int - Maximum difference between consecutive visits.
    """
    if len(visits) < 2:
        return 0

    # Sort the visits to calculate consecutive differences
    visits.sort()

    # Calculate the maximum difference between consecutive visits
    max_diff = 0
    for i in range(1, len(visits)):
        max_diff = max(max_diff, visits[i] - visits[i - 1])

    return max_diff


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    visits = [1, 3, 7, 2, 8]
    print(max_difference_between_visits(visits))  # Output: 5

    # Test Case 2
    visits = [10]
    print(max_difference_between_visits(visits))  # Output: 0

    # Test Case 3
    visits = [5, 5, 5, 5]
    print(max_difference_between_visits(visits))  # Output: 0

    # Test Case 4
    visits = [100, 200, 300, 400]
    print(max_difference_between_visits(visits))  # Output: 100

    # Test Case 5
    visits = [10, 1, 100, 50]
    print(max_difference_between_visits(visits))  # Output: 50


"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the `visits` array.
- Calculating the maximum difference in a single pass takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting the array may require O(n) additional space depending on the sorting algorithm used.
- No additional data structures are used, so the space complexity is O(n).

Topic: Arrays
"""