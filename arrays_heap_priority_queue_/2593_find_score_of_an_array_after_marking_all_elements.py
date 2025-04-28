"""
LeetCode Question #2593: Find Score of an Array After Marking All Elements

Problem Statement:
You are given an array `nums` consisting of positive integers.

Initially, your score is 0. You can perform the following operation until the array becomes empty:
1. Pick the smallest integer of the array and add it to your score.
2. Remove the picked integer and its adjacent integers from the array.

Return the score you can achieve after performing the above operation.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

# Python Solution
from heapq import heappop, heappush

def findScore(nums):
    """
    Function to calculate the score of the array after marking all elements.

    Args:
    nums (List[int]): List of positive integers.

    Returns:
    int: The maximum score achievable.
    """
    n = len(nums)
    marked = [False] * n  # To track marked elements
    heap = []  # Min-heap to store (value, index) pairs
    score = 0

    # Push all elements into the heap
    for i, num in enumerate(nums):
        heappush(heap, (num, i))

    # Process the heap
    while heap:
        value, index = heappop(heap)
        # Skip if the element is already marked
        if marked[index]:
            continue
        # Add the value to the score
        score += value
        # Mark the current element and its adjacent elements
        marked[index] = True
        if index > 0:
            marked[index - 1] = True
        if index < n - 1:
            marked[index + 1] = True

    return score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3, 4, 5, 6]
    print(findScore(nums1))  # Expected Output: 12

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(findScore(nums2))  # Expected Output: 9

    # Test Case 3
    nums3 = [10, 20, 30, 40, 50]
    print(findScore(nums3))  # Expected Output: 90

    # Test Case 4
    nums4 = [1]
    print(findScore(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [5, 5, 5, 5, 5]
    print(findScore(nums5))  # Expected Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the heap takes O(n), where n is the length of the array.
- Each heap operation (push and pop) takes O(log n).
- In the worst case, we process all elements, resulting in O(n log n) complexity.

Space Complexity:
- The `marked` array takes O(n) space.
- The heap also takes O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Arrays, Heap (Priority Queue)
"""