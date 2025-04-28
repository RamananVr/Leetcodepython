"""
LeetCode Problem #2818: Apply Operations to Maximize Score

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `k`. You have to perform the following operation exactly `k` times:

1. Select any element from `nums`.
2. Remove the selected element from the array.
3. Add the square of the selected element to your score.

Return the maximum possible score you can achieve after performing the operation exactly `k` times.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
- 1 <= k <= nums.length
"""

# Solution
import heapq

def maximizeScore(nums, k):
    """
    Function to maximize the score by selecting k elements from nums.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The number of operations to perform.
    
    Returns:
    int: The maximum possible score.
    """
    # Use a max-heap to always pick the largest element
    max_heap = [-num for num in nums]  # Negate to simulate max-heap using Python's min-heap
    heapq.heapify(max_heap)
    
    score = 0
    for _ in range(k):
        # Extract the largest element
        largest = -heapq.heappop(max_heap)
        # Add its square to the score
        score += largest ** 2
    
    return score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(maximizeScore(nums1, k1))  # Expected Output: 41 (5^2 + 4^2)

    # Test Case 2
    nums2 = [10, 20, 30]
    k2 = 1
    print(maximizeScore(nums2, k2))  # Expected Output: 900 (30^2)

    # Test Case 3
    nums3 = [7, 7, 7, 7]
    k3 = 3
    print(maximizeScore(nums3, k3))  # Expected Output: 147 (7^2 + 7^2 + 7^2)

    # Test Case 4
    nums4 = [1]
    k4 = 1
    print(maximizeScore(nums4, k4))  # Expected Output: 1 (1^2)

    # Test Case 5
    nums5 = [3, 1, 4, 1, 5, 9]
    k5 = 3
    print(maximizeScore(nums5, k5))  # Expected Output: 122 (9^2 + 5^2 + 4^2)

"""
Time Complexity Analysis:
- Building the heap takes O(n), where n is the length of nums.
- Extracting the largest element and adding its square to the score is done k times, each operation taking O(log n).
- Overall time complexity: O(n + k log n).

Space Complexity Analysis:
- The heap requires O(n) space to store the elements.
- Overall space complexity: O(n).

Topic: Arrays, Heap (Priority Queue)
"""