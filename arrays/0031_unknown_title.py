"""
LeetCode Problem #31: Next Permutation

Problem Statement:
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

- The next permutation of an array of integers is the next lexicographically greater permutation of its integer. 
- More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
  then the next permutation of that array is the permutation that follows it in the sorted order. 
- If such an arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

- For example, the next permutation of `arr = [1,2,3]` is `[1,3,2]`.
- Similarly, the next permutation of `arr = [2,3,1]` is `[3,1,2]`.
- While the next permutation of `arr = [3,2,1]` is `[1,2,3]` because it is the lowest possible order.

All integers in the array are unique.

Given an array of integers `nums`, find the next permutation of `nums`.

The replacement must be in place and use only constant extra memory.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 100
"""

def nextPermutation(nums):
    """
    Rearranges numbers into the lexicographically next greater permutation of numbers.
    If such an arrangement is not possible, it rearranges it as the lowest possible order (ascending order).
    This function modifies the input list in-place.

    :param nums: List[int] - The input list of integers
    :return: None
    """
    n = len(nums)
    # Step 1: Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:  # If such an element exists
        # Step 2: Find the next larger element to nums[i] from the right
        j = n - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Step 3: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Step 4: Reverse the elements to the right of i
    nums[i + 1:] = reversed(nums[i + 1:])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nextPermutation(nums1)
    print(nums1)  # Output: [1, 3, 2]

    # Test Case 2
    nums2 = [3, 2, 1]
    nextPermutation(nums2)
    print(nums2)  # Output: [1, 2, 3]

    # Test Case 3
    nums3 = [1, 1, 5]
    nextPermutation(nums3)
    print(nums3)  # Output: [1, 5, 1]

    # Test Case 4
    nums4 = [1, 3, 2]
    nextPermutation(nums4)
    print(nums4)  # Output: [2, 1, 3]

    # Test Case 5
    nums5 = [2, 3, 1]
    nextPermutation(nums5)
    print(nums5)  # Output: [3, 1, 2]

"""
Time Complexity Analysis:
- Step 1: Finding the first decreasing element takes O(n) time.
- Step 2: Finding the next larger element takes O(n) time in the worst case.
- Step 3: Swapping two elements takes O(1) time.
- Step 4: Reversing the subarray takes O(n) time in the worst case.
Overall, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm modifies the input list in place and uses only a constant amount of extra space.
Thus, the space complexity is O(1).

Topic: Arrays
"""