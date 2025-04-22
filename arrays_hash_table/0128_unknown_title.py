"""
LeetCode Problem #128: Longest Consecutive Sequence

Problem Statement:
Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
- 0 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def longestConsecutive(nums):
    """
    Finds the length of the longest consecutive elements sequence in an array.

    :param nums: List[int] - The input array of integers.
    :return: int - The length of the longest consecutive sequence.
    """
    if not nums:
        return 0

    # Convert the list to a set for O(1) lookups
    num_set = set(nums)
    longest_streak = 0

    for num in num_set:
        # Only start counting if `num` is the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_streak = 1

            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            # Update the longest streak
            longest_streak = max(longest_streak, current_streak)

    return longest_streak

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [100, 4, 200, 1, 3, 2]
    print("Test Case 1 Output:", longestConsecutive(nums1))  # Expected Output: 4

    # Test Case 2
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
    print("Test Case 2 Output:", longestConsecutive(nums2))  # Expected Output: 9

    # Test Case 3
    nums3 = []
    print("Test Case 3 Output:", longestConsecutive(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1, 2, 0, 1]
    print("Test Case 4 Output:", longestConsecutive(nums4))  # Expected Output: 3

    # Test Case 5
    nums5 = [10]
    print("Test Case 5 Output:", longestConsecutive(nums5))  # Expected Output: 1

"""
Time Complexity Analysis:
- Converting the list to a set takes O(n).
- The loop iterates over each element in the set, and for each element, the inner while loop runs at most once per element in the sequence.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(n) due to the set used to store the elements of the array.

Topic: Arrays, Hash Table
"""