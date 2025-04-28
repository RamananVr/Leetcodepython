"""
LeetCode Problem #1470: Shuffle the Array

Problem Statement:
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:
Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:
Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:
Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

Constraints:
- 1 <= n <= 500
- nums.length == 2n
- 1 <= nums[i] <= 10^3
"""

# Python Solution
def shuffle(nums, n):
    """
    Rearranges the array nums in the form [x1, y1, x2, y2, ..., xn, yn].

    Args:
    nums (List[int]): The input array of size 2n.
    n (int): The number of elements in each half of the array.

    Returns:
    List[int]: The shuffled array.
    """
    result = []
    for i in range(n):
        result.append(nums[i])  # Add element from the first half
        result.append(nums[i + n])  # Add corresponding element from the second half
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 5, 1, 3, 4, 7]
    n1 = 3
    print(shuffle(nums1, n1))  # Output: [2, 3, 5, 4, 1, 7]

    # Test Case 2
    nums2 = [1, 2, 3, 4, 4, 3, 2, 1]
    n2 = 4
    print(shuffle(nums2, n2))  # Output: [1, 4, 2, 3, 3, 2, 4, 1]

    # Test Case 3
    nums3 = [1, 1, 2, 2]
    n3 = 2
    print(shuffle(nums3, n3))  # Output: [1, 2, 1, 2]

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the first n elements of the array, performing O(1) operations for each element.
Thus, the time complexity is O(n).

Space Complexity:
The function uses an additional list `result` to store the shuffled elements. The size of this list is 2n.
Thus, the space complexity is O(n).
"""

# Topic: Arrays