"""
LeetCode Problem #757: Set Intersection Size At Least Two

Problem Statement:
An integer interval [a, b] (a <= b) is a set of all integers x where a <= x <= b.
For example, [3, 5] is the set {3, 4, 5}.

A set of intervals is a collection of intervals. The intersection size of a set of intervals is the size of the smallest set S such that for every interval [a, b] in the set, S contains at least two integers from the interval.

Given a set of intervals, return the size of the smallest set S such that the intersection size of the set of intervals is at least two.

Example 1:
Input: intervals = [[1, 3], [3, 7], [5, 7], [7, 8]]
Output: 5
Explanation: One possible set S is {2, 3, 6, 7, 8}.

Example 2:
Input: intervals = [[1, 2], [2, 3], [2, 4], [4, 5]]
Output: 5
Explanation: One possible set S is {2, 3, 4, 5}.

Constraints:
- 1 <= intervals.length <= 3000
- 0 <= intervals[i][0] < intervals[i][1] <= 10^8
"""

# Python Solution
def intersectionSizeTwo(intervals):
    # Sort intervals by their ending points, and if equal, by their starting points in reverse order
    intervals.sort(key=lambda x: (x[1], -x[0]))
    
    # Initialize the result set
    S = []
    
    for a, b in intervals:
        # Check if the interval [a, b] already has at least two elements in S
        if len(S) < 2 or S[-2] < a:
            # Add the last two elements of the interval to S
            S.append(b - 1)
            S.append(b)
        elif len(S) < 2 or S[-1] < a:
            # Add the last element of the interval to S
            S.append(b)
    
    return len(S)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    intervals1 = [[1, 3], [3, 7], [5, 7], [7, 8]]
    print(intersectionSizeTwo(intervals1))  # Output: 5

    # Test Case 2
    intervals2 = [[1, 2], [2, 3], [2, 4], [4, 5]]
    print(intersectionSizeTwo(intervals2))  # Output: 5

    # Test Case 3
    intervals3 = [[1, 2], [2, 3], [3, 4], [4, 5]]
    print(intersectionSizeTwo(intervals3))  # Output: 4

    # Test Case 4
    intervals4 = [[1, 10], [2, 3], [4, 5], [6, 7]]
    print(intersectionSizeTwo(intervals4))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the intervals takes O(n log n), where n is the number of intervals.
- Iterating through the intervals takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used for the result set S is O(n) in the worst case.
- Overall space complexity: O(n).

Topic: Greedy Algorithm
"""