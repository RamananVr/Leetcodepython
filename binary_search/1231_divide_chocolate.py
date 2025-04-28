"""
LeetCode Question #1231: Divide Chocolate

Problem Statement:
You have one chocolate bar that consists of some chunks. Each chunk has its own sweetness given by the array `sweetness`.

You want to share the chocolate with your `k` friends so you start cutting the chocolate bar into `k + 1` pieces using `k` cuts, each piece consisting of some consecutive chunks.

Being generous, you will eat the piece with the minimum total sweetness and give the other pieces to your friends. Find the maximum total sweetness of the piece you can get by cutting the chocolate bar optimally.

Constraints:
- `0 <= k < sweetness.length <= 10^4`
- `1 <= sweetness[i] <= 10^5`

Example:
Input: sweetness = [1,2,3,4,5,6,7,8,9], k = 5
Output: 6
Explanation: You can divide the chocolate into [1,2,3], [4,5], [6], [7], [8], [9] with minimum sweetness 6.

Input: sweetness = [5,6,7,8,9,1,2,3,4], k = 8
Output: 1
Explanation: There are 9 chunks, so you need to make 8 cuts to form 9 pieces. Each piece will have sweetness of 1.

Input: sweetness = [1,2,2,1,2,2,1,2,2], k = 2
Output: 5
Explanation: You can divide the chocolate into [1,2,2], [1,2,2], [1,2,2] with minimum sweetness 5.
"""

# Solution
def maximizeSweetness(sweetness, k):
    def canDivide(mid):
        # Check if we can divide the chocolate into k+1 pieces with at least `mid` sweetness
        current_sum = 0
        pieces = 0
        for s in sweetness:
            current_sum += s
            if current_sum >= mid:
                pieces += 1
                current_sum = 0
        return pieces >= k + 1

    # Binary search for the maximum minimum sweetness
    left, right = 1, sum(sweetness) // (k + 1)
    while left < right:
        mid = (left + right + 1) // 2
        if canDivide(mid):
            left = mid
        else:
            right = mid - 1
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sweetness = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    k = 5
    print(maximizeSweetness(sweetness, k))  # Output: 6

    # Test Case 2
    sweetness = [5, 6, 7, 8, 9, 1, 2, 3, 4]
    k = 8
    print(maximizeSweetness(sweetness, k))  # Output: 1

    # Test Case 3
    sweetness = [1, 2, 2, 1, 2, 2, 1, 2, 2]
    k = 2
    print(maximizeSweetness(sweetness, k))  # Output: 5

    # Test Case 4
    sweetness = [10, 20, 30, 40, 50]
    k = 3
    print(maximizeSweetness(sweetness, k))  # Output: 30

    # Test Case 5
    sweetness = [1, 1, 1, 1, 1, 1, 1, 1, 1]
    k = 4
    print(maximizeSweetness(sweetness, k))  # Output: 2

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The binary search runs in O(log(sum(sweetness) // (k + 1))) iterations.
   - For each iteration, the `canDivide` function is called, which iterates through the `sweetness` array in O(n) time.
   - Therefore, the overall time complexity is O(n * log(sum(sweetness) // (k + 1))).

2. Space Complexity:
   - The algorithm uses O(1) additional space since no extra data structures are used.

Topic: Binary Search
"""