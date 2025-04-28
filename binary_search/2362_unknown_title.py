"""
LeetCode Problem #2362: Generate the Problem Statement

Problem Statement:
You are given an array `weights` where `weights[i]` represents the weight of the i-th item. 
You are also given an integer `k` which represents the number of groups you need to divide the items into. 
The goal is to divide the items into `k` groups such that the maximum weight of any group is minimized.

Return the minimized maximum weight of any group.

Constraints:
- 1 <= weights.length <= 10^5
- 1 <= weights[i] <= 10^6
- 1 <= k <= weights.length
"""

# Solution
def minimizeMaxWeight(weights, k):
    def canDivide(maxWeight):
        groups = 1
        currentSum = 0
        for weight in weights:
            if currentSum + weight > maxWeight:
                groups += 1
                currentSum = weight
                if groups > k:
                    return False
            else:
                currentSum += weight
        return True

    # Binary search for the minimized maximum weight
    left, right = max(weights), sum(weights)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if canDivide(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    weights1 = [10, 20, 30, 40]
    k1 = 2
    print(minimizeMaxWeight(weights1, k1))  # Expected Output: 60

    # Test Case 2
    weights2 = [1, 2, 3, 4, 5]
    k2 = 3
    print(minimizeMaxWeight(weights2, k2))  # Expected Output: 5

    # Test Case 3
    weights3 = [7, 2, 5, 10, 8]
    k3 = 2
    print(minimizeMaxWeight(weights3, k3))  # Expected Output: 18

    # Test Case 4
    weights4 = [1, 1, 1, 1, 1, 1, 1, 1]
    k4 = 4
    print(minimizeMaxWeight(weights4, k4))  # Expected Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(sum(weights) - max(weights))).
- For each binary search iteration, we iterate through the weights array to check if the division is possible, which takes O(n).
- Therefore, the overall time complexity is O(n * log(sum(weights) - max(weights))).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables for computation.

Topic: Binary Search
"""