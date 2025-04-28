"""
LeetCode Problem #1673: Find the Most Competitive Subsequence

Problem Statement:
Given an integer array `nums` and a positive integer `k`, return the most competitive subsequence of `nums` of size `k`.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array. A subsequence is considered competitive if it has the smallest lexicographical order compared to all other subsequences of the same size.

Example:
Input: nums = [3, 5, 2, 6], k = 2
Output: [2, 6]

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^9
1 <= k <= nums.length
"""

# Solution
def mostCompetitive(nums, k):
    """
    Finds the most competitive subsequence of size k from the given array nums.

    :param nums: List[int] - The input array
    :param k: int - The size of the desired subsequence
    :return: List[int] - The most competitive subsequence
    """
    stack = []
    n = len(nums)
    
    for i, num in enumerate(nums):
        # While the stack is not empty, the current number is smaller than the top of the stack,
        # and removing the top of the stack won't prevent us from forming a subsequence of size k
        while stack and num < stack[-1] and len(stack) + (n - i) > k:
            stack.pop()
        
        # Add the current number to the stack if the stack size is less than k
        if len(stack) < k:
            stack.append(num)
    
    return stack

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 2, 6]
    k1 = 2
    print(mostCompetitive(nums1, k1))  # Output: [2, 6]

    # Test Case 2
    nums2 = [2, 4, 3, 3, 5, 4, 9, 6]
    k2 = 4
    print(mostCompetitive(nums2, k2))  # Output: [2, 3, 3, 4]

    # Test Case 3
    nums3 = [1, 3, 1]
    k3 = 2
    print(mostCompetitive(nums3, k3))  # Output: [1, 1]

    # Test Case 4
    nums4 = [6, 7, 8, 1, 2, 3]
    k4 = 3
    print(mostCompetitive(nums4, k4))  # Output: [1, 2, 3]

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm iterates through the array `nums` once, and for each element, it may perform a pop operation on the stack. 
Since each element is pushed and popped from the stack at most once, the total time complexity is O(n), where n is the length of `nums`.

Space Complexity:
The space complexity is O(k), where k is the size of the desired subsequence, as the stack will store at most k elements.

Topic: Arrays, Monotonic Stack
"""