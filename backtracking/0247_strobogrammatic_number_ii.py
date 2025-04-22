"""
LeetCode Question #247: Strobogrammatic Number II

Problem Statement:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 
Find all strobogrammatic numbers that are of length `n`.

Example:
Input: n = 2
Output: ["11", "69", "88", "96"]

Constraints:
- 1 <= n <= 14
- The output should be sorted in ascending order.
"""

from typing import List

def findStrobogrammatic(n: int) -> List[str]:
    """
    Function to find all strobogrammatic numbers of length n.
    """
    def helper(current_length: int, total_length: int) -> List[str]:
        # Base case: if the current length is 0, return an empty string
        if current_length == 0:
            return [""]
        # Base case: if the current length is 1, return single-digit strobogrammatic numbers
        if current_length == 1:
            return ["0", "1", "8"]
        
        # Recursive case: build strobogrammatic numbers of smaller lengths
        smaller_numbers = helper(current_length - 2, total_length)
        result = []
        
        for num in smaller_numbers:
            # Add valid strobogrammatic pairs around the smaller numbers
            if current_length != total_length:  # Avoid leading zeros
                result.append("0" + num + "0")
            result.append("1" + num + "1")
            result.append("6" + num + "9")
            result.append("8" + num + "8")
            result.append("9" + num + "6")
        
        return result
    
    return helper(n, n)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 2
    print(f"Strobogrammatic numbers of length {n}: {findStrobogrammatic(n)}")
    # Expected Output: ["11", "69", "88", "96"]

    # Test Case 2
    n = 3
    print(f"Strobogrammatic numbers of length {n}: {findStrobogrammatic(n)}")
    # Expected Output: ["101", "609", "808", "906", "111", "619", "818", "916", "181", "689", "888", "986"]

    # Test Case 3
    n = 1
    print(f"Strobogrammatic numbers of length {n}: {findStrobogrammatic(n)}")
    # Expected Output: ["0", "1", "8"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of strobogrammatic numbers of length `n` is approximately O(5^(n/2)).
- The recursive function generates all valid combinations, and for each smaller number, it adds up to 5 pairs.
- Therefore, the time complexity is O(5^(n/2)).

Space Complexity:
- The space complexity is dominated by the recursion stack and the result list.
- The recursion stack depth is O(n/2), and the result list contains O(5^(n/2)) numbers.
- Therefore, the space complexity is O(5^(n/2)).

Topic: Backtracking
"""