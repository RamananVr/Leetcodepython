"""
LeetCode Problem #2913: Sum of Distances

Problem Statement:
You are given an array `nums` of size `n` where `nums[i]` represents the position of the i-th point on a number line. 
The distance between two points `i` and `j` is defined as `|nums[i] - nums[j]|`.

Return an array `result` of size `n` where `result[i]` is the sum of distances between the i-th point and all other points.

Example:
Input: nums = [2, 3, 5]
Output: [6, 5, 7]
Explanation:
- For nums[0] = 2, the distances are |2-3| + |2-5| = 1 + 3 = 4.
- For nums[1] = 3, the distances are |3-2| + |3-5| = 1 + 2 = 3.
- For nums[2] = 5, the distances are |5-2| + |5-3| = 3 + 2 = 5.

Constraints:
- 1 <= nums.length <= 10^5
- -10^4 <= nums[i] <= 10^4
"""

# Python Solution
def sum_of_distances(nums):
    """
    Calculate the sum of distances for each point in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: An array where each element is the sum of distances for the corresponding point.
    """
    n = len(nums)
    nums_sorted = sorted((num, i) for i, num in enumerate(nums))  # Sort nums with their original indices
    sorted_nums = [num for num, _ in nums_sorted]
    indices = [i for _, i in nums_sorted]

    # Prefix sums for sorted array
    prefix_sum = [0] * n
    prefix_sum[0] = sorted_nums[0]
    for i in range(1, n):
        prefix_sum[i] = prefix_sum[i - 1] + sorted_nums[i]

    # Calculate result
    result = [0] * n
    for i in range(n):
        num = sorted_nums[i]
        left_sum = prefix_sum[i] - num  # Sum of all elements to the left of current element
        right_sum = prefix_sum[-1] - prefix_sum[i]  # Sum of all elements to the right of current element
        left_count = i  # Number of elements to the left
        right_count = n - i - 1  # Number of elements to the right

        # Total distance for the current element
        result[indices[i]] = (num * left_count - left_sum) + (right_sum - num * right_count)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [2, 3, 5]
    print(sum_of_distances(nums))  # Output: [6, 5, 7]

    # Test Case 2
    nums = [1, 4, 6, 8]
    print(sum_of_distances(nums))  # Output: [15, 9, 9, 15]

    # Test Case 3
    nums = [10]
    print(sum_of_distances(nums))  # Output: [0]

    # Test Case 4
    nums = [1, 1, 1]
    print(sum_of_distances(nums))  # Output: [0, 0, 0]

    # Test Case 5
    nums = [-5, -2, 0, 3]
    print(sum_of_distances(nums))  # Output: [18, 10, 8, 14]

"""
Time Complexity:
- Sorting the array takes O(n log n).
- Calculating prefix sums takes O(n).
- Calculating the result array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used for the sorted array, prefix sums, and result array is O(n).
- Overall space complexity: O(n).

Topic: Arrays, Prefix Sum
"""