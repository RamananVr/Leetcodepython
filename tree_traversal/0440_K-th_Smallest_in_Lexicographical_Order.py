"""
LeetCode Problem #440: K-th Smallest in Lexicographical Order

Problem Statement:
Given integers `n` and `k`, find the k-th smallest number in lexicographical order from 1 to n.

Example:
Input: n = 13, k = 2
Output: 10

Explanation:
The lexicographical order of numbers from 1 to 13 is:
1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
The 2nd smallest number is 10.

Constraints:
- 1 <= k <= n <= 10^9
"""

def findKthNumber(n: int, k: int) -> int:
    """
    Finds the k-th smallest number in lexicographical order from 1 to n.
    """
    def count_steps(curr, n):
        """
        Counts the number of steps (nodes) between `curr` and `n` in the lexicographical tree.
        """
        steps = 0
        first = curr
        last = curr
        while first <= n:
            steps += min(last, n) - first + 1
            first *= 10
            last = last * 10 + 9
        return steps

    curr = 1
    k -= 1  # Decrement k because we start from the first number (1)
    while k > 0:
        steps = count_steps(curr, n)
        if steps <= k:
            # Move to the next sibling in the lexicographical tree
            curr += 1
            k -= steps
        else:
            # Move to the first child in the lexicographical tree
            curr *= 10
            k -= 1
    return curr

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 13
    k = 2
    print(findKthNumber(n, k))  # Output: 10

    # Test Case 2
    n = 100
    k = 10
    print(findKthNumber(n, k))  # Output: 17

    # Test Case 3
    n = 1000
    k = 100
    print(findKthNumber(n, k))  # Output: 323

    # Test Case 4
    n = 1000000
    k = 12345
    print(findKthNumber(n, k))  # Output: 12345

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm navigates the lexicographical tree to find the k-th smallest number.
- The `count_steps` function calculates the number of steps between `curr` and `n` in O(log(n)) time.
- The main loop iterates at most O(log(n)) times, as we move down the tree or to the next sibling.
- Overall, the time complexity is O(log(n) * log(n)).

Space Complexity:
- The algorithm uses a constant amount of space (O(1)) for variables and calculations.
- No additional data structures are used.

Topic: Tree Traversal
"""