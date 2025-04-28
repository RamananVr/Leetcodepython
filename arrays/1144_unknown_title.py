"""
LeetCode Problem #1144: Decrease Elements To Make Array Zigzag

Problem Statement:
Given an array `nums` of integers, a "zigzag" array is defined as an array where every even-indexed element is greater than its adjacent elements, 
and every odd-indexed element is less than its adjacent elements. More formally, for every even index `i`, 
`nums[i] > nums[i-1]` and `nums[i] > nums[i+1]` (if they exist), and for every odd index `i`, 
`nums[i] < nums[i-1]` and `nums[i] < nums[i+1]` (if they exist).

You can decrease the value of any element in the array as many times as you want. The cost of doing so is 1 for each decrease.

Return the minimum cost to make the array a zigzag array.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def movesToMakeZigzag(nums):
    """
    Function to calculate the minimum cost to make the array a zigzag array.
    
    :param nums: List[int] - The input array of integers.
    :return: int - The minimum cost to make the array zigzag.
    """
    n = len(nums)
    
    # Helper function to calculate the cost for a specific parity (even or odd)
    def calculate_cost(parity):
        cost = 0
        for i in range(n):
            if i % 2 == parity:
                decrease = 0
                if i > 0 and nums[i] >= nums[i - 1]:
                    decrease = max(decrease, nums[i] - nums[i - 1] + 1)
                if i < n - 1 and nums[i] >= nums[i + 1]:
                    decrease = max(decrease, nums[i] - nums[i + 1] + 1)
                cost += decrease
        return cost
    
    # Calculate the cost for both even and odd parity
    return min(calculate_cost(0), calculate_cost(1))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(movesToMakeZigzag(nums1))  # Output: 2

    # Test Case 2
    nums2 = [9, 6, 1, 6, 2]
    print(movesToMakeZigzag(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 2, 1]
    print(movesToMakeZigzag(nums3))  # Output: 0

    # Test Case 4
    nums4 = [10, 4, 4, 10]
    print(movesToMakeZigzag(nums4))  # Output: 4

"""
Time Complexity Analysis:
- The function iterates through the array twice (once for each parity: even and odd).
- For each element, it performs constant-time operations to calculate the decrease needed.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The function uses a constant amount of extra space for variables and calculations.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""