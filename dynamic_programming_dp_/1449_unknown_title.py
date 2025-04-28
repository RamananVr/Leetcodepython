"""
LeetCode Problem #1449: Form Largest Integer With Digits That Add up to Target

Problem Statement:
You are given an integer array `cost` where `cost[i]` is the cost of `i + 1`-th digit (1-indexed). 
You are also given an integer `target`. Return the largest integer you can paint under the following conditions:
- The cost of painting a digit `i + 1` is `cost[i]`.
- The total cost used must be equal to `target`.
- If it is impossible to paint any integer, return "0".

Note: The integer painted must not contain leading zeros.

Example 1:
Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"
Explanation: The cost to paint the digit '7' is 2, and the total cost is 2 + 2 + 2 + 3 = 9. 
You can paint the digits "7772", forming the largest integer.

Example 2:
Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: "85"
Explanation: The cost to paint the digit '8' is 7, and the cost to paint the digit '5' is 5. 
The total cost is 7 + 5 = 12, and "85" is the largest number.

Example 3:
Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: "0"
Explanation: It is impossible to paint any integer with total cost equal to target.

Constraints:
- `cost.length == 9`
- `1 <= cost[i] <= 5000`
- `1 <= target <= 5000`
"""

# Solution
def largestNumber(cost, target):
    # dp[i] will store the largest number we can form with cost equal to i
    dp = [""] * (target + 1)
    
    for t in range(1, target + 1):
        for digit in range(9):
            if t >= cost[digit] and dp[t - cost[digit]] != "0":
                candidate = dp[t - cost[digit]] + str(digit + 1)
                dp[t] = max(dp[t], candidate, key=lambda x: (len(x), x))
    
    return dp[target] if dp[target] else "0"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cost = [4,3,2,5,6,7,2,5,5]
    target = 9
    print(largestNumber(cost, target))  # Output: "7772"

    # Test Case 2
    cost = [7,6,5,5,5,6,8,7,8]
    target = 12
    print(largestNumber(cost, target))  # Output: "85"

    # Test Case 3
    cost = [2,4,6,2,4,6,4,4,4]
    target = 5
    print(largestNumber(cost, target))  # Output: "0"

    # Test Case 4
    cost = [1,1,1,1,1,1,1,1,1]
    target = 9
    print(largestNumber(cost, target))  # Output: "999999999"

    # Test Case 5
    cost = [1,2,3,4,5,6,7,8,9]
    target = 15
    print(largestNumber(cost, target))  # Output: "555"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `target` iterations.
- The inner loop runs for 9 iterations (fixed number of digits).
- For each iteration, we perform string concatenation and comparison, which is proportional to the length of the string.
- In the worst case, the length of the string can be proportional to `target`.
- Therefore, the time complexity is O(target * 9 * target) = O(target^2).

Space Complexity:
- We use a DP array of size `target + 1`, where each element is a string.
- In the worst case, the total space used by strings can be proportional to `target^2`.
- Therefore, the space complexity is O(target^2).
"""

# Topic: Dynamic Programming (DP)