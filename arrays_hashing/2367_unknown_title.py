"""
LeetCode Problem #2367: Number of Arithmetic Triplets

Problem Statement:
You are given a 0-indexed, strictly increasing integer array `nums` and a positive integer `diff`. 
A triplet `(i, j, k)` is an arithmetic triplet if the following conditions are met:
    - i < j < k
    - nums[j] - nums[i] == diff
    - nums[k] - nums[j] == diff

Return the number of unique arithmetic triplets.

Constraints:
    - 3 <= nums.length <= 200
    - 0 <= nums[i] <= 200
    - 1 <= diff <= 50
    - nums is strictly increasing.
"""

def arithmeticTriplets(nums, diff):
    """
    Function to count the number of arithmetic triplets in the array.

    :param nums: List[int] - A strictly increasing list of integers.
    :param diff: int - The common difference for the arithmetic triplet.
    :return: int - The number of arithmetic triplets.
    """
    num_set = set(nums)
    count = 0

    for num in nums:
        if (num + diff in num_set) and (num + 2 * diff in num_set):
            count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 4, 6, 7, 10]
    diff1 = 3
    print(arithmeticTriplets(nums1, diff1))  # Output: 2

    # Test Case 2
    nums2 = [4, 5, 6, 7, 8, 9]
    diff2 = 2
    print(arithmeticTriplets(nums2, diff2))  # Output: 2

    # Test Case 3
    nums3 = [1, 3, 5, 7, 9]
    diff3 = 2
    print(arithmeticTriplets(nums3, diff3))  # Output: 3

    # Test Case 4
    nums4 = [1, 2, 3, 4]
    diff4 = 1
    print(arithmeticTriplets(nums4, diff4))  # Output: 2

"""
Time Complexity:
    - The function iterates through the `nums` array once, and for each element, it performs O(1) operations 
      to check membership in the set. Thus, the time complexity is O(n), where n is the length of the `nums` array.

Space Complexity:
    - The function uses a set to store the elements of `nums`, which requires O(n) space. 
      Therefore, the space complexity is O(n).

Topic: Arrays, Hashing
"""