"""
LeetCode Problem #986: Interval List Intersections

Problem Statement:
You are given two lists of closed intervals, `firstList` and `secondList`, where `firstList[i] = [start_i, end_i]` and `secondList[j] = [start_j, end_j]`. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval `[a, b]` (with `a <= b`) denotes the set of real numbers `x` with `a <= x <= b`.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of `[1, 3]` and `[2, 4]` is `[2, 3]`.

Example 1:
Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

Example 2:
Input: firstList = [[1,3],[5,9]], secondList = []
Output: []

Constraints:
- `0 <= firstList.length, secondList.length <= 1000`
- `firstList[i].length == 2` and `secondList[j].length == 2`
- `0 <= start_i <= end_i <= 10^9`
- `0 <= start_j <= end_j <= 10^9`
- The intervals in `firstList` and `secondList` are disjoint and sorted in ascending order.
"""

# Solution
def intervalIntersection(firstList, secondList):
    """
    Finds the intersection of two lists of intervals.

    Args:
    firstList (List[List[int]]): The first list of intervals.
    secondList (List[List[int]]): The second list of intervals.

    Returns:
    List[List[int]]: A list of intervals representing the intersection of the input lists.
    """
    i, j = 0, 0
    result = []

    while i < len(firstList) and j < len(secondList):
        # Find the intersection between firstList[i] and secondList[j]
        start = max(firstList[i][0], secondList[j][0])
        end = min(firstList[i][1], secondList[j][1])

        # If the intervals overlap, add the intersection to the result
        if start <= end:
            result.append([start, end])

        # Move to the next interval in the list with the smaller endpoint
        if firstList[i][1] < secondList[j][1]:
            i += 1
        else:
            j += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]]
    print(intervalIntersection(firstList, secondList))  # Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

    # Test Case 2
    firstList = [[1,3],[5,9]]
    secondList = []
    print(intervalIntersection(firstList, secondList))  # Output: []

    # Test Case 3
    firstList = [[1,7]]
    secondList = [[3,10]]
    print(intervalIntersection(firstList, secondList))  # Output: [[3,7]]

    # Test Case 4
    firstList = [[1,3],[5,7],[9,12]]
    secondList = [[5,10]]
    print(intervalIntersection(firstList, secondList))  # Output: [[5,7],[9,10]]

# Time and Space Complexity Analysis
"""
Time Complexity:
The algorithm iterates through both lists of intervals, processing each interval once. 
Thus, the time complexity is O(n + m), where n is the length of `firstList` and m is the length of `secondList`.

Space Complexity:
The space complexity is O(k), where k is the number of intersections added to the result list. 
No additional space is used apart from the output list.
"""

# Topic: Arrays