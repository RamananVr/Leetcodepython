"""
LeetCode Question #457: Circular Array Loop

Problem Statement:
You are given a circular array nums of positive and negative integers. If a number k at an index is positive, 
then move k steps forward. Conversely, if it's negative, move k steps backward. Since the array is circular, 
you may assume that the last element's next element is the first element, and the first element's previous 
element is the last element.

Determine if there is a loop (or a cycle) in nums. A loop must meet the following conditions:
1. The loop must be entirely within the array (i.e., no jumps outside the bounds of the array).
2. The loop must consist of a single direction (all numbers in the loop are either positive or negative).
3. The loop must have a length of at least 2.

Return true if there is a loop in nums, otherwise return false.

Constraints:
- 1 <= nums.length <= 5000
- -1000 <= nums[i] <= 1000

Example:
Input: nums = [2, -1, 1, 2, 2]
Output: true

Input: nums = [-1, 2]
Output: false

Input: nums = [-2, 1, -1, -2, -2]
Output: false
"""

def circularArrayLoop(nums):
    """
    Determines if there is a circular loop in the array nums.

    :param nums: List[int] - The input array of integers.
    :return: bool - True if there is a valid loop, False otherwise.
    """
    n = len(nums)

    def next_index(i):
        return (i + nums[i]) % n

    for i in range(n):
        if nums[i] == 0:
            continue

        slow, fast = i, next_index(i)
        while nums[fast] * nums[i] > 0 and nums[next_index(fast)] * nums[i] > 0:
            if slow == fast:
                # Check if the loop length is greater than 1
                if slow == next_index(slow):
                    break
                return True
            slow = next_index(slow)
            fast = next_index(next_index(fast))

        # Mark all elements in the current cycle as 0 to avoid revisiting
        marker = i
        while nums[marker] * nums[i] > 0:
            temp = marker
            marker = next_index(marker)
            nums[temp] = 0

    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, -1, 1, 2, 2]
    print(circularArrayLoop(nums1))  # Output: True

    # Test Case 2
    nums2 = [-1, 2]
    print(circularArrayLoop(nums2))  # Output: False

    # Test Case 3
    nums3 = [-2, 1, -1, -2, -2]
    print(circularArrayLoop(nums3))  # Output: False

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print(circularArrayLoop(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, -1, 1, -1, 1]
    print(circularArrayLoop(nums5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, and for each element, it may traverse the cycle formed by the array.
- In the worst case, each element is visited once, resulting in O(n) time complexity.

Space Complexity:
- The algorithm uses a constant amount of extra space for pointers and variables, resulting in O(1) space complexity.

Topic: Arrays, Two Pointers
"""