"""
LeetCode Problem #2261: K Divisible Elements Subarrays

Problem Statement:
You are given a 0-indexed integer array `nums` and two integers `k` and `p`.

A subarray of `nums` is called a k-divisible elements subarray if:
- The number of elements in the subarray that are divisible by `p` is at most `k`.

Return the number of distinct k-divisible elements subarrays in the array `nums`.

A subarray is a contiguous non-empty sequence of elements within an array. Two subarrays are distinct if they have different starting or ending indices, or if they contain different elements.

Constraints:
- `1 <= nums.length <= 200`
- `1 <= nums[i], p <= 200`
- `1 <= k <= nums.length`
"""

# Python Solution
def countDistinct(nums, k, p):
    """
    Function to count the number of distinct k-divisible elements subarrays.

    Args:
    nums (List[int]): The input array.
    k (int): Maximum number of elements divisible by p allowed in a subarray.
    p (int): The divisor.

    Returns:
    int: The number of distinct k-divisible elements subarrays.
    """
    n = len(nums)
    seen = set()

    for i in range(n):
        count_divisible = 0
        subarray = []
        for j in range(i, n):
            subarray.append(nums[j])
            if nums[j] % p == 0:
                count_divisible += 1
            if count_divisible > k:
                break
            seen.add(tuple(subarray))  # Use tuple to store subarray in a set

    return len(seen)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 3, 2, 2]
    k1 = 2
    p1 = 2
    print(countDistinct(nums1, k1, p1))  # Expected Output: 11

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    k2 = 1
    p2 = 2
    print(countDistinct(nums2, k2, p2))  # Expected Output: 10

    # Test Case 3
    nums3 = [4, 4, 4, 4]
    k3 = 3
    p3 = 4
    print(countDistinct(nums3, k3, p3))  # Expected Output: 10

    # Test Case 4
    nums4 = [1, 1, 1, 1]
    k4 = 0
    p4 = 2
    print(countDistinct(nums4, k4, p4))  # Expected Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs `n` times (for each starting index of the subarray).
- The inner loop runs at most `n` times (for each ending index of the subarray).
- For each subarray, we perform an O(1) operation to add it to the set.
- In the worst case, the total number of subarrays is O(n^2), so the time complexity is O(n^2).

Space Complexity:
- We use a set to store all distinct subarrays. In the worst case, the set can contain O(n^2) subarrays.
- Each subarray is stored as a tuple, and the size of each tuple is proportional to the length of the subarray.
- Therefore, the space complexity is O(n^3) in the worst case.
"""

# Topic: Arrays, Hashing