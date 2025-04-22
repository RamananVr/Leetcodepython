"""
LeetCode Question #275: H-Index II

Problem Statement:
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their ith paper, 
and `citations` is sorted in ascending order, return the researcher's h-index.

The h-index is defined as the maximum value `h` such that the researcher has published at least `h` papers that have each been 
cited at least `h` times.

You must write an algorithm that runs in O(log n) time.

Example 1:
Input: citations = [0,1,3,5,6]
Output: 3
Explanation: [0,1,3,5,6] means the researcher has 5 papers in total. 
             The researcher has 3 papers with at least 3 citations each.

Example 2:
Input: citations = [1,2,100]
Output: 2

Constraints:
- `n == citations.length`
- `1 <= n <= 10^5`
- `0 <= citations[i] <= 1000`
- `citations` is sorted in ascending order.
"""

def hIndex(citations):
    """
    Function to calculate the h-index for a sorted list of citations.

    :param citations: List[int] - A sorted list of citations.
    :return: int - The h-index of the researcher.
    """
    n = len(citations)
    left, right = 0, n - 1

    while left <= right:
        mid = (left + right) // 2
        if citations[mid] == n - mid:
            return citations[mid]
        elif citations[mid] < n - mid:
            left = mid + 1
        else:
            right = mid - 1

    return n - left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    citations1 = [0, 1, 3, 5, 6]
    print(hIndex(citations1))  # Output: 3

    # Test Case 2
    citations2 = [1, 2, 100]
    print(hIndex(citations2))  # Output: 2

    # Test Case 3
    citations3 = [0, 0, 0, 0]
    print(hIndex(citations3))  # Output: 0

    # Test Case 4
    citations4 = [0, 1, 2, 3, 4, 5, 6]
    print(hIndex(citations4))  # Output: 3

    # Test Case 5
    citations5 = [10, 20, 30, 40, 50]
    print(hIndex(citations5))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm uses binary search, which operates in O(log n) time. 
Here, `n` is the length of the `citations` array.

Space Complexity:
The algorithm uses constant space, i.e., O(1), as no additional data structures are used.

Topic: Binary Search
"""