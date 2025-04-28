"""
LeetCode Problem #2984: Maximize the Sum of an Array After K Negations

Problem Statement:
Given an integer array `nums` and an integer `k`, you can choose any element from the array and flip its sign (i.e., change the element from positive to negative or vice versa). You can perform this operation at most `k` times. Return the maximum possible sum of the array after performing the operation at most `k` times.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4
"""

def maximizeSumAfterKNegations(nums, k):
    """
    Function to maximize the sum of an array after performing at most k negations.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum number of negations allowed.

    Returns:
    int: The maximum possible sum of the array after k negations.
    """
    # Sort the array to prioritize flipping the smallest (most negative) values
    nums.sort()
    
    # Flip the smallest values (negative ones) up to k times
    for i in range(len(nums)):
        if k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
    
    # If k is still greater than 0, flip the smallest value repeatedly
    # (this is equivalent to flipping it an even number of times, which has no effect)
    if k % 2 == 1:
        nums.sort()  # Re-sort the array to find the smallest value
        nums[0] = -nums[0]
    
    # Return the sum of the array
    return sum(nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 3]
    k1 = 1
    print(maximizeSumAfterKNegations(nums1, k1))  # Expected Output: 5

    # Test Case 2
    nums2 = [3, -1, 0, 2]
    k2 = 3
    print(maximizeSumAfterKNegations(nums2, k2))  # Expected Output: 6

    # Test Case 3
    nums3 = [2, -3, -1, 5, -4]
    k3 = 2
    print(maximizeSumAfterKNegations(nums3, k3))  # Expected Output: 13

    # Test Case 4
    nums4 = [-8, -3, -2, 1, 2]
    k4 = 5
    print(maximizeSumAfterKNegations(nums4, k4))  # Expected Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The loop to flip elements runs in O(n).
- Re-sorting the array (if k is odd) takes O(n log n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it modifies the input array in place.
- Overall space complexity: O(1).

Topic: Arrays, Greedy
"""