"""
LeetCode Problem #2562: Find the Array Concatenation Value

Problem Statement:
You are given a 0-indexed integer array `nums`. The concatenation of two numbers is the number formed by concatenating their decimal representations.

- For example, the concatenation of 15 and 49 is 1549.
- The concatenation of 49 and 15 is 4915.

The concatenation value of `nums` is initially equal to 0. Perform the following operation until `nums` becomes empty:

1. If there exists only one element in `nums`, add its value to the concatenation value and remove it.
2. Otherwise, choose the first element and the last element in `nums`. Add the value of their concatenation to the concatenation value, and then remove both elements from `nums`.

Return the final concatenation value after the above operations.

Constraints:
- `1 <= nums.length <= 1000`
- `1 <= nums[i] <= 10^4`
"""

def findTheArrayConcVal(nums):
    """
    Function to calculate the concatenation value of the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The concatenation value of the array.
    """
    concatenation_value = 0
    while len(nums) > 1:
        # Take the first and last elements
        first = nums.pop(0)
        last = nums.pop(-1)
        # Concatenate them as strings and convert back to integer
        concatenation_value += int(str(first) + str(last))
    
    # If there's one element left, add it to the concatenation value
    if nums:
        concatenation_value += nums[0]
    
    return concatenation_value

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 52, 2, 4]
    print(findTheArrayConcVal(nums1))  # Expected Output: 596

    # Test Case 2
    nums2 = [5, 14, 13, 8, 12]
    print(findTheArrayConcVal(nums2))  # Expected Output: 673

    # Test Case 3
    nums3 = [1]
    print(findTheArrayConcVal(nums3))  # Expected Output: 1

    # Test Case 4
    nums4 = [10, 20, 30, 40]
    print(findTheArrayConcVal(nums4))  # Expected Output: 104030

    # Test Case 5
    nums5 = [100, 200]
    print(findTheArrayConcVal(nums5))  # Expected Output: 100200

"""
Time Complexity Analysis:
- The while loop runs until the array is empty. In each iteration, we remove two elements from the array.
- Removing elements from the front of a list (pop(0)) takes O(n) time, while removing from the end (pop(-1)) takes O(1).
- Therefore, the overall time complexity is O(n^2) due to the repeated O(n) operations for pop(0).

Space Complexity Analysis:
- The space complexity is O(1) as we are not using any additional data structures, and the operations are performed in-place.

Topic: Arrays
"""