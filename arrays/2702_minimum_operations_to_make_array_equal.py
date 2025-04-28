"""
LeetCode Question #2702: Minimum Operations to Make Array Equal

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n`. The arrays are said to be equal if for every index `i` (0 <= i < n), `nums1[i] == nums2[i]`.

In one operation, you can choose any index `i` (0 <= i < n) and increment or decrement `nums1[i]` by 1.

Return the minimum number of operations required to make `nums1` and `nums2` equal. If it is impossible to make the arrays equal, return -1.

Constraints:
- `nums1.length == nums2.length == n`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^9`
"""

# Python Solution
def minOperations(nums1, nums2):
    """
    Calculate the minimum number of operations to make nums1 equal to nums2.

    Args:
    nums1 (List[int]): The first array.
    nums2 (List[int]): The second array.

    Returns:
    int: The minimum number of operations required, or -1 if impossible.
    """
    # Calculate the difference between the two arrays
    total_diff = sum(nums2) - sum(nums1)
    
    # If the total difference is not divisible by n, it's impossible to equalize
    if total_diff % len(nums1) != 0:
        return -1
    
    # Calculate the target difference per element
    target_diff = total_diff // len(nums1)
    
    # Calculate the number of operations required
    operations = 0
    for i in range(len(nums1)):
        operations += abs(nums2[i] - (nums1[i] + target_diff))
    
    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Arrays are already equal
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    print(minOperations(nums1, nums2))  # Output: 0

    # Test Case 2: Arrays can be made equal
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(minOperations(nums1, nums2))  # Output: 9

    # Test Case 3: Arrays cannot be made equal
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 5]
    print(minOperations(nums1, nums2))  # Output: -1

    # Test Case 4: Large difference
    nums1 = [1, 1, 1]
    nums2 = [1000000000, 1000000000, 1000000000]
    print(minOperations(nums1, nums2))  # Output: 2999999997

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the sum of nums1 and nums2 takes O(n).
- Iterating through nums1 and nums2 to calculate the operations takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- We use a constant amount of extra space for variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays