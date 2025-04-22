"""
LeetCode Problem #274: H-Index

Problem Statement:
Given an array of integers `citations` where `citations[i]` is the number of citations a researcher received for their ith paper, 
return the researcher's h-index.

According to the definition of h-index on Wikipedia: A scientist has an index h if h of their n papers have at least h citations each, 
and the other n − h papers have no more than h citations each.

If there are several possible values for h, the maximum one is taken as the h-index.

Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively. 
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.

Example 2:
Input: citations = [1,3,1]
Output: 1

Constraints:
- n == citations.length
- 1 <= n <= 5000
- 0 <= citations[i] <= 1000
"""

def hIndex(citations):
    """
    Calculate the h-index of a researcher based on their citation counts.

    :param citations: List[int] - A list of integers representing citation counts for each paper.
    :return: int - The h-index of the researcher.
    """
    # Sort the citations in descending order
    citations.sort(reverse=True)
    
    # Iterate through the sorted list and find the h-index
    h = 0
    for i, citation in enumerate(citations):
        if citation >= i + 1:
            h = i + 1
        else:
            break
    return h

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    citations1 = [3, 0, 6, 1, 5]
    print(f"Test Case 1: {hIndex(citations1)}")  # Expected Output: 3

    # Test Case 2
    citations2 = [1, 3, 1]
    print(f"Test Case 2: {hIndex(citations2)}")  # Expected Output: 1

    # Test Case 3
    citations3 = [0, 0, 0]
    print(f"Test Case 3: {hIndex(citations3)}")  # Expected Output: 0

    # Test Case 4
    citations4 = [10, 8, 5, 4, 3]
    print(f"Test Case 4: {hIndex(citations4)}")  # Expected Output: 4

    # Test Case 5
    citations5 = [25, 8, 5, 3, 3]
    print(f"Test Case 5: {hIndex(citations5)}")  # Expected Output: 3

"""
Time Complexity Analysis:
- Sorting the citations array takes O(n log n), where n is the length of the array.
- Iterating through the sorted array takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring the space used by the sorting algorithm).

Topic: Arrays
"""