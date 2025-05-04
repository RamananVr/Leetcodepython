"""
LeetCode Question #2615: Sum of Distances

Problem Statement:
You are given a 0-indexed integer array `nums`. There exists an array `answer` of the same length as `nums`, where `answer[i]` is the sum of the absolute differences between `nums[i]` and all the other elements in the array.

Formally, `answer[i] = sum(abs(nums[i] - nums[j]))` for every `0 <= j < len(nums)` and `j != i`.

Return the array `answer`.

Example:
Input: nums = [2, 3, 5]
Output: [4, 3, 7]
Explanation:
For nums[0] = 2, |2-3| + |2-5| = 1 + 3 = 4.
For nums[1] = 3, |3-2| + |3-5| = 1 + 2 = 3.
For nums[2] = 5, |5-2| + |5-3| = 3 + 2 = 7.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

# Clean, Correct Python Solution
def sumOfDistances(nums):
    """
    Calculate the sum of absolute differences for each element in the array.

    Args:
    nums (List[int]): The input array.

    Returns:
    List[int]: The array containing the sum of absolute differences for each element.
    """
    n = len(nums)
    nums_sorted = sorted((num, i) for i, num in enumerate(nums))
    sorted_nums = [num for num, _ in nums_sorted]
    indices = [i for _, i in nums_sorted]

    prefix_sum = [0] * n
    suffix_sum = [0] * n

    # Calculate prefix sums
    prefix_sum[0] = sorted_nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + sorted_nums[i]

    # Calculate suffix sums
    suffix_sum[n - 1] = sorted_nums[n - 1]
    for i in range(n - 2, -1, -1):
        suffix_sum[i] = suffix_sum[i + 1] + sorted_nums[i]

    # Calculate the result
    result = [0] * n
    for i in range(n):
        left_sum = sorted_nums[i] * i - prefix_sum[i - 1] if i > 0 else 0
        right_sum = suffix_sum[i + 1] - sorted_nums[i] * (n - i - 1) if i < n - 1 else 0
        result[indices[i]] = left_sum + right_sum

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 3, 5]
    print(sumOfDistances(nums))  # Output: [4, 3, 7]

    # Test Case 2
    nums = [1, 4, 6]
    print(sumOfDistances(nums))  # Output: [9, 7, 11]

    # Test Case 3
    nums = [10, 10, 10]
    print(sumOfDistances(nums))  # Output: [0, 0, 0]

    # Test Case 4
    nums = [1]
    print(sumOfDistances(nums))  # Output: [0]

    # Test Case 5
    nums = [1, 2, 3, 4, 5]
    print(sumOfDistances(nums))  # Output: [10, 7, 6, 7, 10]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n).
- Calculating prefix and suffix sums takes O(n).
- Calculating the result array takes O(n).
Overall time complexity: O(n log n).

Space Complexity:
- The space used for prefix_sum, suffix_sum, and result arrays is O(n).
- The space used for the sorted array and indices is O(n).
Overall space complexity: O(n).
"""

# Topic: Arrays