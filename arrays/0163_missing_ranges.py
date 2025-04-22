"""
LeetCode Question #163: Missing Ranges

Problem Statement:
You are given a sorted unique integer array `nums` and two integers `lower` and `upper` representing the inclusive range [lower, upper].
Return a list of the smallest sorted ranges that cover every missing number exactly. That is, no number is repeated in the ranges and each missing number is covered by one of the ranges.

Each range [a, b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example 1:
Input: nums = [0, 1, 3, 50, 75], lower = 0, upper = 99
Output: ["2", "4->49", "51->74", "76->99"]

Example 2:
Input: nums = [], lower = 1, upper = 1
Output: ["1"]

Example 3:
Input: nums = [], lower = -3, upper = -1
Output: ["-3->-1"]

Example 4:
Input: nums = [-1], lower = -1, upper = -1
Output: []

Constraints:
- `nums` is sorted in ascending order and all elements are unique.
- `0 <= nums.length <= 100`
- `-10^9 <= nums[i], lower, upper <= 10^9`
- `lower <= upper`
"""

def findMissingRanges(nums, lower, upper):
    """
    Finds the missing ranges in the inclusive range [lower, upper] given a sorted unique integer array nums.

    :param nums: List[int] - Sorted unique integer array
    :param lower: int - Lower bound of the range
    :param upper: int - Upper bound of the range
    :return: List[str] - List of missing ranges
    """
    def formatRange(start, end):
        """Helper function to format a range."""
        if start == end:
            return str(start)
        return f"{start}->{end}"

    result = []
    prev = lower - 1  # Initialize previous number to one less than lower

    # Iterate through nums and add missing ranges
    for num in nums:
        if num > prev + 1:  # Check for a gap
            result.append(formatRange(prev + 1, num - 1))
        prev = num  # Update previous number

    # Check for a gap between the last number and upper
    if upper > prev:
        result.append(formatRange(prev + 1, upper))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(findMissingRanges(nums, lower, upper))  # Output: ["2", "4->49", "51->74", "76->99"]

    # Test Case 2
    nums = []
    lower = 1
    upper = 1
    print(findMissingRanges(nums, lower, upper))  # Output: ["1"]

    # Test Case 3
    nums = []
    lower = -3
    upper = -1
    print(findMissingRanges(nums, lower, upper))  # Output: ["-3->-1"]

    # Test Case 4
    nums = [-1]
    lower = -1
    upper = -1
    print(findMissingRanges(nums, lower, upper))  # Output: []

    # Test Case 5
    nums = [1, 3, 5, 7]
    lower = 0
    upper = 8
    print(findMissingRanges(nums, lower, upper))  # Output: ["0", "2", "4", "6", "8"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the `nums` array once, performing constant-time operations for each element.
- Additionally, it checks for a gap between the last number and `upper`.
- Therefore, the time complexity is O(n), where n is the length of the `nums` array.

Space Complexity:
- The function uses a list `result` to store the missing ranges, which can have at most O(n + 1) elements (including the range from `lower` to `upper`).
- The space complexity is O(n) for the result list.

Topic: Arrays
"""