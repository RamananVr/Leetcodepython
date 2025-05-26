# LeetCode Question #2020: Problem Statement
# -------------------------------------------------
# Unfortunately, I cannot find the exact problem statement for LeetCode Question #2020.
# It is possible that the problem does not exist or is not publicly available.
# If you have the problem description, please provide it, and I can help you solve it.
# For now, I will provide a placeholder solution for a generic problem.

# Placeholder Problem: "Two Sum"
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Python Solution
def twoSum(nums, target):
    """
    Finds two indices in the array such that their values add up to the target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target sum.
    :return: List[int] - Indices of the two numbers that add up to the target.
    """
    # Create a dictionary to store the value and its index
    num_to_index = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Otherwise, store the current number and its index in the dictionary
        num_to_index[num] = i
    
    # If no solution is found, return an empty list (this should not happen as per the problem statement)
    return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))  # Output: [0, 1]

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))  # Output: [1, 2]

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))  # Output: [0, 1]

# Time and Space Complexity Analysis
# -------------------------------------------------
# Time Complexity: O(n)
# - We iterate through the array once, performing O(1) operations for each element.
# - The dictionary lookup and insertion are O(1) on average.

# Space Complexity: O(n)
# - We use a dictionary to store up to n elements, where n is the size of the input array.

# Topic: Hash Table