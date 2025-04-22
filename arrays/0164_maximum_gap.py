"""
LeetCode Question #164: Maximum Gap

Problem Statement:
Given an integer array `nums`, return the maximum difference between two successive elements in its sorted form. 
If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

# Solution
def maximumGap(nums):
    """
    Finds the maximum gap between two successive elements in the sorted form of the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum gap between two successive elements in the sorted form of the array.
    """
    if len(nums) < 2:
        return 0

    # Step 1: Find the minimum and maximum values in the array
    min_val, max_val = min(nums), max(nums)

    # Step 2: Calculate the bucket size and number of buckets
    n = len(nums)
    bucket_size = max(1, (max_val - min_val) // (n - 1))
    bucket_count = (max_val - min_val) // bucket_size + 1

    # Step 3: Initialize buckets
    buckets = [[float('inf'), float('-inf')] for _ in range(bucket_count)]

    # Step 4: Place each number in its corresponding bucket
    for num in nums:
        bucket_index = (num - min_val) // bucket_size
        buckets[bucket_index][0] = min(buckets[bucket_index][0], num)
        buckets[bucket_index][1] = max(buckets[bucket_index][1], num)

    # Step 5: Calculate the maximum gap
    max_gap = 0
    prev_max = min_val

    for bucket in buckets:
        if bucket[0] == float('inf') and bucket[1] == float('-inf'):
            # Skip empty buckets
            continue
        max_gap = max(max_gap, bucket[0] - prev_max)
        prev_max = bucket[1]

    return max_gap

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 6, 9, 1]
    print(maximumGap(nums1))  # Expected Output: 3

    # Test Case 2
    nums2 = [10]
    print(maximumGap(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [1, 10000000]
    print(maximumGap(nums3))  # Expected Output: 9999999

    # Test Case 4
    nums4 = [1, 3, 7, 9, 15]
    print(maximumGap(nums4))  # Expected Output: 6

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    print(maximumGap(nums5))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the minimum and maximum values takes O(n).
- Placing elements into buckets takes O(n).
- Calculating the maximum gap by iterating through the buckets takes O(bucket_count), which is at most O(n).
Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses O(bucket_count) space for the buckets, which is proportional to the number of elements in the array.
- Therefore, the space complexity is O(n).

Topic: Arrays
"""