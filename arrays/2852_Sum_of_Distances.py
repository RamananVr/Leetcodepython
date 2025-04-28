"""
LeetCode Problem #2852: Sum of Distances

Problem Statement:
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, 
where arr[i] is the sum of |i - j| for all j such that nums[j] == nums[i] and j != i. 
If there is no such j, set arr[i] = 0.

Return the array arr.

Example:
Input: nums = [1, 3, 1, 1, 2]
Output: [5, 0, 3, 4, 0]

Explanation:
- For nums[0] = 1, there are two other indices with value 1: nums[2] and nums[3]. 
  The sum of distances is |0 - 2| + |0 - 3| = 2 + 3 = 5.
- For nums[1] = 3, there are no other indices with value 3, so arr[1] = 0.
- For nums[2] = 1, there are two other indices with value 1: nums[0] and nums[3]. 
  The sum of distances is |2 - 0| + |2 - 3| = 2 + 1 = 3.
- For nums[3] = 1, there are two other indices with value 1: nums[0] and nums[2]. 
  The sum of distances is |3 - 0| + |3 - 2| = 3 + 1 = 4.
- For nums[4] = 2, there are no other indices with value 2, so arr[4] = 0.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

# Solution
from collections import defaultdict

def sum_of_distances(nums):
    """
    Calculate the sum of distances for each element in the array based on the problem statement.

    :param nums: List[int] - Input array
    :return: List[int] - Result array
    """
    # Step 1: Group indices by value
    value_to_indices = defaultdict(list)
    for i, num in enumerate(nums):
        value_to_indices[num].append(i)
    
    # Step 2: Calculate the sum of distances for each group
    result = [0] * len(nums)
    for indices in value_to_indices.values():
        n = len(indices)
        if n > 1:
            # Prefix sum to calculate distances efficiently
            prefix_sum = [0] * n
            prefix_sum[0] = indices[0]
            for i in range(1, n):
                prefix_sum[i] = prefix_sum[i - 1] + indices[i]
            
            for i in range(n):
                left_sum = prefix_sum[i] if i > 0 else 0
                right_sum = prefix_sum[-1] - prefix_sum[i]
                left_count = i
                right_count = n - i - 1
                result[indices[i]] = (indices[i] * left_count - left_sum) + (right_sum - indices[i] * right_count)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 1, 1, 2]
    print(sum_of_distances(nums1))  # Output: [5, 0, 3, 4, 0]

    # Test Case 2
    nums2 = [1, 1, 1]
    print(sum_of_distances(nums2))  # Output: [4, 2, 4]

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(sum_of_distances(nums3))  # Output: [0, 0, 0, 0]

    # Test Case 4
    nums4 = [1, 1, 2, 2, 2]
    print(sum_of_distances(nums4))  # Output: [1, 1, 3, 2, 3]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Grouping indices by value takes O(n), where n is the length of nums.
- Calculating the sum of distances for each group involves prefix sums and iteration over indices.
  For each group of size k, this takes O(k). Summing over all groups, the total work is O(n).
- Overall time complexity: O(n).

Space Complexity:
- The value_to_indices dictionary stores indices for each unique value in nums. In the worst case, 
  this requires O(n) space.
- The result array requires O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""