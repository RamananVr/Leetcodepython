"""
LeetCode Problem #1877: Minimize Maximum Pair Sum in Array

Problem Statement:
The pair sum of a pair (a,b) is defined as (a + b). 
- The maximum pair sum is the largest pair sum in a list of pairs.
- For example, if we have pairs (1,5), (2,3), and (4,4), the pair sums are 6, 5, and 8. 
  The maximum pair sum is 8.

Given an array `nums` of even length `n`, you need to pair up the elements of `nums` such that:
- Each element of `nums` is in exactly one pair, and
- The maximum pair sum is minimized.

Return the minimized maximum pair sum after optimally pairing up the elements.

Constraints:
- `n == nums.length`
- `2 <= n <= 10^5`
- `n` is even.
- `1 <= nums[i] <= 10^5`
"""

# Solution
def minPairSum(nums):
    """
    Minimize the maximum pair sum in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimized maximum pair sum.
    """
    # Sort the array
    nums.sort()
    
    # Initialize the maximum pair sum
    max_pair_sum = 0
    
    # Use two pointers to pair the smallest and largest elements
    left, right = 0, len(nums) - 1
    while left < right:
        # Calculate the pair sum
        pair_sum = nums[left] + nums[right]
        # Update the maximum pair sum
        max_pair_sum = max(max_pair_sum, pair_sum)
        # Move the pointers
        left += 1
        right -= 1
    
    return max_pair_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 2, 3]
    print(minPairSum(nums1))  # Output: 7

    # Test Case 2
    nums2 = [4, 1, 2, 3]
    print(minPairSum(nums2))  # Output: 6

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(minPairSum(nums3))  # Output: 2

    # Test Case 4
    nums4 = [9, 2, 8, 4, 5, 1]
    print(minPairSum(nums4))  # Output: 10

    # Test Case 5
    nums5 = [1, 2]
    print(minPairSum(nums5))  # Output: 3

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- The two-pointer traversal takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation uses O(1) additional space if done in-place.
- Overall space complexity: O(1).

Topic: Arrays, Two Pointers, Greedy
"""