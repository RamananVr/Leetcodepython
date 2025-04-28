"""
LeetCode Problem #1399: Count Largest Group

Problem Statement:
You are given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
Return the number of groups that have the largest size.

Example 1:
Input: n = 13
Output: 4
Explanation: There are 4 groups [1,10], [2,11], [3,12], [4,13]. All of them have size 2.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2]. Both of them have size 1.

Constraints:
- 1 <= n <= 10^4
"""

from collections import defaultdict

def countLargestGroup(n: int) -> int:
    """
    Function to count the number of groups with the largest size.
    """
    # Dictionary to store the size of each group based on digit sum
    digit_sum_groups = defaultdict(int)
    
    # Calculate the digit sum for each number from 1 to n
    for num in range(1, n + 1):
        digit_sum = sum(int(digit) for digit in str(num))
        digit_sum_groups[digit_sum] += 1
    
    # Find the maximum group size
    max_group_size = max(digit_sum_groups.values())
    
    # Count the number of groups with the maximum size
    largest_group_count = sum(1 for size in digit_sum_groups.values() if size == max_group_size)
    
    return largest_group_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 13
    print(f"Input: n = {n1}, Output: {countLargestGroup(n1)}")  # Expected Output: 4

    # Test Case 2
    n2 = 2
    print(f"Input: n = {n2}, Output: {countLargestGroup(n2)}")  # Expected Output: 2

    # Test Case 3
    n3 = 15
    print(f"Input: n = {n3}, Output: {countLargestGroup(n3)}")  # Expected Output: 6

    # Test Case 4
    n4 = 24
    print(f"Input: n = {n4}, Output: {countLargestGroup(n4)}")  # Expected Output: 5

"""
Time Complexity Analysis:
- Calculating the digit sum for each number from 1 to n takes O(d), where d is the number of digits in the number.
  Since there are n numbers, the total time complexity is O(n * d). In the worst case, d = log10(n), so the complexity
  becomes O(n * log10(n)).
- Finding the maximum group size and counting the groups with the maximum size takes O(k), where k is the number of unique digit sums.
  Since k is much smaller than n, this step is negligible compared to the first step.

Overall Time Complexity: O(n * log10(n))

Space Complexity Analysis:
- The space complexity is determined by the size of the `digit_sum_groups` dictionary, which stores the count of each digit sum.
  In the worst case, there are O(log10(n)) unique digit sums (e.g., for n = 9999, the maximum digit sum is 36).
- Thus, the space complexity is O(log10(n)).

Overall Space Complexity: O(log10(n))

Topic: Hash Table
"""