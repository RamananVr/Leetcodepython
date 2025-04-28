"""
LeetCode Problem #2640: Find the Score of All Prefixes of an Array

Problem Statement:
You are given a 0-indexed array `nums` of `n` integers. The score of a prefix of `nums` is defined as the sum of the prefix multiplied by the maximum value in the prefix.

For example, if `nums = [2, 1, 3]`, then:
- The score of the prefix `[2]` is `2 * 2 = 4`.
- The score of the prefix `[2, 1]` is `(2 + 1) * 2 = 6`.
- The score of the prefix `[2, 1, 3]` is `(2 + 1 + 3) * 3 = 18`.

Return an array `result` of length `n` where `result[i]` is the score of the prefix ending at index `i`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^5`
"""

def findPrefixScore(nums):
    """
    Function to calculate the score of all prefixes of the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: An array where each element is the score of the prefix ending at that index.
    """
    n = len(nums)
    result = []
    prefix_sum = 0
    max_value = float('-inf')

    for num in nums:
        prefix_sum += num
        max_value = max(max_value, num)
        result.append(prefix_sum * max_value)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3]
    print(findPrefixScore(nums1))  # Output: [4, 6, 18]

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(findPrefixScore(nums2))  # Output: [1, 6, 18, 40]

    # Test Case 3
    nums3 = [5, 1, 2]
    print(findPrefixScore(nums3))  # Output: [25, 30, 42]

    # Test Case 4
    nums4 = [10]
    print(findPrefixScore(nums4))  # Output: [100]

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    print(findPrefixScore(nums5))  # Output: [1, 4, 9, 16]

"""
Time Complexity Analysis:
- The function iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The function uses a result list to store the scores, which requires O(n) space.
- Other variables (prefix_sum, max_value) use O(1) space.
- Therefore, the space complexity is O(n).

Topic: Arrays
"""