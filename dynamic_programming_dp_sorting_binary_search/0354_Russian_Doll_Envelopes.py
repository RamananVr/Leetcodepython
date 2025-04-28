"""
LeetCode Problem #354: Russian Doll Envelopes

Problem Statement:
You are given a 2D array of integers `envelopes` where `envelopes[i] = [wi, hi]` represents the width and height of an envelope.
One envelope can fit into another if and only if both the width and height of one envelope are greater than the width and height of the other envelope.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note:
You cannot rotate an envelope.

Example 1:
Input: envelopes = [[5,4],[6,4],[6,7],[2,3]]
Output: 3
Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3] => [5,4] => [6,7]).

Example 2:
Input: envelopes = [[1,1],[1,1],[1,1]]
Output: 1

Constraints:
- 1 <= envelopes.length <= 10^5
- envelopes[i].length == 2
- 1 <= wi, hi <= 10^5
"""

# Solution
from bisect import bisect_left

def maxEnvelopes(envelopes):
    """
    Finds the maximum number of envelopes that can be Russian dolled.

    :param envelopes: List[List[int]] - List of envelopes represented as [width, height].
    :return: int - Maximum number of envelopes that can be Russian dolled.
    """
    # Step 1: Sort envelopes by width in ascending order, and by height in descending order if widths are the same.
    envelopes.sort(key=lambda x: (x[0], -x[1]))
    
    # Step 2: Extract heights and find the Longest Increasing Subsequence (LIS) in heights.
    heights = [envelope[1] for envelope in envelopes]
    lis = []
    
    for height in heights:
        pos = bisect_left(lis, height)
        if pos == len(lis):
            lis.append(height)
        else:
            lis[pos] = height
    
    return len(lis)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    envelopes1 = [[5,4],[6,4],[6,7],[2,3]]
    print(maxEnvelopes(envelopes1))  # Output: 3

    # Test Case 2
    envelopes2 = [[1,1],[1,1],[1,1]]
    print(maxEnvelopes(envelopes2))  # Output: 1

    # Test Case 3
    envelopes3 = [[8,9],[7,8],[6,7],[5,6],[4,5],[3,4],[2,3],[1,2]]
    print(maxEnvelopes(envelopes3))  # Output: 8

    # Test Case 4
    envelopes4 = [[4,5],[4,6],[6,7],[2,3],[1,1]]
    print(maxEnvelopes(envelopes4))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the envelopes takes O(n log n), where n is the number of envelopes.
- Finding the LIS using binary search takes O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `lis` list used to store the heights in the LIS takes O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Dynamic Programming (DP), Sorting, Binary Search