"""
LeetCode Problem #2814: Minimum Operations to Make Array Equal II

Problem Statement:
You are given two integer arrays nums1 and nums2 of length n.

In one operation, you can choose any index i (0 <= i < n) and increment nums1[i] by 1 or decrement nums1[i] by 1.

Return the minimum number of operations required to make nums1 equal to nums2. If it is impossible to make the arrays equal, return -1.

Constraints:
- nums1.length == nums2.length == n
- 1 <= n <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^9
"""

# Solution
def minOperations(nums1, nums2):
    """
    Calculate the minimum number of operations to make nums1 equal to nums2.
    If impossible, return -1.
    
    :param nums1: List[int] - First array
    :param nums2: List[int] - Second array
    :return: int - Minimum number of operations or -1 if impossible
    """
    # Calculate the difference between nums1 and nums2
    total_diff = sum(nums2) - sum(nums1)
    
    # If the total difference is odd, it's impossible to equalize the arrays
    if total_diff % 2 != 0:
        return -1
    
    # Calculate the absolute differences for each element
    diffs = [abs(nums1[i] - nums2[i]) for i in range(len(nums1))]
    
    # Sort the differences in descending order
    diffs.sort(reverse=True)
    
    # Initialize variables
    operations = 0
    current_diff = 0
    
    # Iterate through the sorted differences
    for diff in diffs:
        current_diff += diff
        operations += 1
        
        # Check if the current difference matches the total difference
        if current_diff == total_diff:
            return operations
    
    # If we exhaust all differences and cannot match the total difference, return -1
    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(minOperations(nums1, nums2))  # Expected Output: 3
    
    # Test Case 2
    nums1 = [1, 1, 1]
    nums2 = [2, 2, 2]
    print(minOperations(nums1, nums2))  # Expected Output: 3
    
    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 3]
    print(minOperations(nums1, nums2))  # Expected Output: 0
    
    # Test Case 4
    nums1 = [1, 2, 3]
    nums2 = [1, 2, 4]
    print(minOperations(nums1, nums2))  # Expected Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the total difference: O(n)
- Calculating absolute differences: O(n)
- Sorting the differences: O(n log n)
- Iterating through the sorted differences: O(n)
Overall: O(n log n)

Space Complexity:
- Storing the differences array: O(n)
Overall: O(n)
"""

# Topic: Arrays