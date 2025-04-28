"""
LeetCode Problem #2051: The Category of Each Member in the Array

Problem Statement:
You are given an array `nums` of integers and an integer `k`. A member of the array is considered "special" if it is greater than or equal to `k`. Your task is to categorize each member of the array into one of three categories:
1. "Special" if the number is greater than or equal to `k`.
2. "Normal" if the number is less than `k` but greater than or equal to `k // 2`.
3. "Low" if the number is less than `k // 2`.

Return a list of strings where each string represents the category of the corresponding number in the input array.

Constraints:
- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `1 <= k <= 10^4`
"""

def categorize_members(nums, k):
    """
    Categorize each member of the array into "Special", "Normal", or "Low".

    Args:
    nums (List[int]): The input array of integers.
    k (int): The threshold value for categorization.

    Returns:
    List[str]: A list of strings representing the category of each number.
    """
    result = []
    for num in nums:
        if num >= k:
            result.append("Special")
        elif num >= k // 2:
            result.append("Normal")
        else:
            result.append("Low")
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [10, 5, 2, 15, 7]
    k1 = 10
    print(categorize_members(nums1, k1))  # Output: ['Special', 'Normal', 'Low', 'Special', 'Normal']

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 3
    print(categorize_members(nums2, k2))  # Output: ['Low', 'Normal', 'Special', 'Special', 'Special']

    # Test Case 3
    nums3 = [0, -5, 20, 10, 5]
    k3 = 10
    print(categorize_members(nums3, k3))  # Output: ['Low', 'Low', 'Special', 'Special', 'Normal']

    # Test Case 4
    nums4 = [100, 50, 25, 10, 5]
    k4 = 50
    print(categorize_members(nums4, k4))  # Output: ['Special', 'Special', 'Normal', 'Low', 'Low']

    # Test Case 5
    nums5 = [1]
    k5 = 1
    print(categorize_members(nums5, k5))  # Output: ['Special']

"""
Time Complexity:
- The function iterates through the `nums` array once, performing constant-time operations for each element.
- Let `n` be the length of the array. The time complexity is O(n).

Space Complexity:
- The function uses a list `result` to store the output, which has the same size as the input array.
- The space complexity is O(n).

Topic: Arrays
"""