"""
LeetCode Question #976: Largest Perimeter Triangle

Problem Statement:
Given an integer array `nums`, return the largest perimeter of a triangle with a non-zero area, 
formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

A triangle is valid if the sum of any two sides is greater than the third side.

Constraints:
- 3 <= nums.length <= 10^4
- 1 <= nums[i] <= 10^6
"""

def largestPerimeter(nums):
    """
    Function to find the largest perimeter of a triangle with non-zero area.

    Args:
    nums (List[int]): List of integers representing side lengths.

    Returns:
    int: The largest perimeter of a valid triangle, or 0 if no valid triangle can be formed.
    """
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # Iterate through the sorted array to find the largest valid triangle
    for i in range(len(nums) - 2):
        # Check if the triangle inequality holds
        if nums[i] < nums[i + 1] + nums[i + 2]:
            # Return the perimeter of the triangle
            return nums[i] + nums[i + 1] + nums[i + 2]
    
    # If no valid triangle is found, return 0
    return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid triangle with largest perimeter
    nums1 = [2, 1, 2]
    print(largestPerimeter(nums1))  # Output: 5

    # Test Case 2: No valid triangle can be formed
    nums2 = [1, 2, 1]
    print(largestPerimeter(nums2))  # Output: 0

    # Test Case 3: Larger array with valid triangle
    nums3 = [3, 6, 2, 3]
    print(largestPerimeter(nums3))  # Output: 8

    # Test Case 4: All sides are equal
    nums4 = [5, 5, 5]
    print(largestPerimeter(nums4))  # Output: 15

    # Test Case 5: Large array with multiple valid triangles
    nums5 = [10, 15, 20, 25, 30]
    print(largestPerimeter(nums5))  # Output: 70

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The subsequent iteration through the array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so the space complexity is O(1) (excluding input storage).

Topic: Arrays
"""