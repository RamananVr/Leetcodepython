"""
LeetCode Problem #2772: Apply Operations to Make All Array Elements Equal to Zero

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `k`. You can perform the following operation any number of times:
- Choose an index `i` such that `0 <= i < len(nums) - k`.
- Add `nums[i]` to `nums[i + k]`, and then set `nums[i]` to `0`.

Return `True` if you can make all the elements of the array equal to `0`, or `False` otherwise.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 1 <= k < nums.length
"""

def checkArray(nums, k):
    """
    Determines if it is possible to make all elements of the array equal to zero
    by performing the given operation any number of times.

    :param nums: List[int] - The input array of integers.
    :param k: int - The step size for the operation.
    :return: bool - True if all elements can be made zero, False otherwise.
    """
    n = len(nums)
    current_addition = 0
    diff = [0] * n  # Difference array to track the effect of operations.

    for i in range(n):
        # Apply the current addition to the current element.
        current_addition += diff[i]
        nums[i] += current_addition

        # If nums[i] is not zero, we need to perform an operation.
        if nums[i] != 0:
            if i + k > n:  # If we can't perform the operation, return False.
                return False
            # Calculate the amount to zero out nums[i].
            operation = -nums[i]
            nums[i] += operation
            current_addition += operation
            if i + k < n:
                diff[i + k] -= operation

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 2, 3, 1, 1, 0]
    k1 = 3
    print(checkArray(nums1, k1))  # Expected Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 2
    print(checkArray(nums2, k2))  # Expected Output: False

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    k3 = 1
    print(checkArray(nums3, k3))  # Expected Output: True

    # Test Case 4
    nums4 = [10, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    k4 = 5
    print(checkArray(nums4, k4))  # Expected Output: False

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Thus, the time complexity is O(n), where n is the length of the array.

Space Complexity Analysis:
- The algorithm uses an auxiliary difference array of size n.
- Thus, the space complexity is O(n).

Topic: Arrays, Greedy
"""