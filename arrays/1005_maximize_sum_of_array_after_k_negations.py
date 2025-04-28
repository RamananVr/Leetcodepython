"""
LeetCode Question #1005: Maximize Sum Of Array After K Negations

Problem Statement:
Given an integer array `nums` and an integer `k`, you must perform `k` operations on the array. 
In one operation, you can choose any element of the array and flip its sign (i.e., change the sign of the element).
Return the largest possible sum of the array after performing exactly `k` operations.

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- 1 <= k <= 10^4
"""

# Solution
def largestSumAfterKNegations(nums, k):
    """
    Function to maximize the sum of the array after k negations.

    :param nums: List[int] - The input array of integers.
    :param k: int - The number of negations allowed.
    :return: int - The maximum possible sum of the array after k negations.
    """
    # Sort the array to prioritize flipping the smallest (most negative) values
    nums.sort()
    
    # Flip the smallest values (negative ones) k times
    for i in range(len(nums)):
        if k > 0 and nums[i] < 0:
            nums[i] = -nums[i]
            k -= 1
    
    # If k is still positive and odd, flip the smallest value again
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
    print(largestSumAfterKNegations(nums1, k1))  # Expected Output: 5

    # Test Case 2
    nums2 = [3, -1, 0, 2]
    k2 = 3
    print(largestSumAfterKNegations(nums2, k2))  # Expected Output: 6

    # Test Case 3
    nums3 = [2, -3, -1, 5, -4]
    k3 = 2
    print(largestSumAfterKNegations(nums3, k3))  # Expected Output: 13

    # Test Case 4
    nums4 = [-8, -3, -2, 5, 9]
    k4 = 5
    print(largestSumAfterKNegations(nums4, k4))  # Expected Output: 19

    # Test Case 5
    nums5 = [1, 2, 3]
    k5 = 10
    print(largestSumAfterKNegations(nums5, k5))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The loop to flip elements runs in O(n).
- Re-sorting the array (if k is odd) takes O(n log n).
- Overall, the time complexity is O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space, as it modifies the input array in place.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""