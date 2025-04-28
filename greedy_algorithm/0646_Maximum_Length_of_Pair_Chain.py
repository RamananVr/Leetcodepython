"""
LeetCode Problem #646: Maximum Length of Pair Chain

Problem Statement:
You are given an array of `n` pairs `pairs` where `pairs[i] = [a, b]` and `a < b`. A pair `[c, d]` can follow another pair `[a, b]` if and only if `b < c`. A chain of pairs can be formed in this fashion.

Return the length of the longest chain which can be formed.

Example 1:
Input: pairs = [[1,2],[2,3],[3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4].

Example 2:
Input: pairs = [[1,2],[7,8],[4,5]]
Output: 3
Explanation: The longest chain is [1,2] -> [4,5] -> [7,8].

Constraints:
- `n == pairs.length`
- `1 <= n <= 1000`
- `-1000 <= a < b <= 1000`
"""

# Solution
def findLongestChain(pairs):
    """
    Finds the length of the longest chain of pairs.

    :param pairs: List[List[int]] - List of pairs where each pair is [a, b] and a < b
    :return: int - Length of the longest chain
    """
    # Sort pairs by the second element of each pair
    pairs.sort(key=lambda x: x[1])
    
    # Initialize variables
    current_end = float('-inf')  # Tracks the end of the current chain
    chain_length = 0  # Tracks the length of the chain
    
    # Iterate through the sorted pairs
    for pair in pairs:
        if pair[0] > current_end:  # If the current pair can be added to the chain
            chain_length += 1
            current_end = pair[1]  # Update the end of the chain
    
    return chain_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pairs1 = [[1, 2], [2, 3], [3, 4]]
    print(findLongestChain(pairs1))  # Output: 2

    # Test Case 2
    pairs2 = [[1, 2], [7, 8], [4, 5]]
    print(findLongestChain(pairs2))  # Output: 3

    # Test Case 3
    pairs3 = [[1, 10], [2, 3], [4, 5], [6, 7], [8, 9]]
    print(findLongestChain(pairs3))  # Output: 4

    # Test Case 4
    pairs4 = [[-6, -3], [-2, 0], [1, 2], [3, 4], [5, 6]]
    print(findLongestChain(pairs4))  # Output: 5

    # Test Case 5
    pairs5 = [[1, 2]]
    print(findLongestChain(pairs5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the pairs takes O(n log n), where n is the number of pairs.
- Iterating through the pairs takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation may require O(n) additional space depending on the sorting algorithm.
- Other than that, we use a constant amount of space for variables.
- Overall space complexity: O(1) (excluding input storage).
"""

# Topic: Greedy Algorithm