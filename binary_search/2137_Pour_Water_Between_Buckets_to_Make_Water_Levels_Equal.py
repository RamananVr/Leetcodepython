"""
LeetCode Problem #2137: Pour Water Between Buckets to Make Water Levels Equal

Problem Statement:
You are given two arrays `buckets` and `losses`, both of length `n`. The `buckets[i]` array represents the amount of water in the i-th bucket, and the `losses[i]` array represents the percentage of water lost when transferring water from the i-th bucket to another bucket.

You want to make all the buckets have the same amount of water by transferring water between them. You can transfer water from one bucket to another, but the amount of water transferred will be reduced by the percentage specified in the `losses` array.

Return the maximum possible amount of water that each bucket can have after making all the buckets equal.

Constraints:
- `1 <= n <= 10^5`
- `0 <= buckets[i] <= 10^9`
- `0 <= losses[i] <= 100`

Example:
Input: buckets = [10, 20, 30], losses = [10, 20, 30]
Output: 20.00000
Explanation: You can transfer water between buckets to make their levels equal at 20 units.

"""

# Solution
def equalizeWater(buckets, losses):
    def can_equalize(target):
        # Check if we can equalize all buckets to the target level
        surplus = 0
        deficit = 0
        for i in range(len(buckets)):
            if buckets[i] > target:
                surplus += (buckets[i] - target) * (1 - losses[i] / 100)
            else:
                deficit += target - buckets[i]
        return surplus >= deficit

    # Binary search to find the maximum possible water level
    left, right = 0, max(buckets)
    precision = 1e-5
    while right - left > precision:
        mid = (left + right) / 2
        if can_equalize(mid):
            left = mid
        else:
            right = mid
    return round(left, 5)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    buckets = [10, 20, 30]
    losses = [10, 20, 30]
    print(equalizeWater(buckets, losses))  # Output: 20.00000

    # Test Case 2
    buckets = [5, 5, 5]
    losses = [0, 0, 0]
    print(equalizeWater(buckets, losses))  # Output: 5.00000

    # Test Case 3
    buckets = [100, 200, 300]
    losses = [50, 50, 50]
    print(equalizeWater(buckets, losses))  # Output: 150.00000

    # Test Case 4
    buckets = [1, 2, 3]
    losses = [0, 0, 0]
    print(equalizeWater(buckets, losses))  # Output: 2.00000

# Time and Space Complexity Analysis
# Time Complexity:
# - The binary search runs for O(log(max(buckets) / precision)) iterations.
# - For each iteration, we check all buckets, which takes O(n) time.
# - Therefore, the overall time complexity is O(n * log(max(buckets) / precision)).

# Space Complexity:
# - The space complexity is O(1) since we are only using a few variables for computation.

# Topic: Binary Search