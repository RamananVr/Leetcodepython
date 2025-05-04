"""
LeetCode Problem #2567: Minimum Score by Changing Two Elements

Problem Statement:
You are given a 0-indexed integer array nums.

- The score of nums is the difference between the maximum and minimum elements in nums.
- The score of an array of size 1 is 0.

You can change two elements of nums to any value you want (possibly the same value).

Return the minimum possible score after changing exactly two elements.

Constraints:
- 2 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def minimizeScore(nums):
    """
    Function to calculate the minimum possible score after changing exactly two elements.
    """
    # If the array has only two elements, the score is always 0 after changing both.
    if len(nums) <= 2:
        return 0

    # Sort the array to easily access the smallest and largest elements.
    nums.sort()

    # Consider the following cases:
    # 1. Change the two largest elements to the value of the third largest.
    # 2. Change the two smallest elements to the value of the third smallest.
    # 3. Change the largest and smallest elements to the second largest and second smallest values respectively.
    # 4. Change the largest and smallest elements to the third largest and third smallest values respectively.

    # Calculate the possible scores for each case.
    case1 = nums[-3] - nums[0]  # Change the two largest elements.
    case2 = nums[-1] - nums[2]  # Change the two smallest elements.
    case3 = nums[-2] - nums[1]  # Change one largest and one smallest element.
    case4 = nums[-3] - nums[2]  # Change both largest and smallest to middle values.

    # Return the minimum score among all cases.
    return min(case1, case2, case3, case4)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 7, 8, 5]
    print(minimizeScore(nums1))  # Expected Output: 1

    # Test Case 2
    nums2 = [10, 20, 30, 40, 50]
    print(minimizeScore(nums2))  # Expected Output: 10

    # Test Case 3
    nums3 = [1, 1, 1, 1]
    print(minimizeScore(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [100, 200]
    print(minimizeScore(nums4))  # Expected Output: 0

    # Test Case 5
    nums5 = [1, 3, 6, 10, 15]
    print(minimizeScore(nums5))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Calculating the four cases takes O(1).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, so no additional space is used apart from a few variables.
- Overall space complexity: O(1).

Topic: Arrays, Sorting
"""