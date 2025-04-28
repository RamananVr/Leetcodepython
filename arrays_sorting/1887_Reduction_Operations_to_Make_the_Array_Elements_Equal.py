"""
LeetCode Problem #1887: Reduction Operations to Make the Array Elements Equal

Problem Statement:
Given an integer array `nums`, your goal is to make all the elements in the array equal. 
To achieve this, you can perform the following operation as many times as you want:
- Pick the largest element in the array and reduce it to a smaller value strictly less than itself.

Return the minimum number of operations needed to make all the elements in the array equal.

Constraints:
1. 1 <= nums.length <= 10^5
2. 1 <= nums[i] <= 10^5
"""

def reductionOperations(nums):
    """
    Function to calculate the minimum number of operations to make all elements in the array equal.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum number of operations required.
    """
    # Sort the array in ascending order
    nums.sort()
    
    # Initialize variables
    operations = 0
    prev_operations = 0
    
    # Iterate through the array from the second element
    for i in range(1, len(nums)):
        # If the current element is greater than the previous one, increment the operation count
        if nums[i] > nums[i - 1]:
            prev_operations += 1
        # Add the current operation count to the total
        operations += prev_operations
    
    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 1, 3]
    print(reductionOperations(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 1, 1]
    print(reductionOperations(nums2))  # Output: 0

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    print(reductionOperations(nums3))  # Output: 6

    # Test Case 4
    nums4 = [4, 4, 4, 4]
    print(reductionOperations(nums4))  # Output: 0

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50]
    print(reductionOperations(nums5))  # Output: 10

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- The subsequent iteration through the array takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring the input array).
- No additional data structures are used, so the overall space complexity is O(1).

Topic: Arrays, Sorting
"""