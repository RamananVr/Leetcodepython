"""
LeetCode Question #2233: Maximum Product After K Increments

Problem Statement:
You are given an array of non-negative integers `nums` and an integer `k`. In one operation, you can choose any element of the array and increment it by 1.

Return the maximum product of `nums` after at most `k` operations. Since the answer may be large, return it modulo 10^9 + 7.

Example 1:
Input: nums = [0,4], k = 5
Output: 20
Explanation: Increment the first number 5 times. Now nums = [5,4], with a product of 5 * 4 = 20.

Example 2:
Input: nums = [6,3,3,2], k = 2
Output: 216
Explanation: Increment the two smallest numbers once. Now nums = [6,4,4,2], with a product of 6 * 4 * 4 * 2 = 216.

Constraints:
- 1 <= nums.length, k <= 10^5
- 0 <= nums[i] <= 10^6
"""

from heapq import heapify, heappush, heappop

def maximumProduct(nums, k):
    """
    Function to calculate the maximum product of nums after at most k increments.
    """
    MOD = 10**9 + 7

    # Convert nums into a min-heap
    heapify(nums)

    # Increment the smallest element k times
    for _ in range(k):
        smallest = heappop(nums)
        heappush(nums, smallest + 1)

    # Calculate the product of all elements in the heap
    product = 1
    for num in nums:
        product = (product * num) % MOD

    return product

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 4]
    k1 = 5
    print("Test Case 1 Output:", maximumProduct(nums1, k1))  # Expected Output: 20

    # Test Case 2
    nums2 = [6, 3, 3, 2]
    k2 = 2
    print("Test Case 2 Output:", maximumProduct(nums2, k2))  # Expected Output: 216

    # Test Case 3
    nums3 = [1, 1, 1]
    k3 = 3
    print("Test Case 3 Output:", maximumProduct(nums3, k3))  # Expected Output: 8

    # Test Case 4
    nums4 = [10, 10, 10]
    k4 = 5
    print("Test Case 4 Output:", maximumProduct(nums4, k4))  # Expected Output: 1331000

"""
Time Complexity Analysis:
1. Converting the array into a heap takes O(n), where n is the length of nums.
2. Each of the k operations involves a heappop and heappush, each of which takes O(log n). Thus, the total cost for k operations is O(k log n).
3. Calculating the product of the elements in the heap takes O(n).

Overall Time Complexity: O(n + k log n)

Space Complexity Analysis:
1. The heap data structure requires O(n) space to store the elements of nums.
2. No additional significant space is used.

Overall Space Complexity: O(n)

Topic: Heap (Priority Queue)
"""