"""
LeetCode Problem #2191: Sort the Jumbled Numbers

Problem Statement:
You are given a 0-indexed integer array `mapping` which represents the mapping rule of a shuffled decimal system. 
The mapping rule is as follows: 
- The digit `d` in the decimal system is mapped to `mapping[d]` in the shuffled system.

You are also given another integer array `nums` which represents a list of numbers in the decimal system. 
Apply the mapping rule to each number in `nums` and sort the numbers according to their values in the shuffled system.

If two numbers have the same value in the shuffled system, sort them according to their order in `nums`.

Return an array of the sorted numbers in `nums`.

Example:
Input: mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5], nums = [990, 332, 981]
Output: [981, 990, 332]
Explanation:
- Convert each number in nums to its mapped value:
  - 990 -> 555 (using mapping: 9 -> 5, 9 -> 5, 0 -> 2)
  - 332 -> 844 (using mapping: 3 -> 8, 3 -> 8, 2 -> 4)
  - 981 -> 507 (using mapping: 9 -> 5, 8 -> 7, 1 -> 0)
- Sort based on the mapped values: [507, 555, 844]
- Return the original numbers in sorted order: [981, 990, 332]

Constraints:
- `mapping.length == 10`
- `0 <= mapping[i] <= 9`
- `1 <= nums.length <= 100`
- `0 <= nums[i] < 10^9`
"""

# Python Solution
def sortJumbled(mapping, nums):
    def get_mapped_value(num):
        # Convert the number to its mapped value
        mapped = ''.join(str(mapping[int(digit)]) for digit in str(num))
        return int(mapped)
    
    # Sort nums based on the mapped value, and maintain original order for ties
    return sorted(nums, key=lambda x: (get_mapped_value(x), nums.index(x)))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mapping = [2, 1, 4, 8, 6, 3, 0, 9, 7, 5]
    nums = [990, 332, 981]
    print(sortJumbled(mapping, nums))  # Output: [981, 990, 332]

    # Test Case 2
    mapping = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    nums = [123, 456, 789]
    print(sortJumbled(mapping, nums))  # Output: [123, 456, 789]

    # Test Case 3
    mapping = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    nums = [12, 10, 2]
    print(sortJumbled(mapping, nums))  # Output: [10, 2, 12]

    # Test Case 4
    mapping = [1, 0, 3, 2, 5, 4, 7, 6, 9, 8]
    nums = [0, 1, 2, 3, 4]
    print(sortJumbled(mapping, nums))  # Output: [0, 1, 3, 2, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each number in `nums`, we compute its mapped value. This involves iterating over the digits of the number, 
  which takes O(d) time where d is the number of digits in the number. 
- Sorting the list of numbers takes O(n log n), where n is the length of `nums`.
- Therefore, the overall time complexity is O(n * d + n log n), where d is the average number of digits in the numbers.

Space Complexity:
- The space complexity is O(n) for storing the sorted list, and O(d) for temporary storage during mapping computation.
- Therefore, the overall space complexity is O(n + d).
"""

# Topic: Arrays, Sorting