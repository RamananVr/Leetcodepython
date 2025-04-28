"""
LeetCode Problem #1383: Maximum Performance of a Team

Problem Statement:
You are given two integers `n` and `k` and two integer arrays `speed` and `efficiency`, both of length `n`. 
There are `n` engineers numbered from 1 to `n`. `speed[i]` and `efficiency[i]` represent the speed and 
efficiency of the i-th engineer, respectively.

Choose at most `k` different engineers out of the `n` engineers to form a team with the maximum performance.

The performance of a team is defined as:
    - The sum of their speeds multiplied by the minimum efficiency among their members.

Return the maximum performance of this team modulo `10^9 + 7`.

Constraints:
1. 1 <= n <= 10^5
2. 1 <= k <= n
3. speed.length == efficiency.length == n
4. 1 <= speed[i] <= 10^5
5. 1 <= efficiency[i] <= 10^8

Example:
Input: n = 6, speed = [2, 10, 3, 1, 5, 8], efficiency = [5, 4, 3, 9, 7, 2], k = 2
Output: 60
Explanation: 
    We choose the engineers with speeds [10, 5] and efficiencies [4, 7].
    Performance = (10 + 5) * min(4, 7) = 15 * 4 = 60.

Follow-up:
Can you solve the problem in O(n log n) time complexity?
"""

from heapq import heappush, heappop

def maxPerformance(n, speed, efficiency, k):
    """
    Calculate the maximum performance of a team of engineers.

    :param n: int - Number of engineers
    :param speed: List[int] - Speed of each engineer
    :param efficiency: List[int] - Efficiency of each engineer
    :param k: int - Maximum number of engineers in the team
    :return: int - Maximum performance modulo 10^9 + 7
    """
    MOD = 10**9 + 7

    # Pair efficiency and speed, and sort by efficiency in descending order
    engineers = sorted(zip(efficiency, speed), reverse=True, key=lambda x: x[0])

    max_performance = 0
    speed_sum = 0
    speed_heap = []

    for eff, spd in engineers:
        # Add current speed to the heap and update the speed sum
        heappush(speed_heap, spd)
        speed_sum += spd

        # If the heap size exceeds k, remove the smallest speed
        if len(speed_heap) > k:
            speed_sum -= heappop(speed_heap)

        # Calculate performance with the current efficiency as the minimum
        max_performance = max(max_performance, speed_sum * eff)

    return max_performance % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 2
    print(maxPerformance(n, speed, efficiency, k))  # Output: 60

    # Test Case 2
    n = 6
    speed = [2, 10, 3, 1, 5, 8]
    efficiency = [5, 4, 3, 9, 7, 2]
    k = 3
    print(maxPerformance(n, speed, efficiency, k))  # Output: 68

    # Test Case 3
    n = 3
    speed = [2, 8, 2]
    efficiency = [2, 7, 1]
    k = 2
    print(maxPerformance(n, speed, efficiency, k))  # Output: 56

# Time Complexity Analysis:
# Sorting the engineers by efficiency takes O(n log n).
# Iterating through the engineers and maintaining a heap of size k takes O(n log k).
# Overall time complexity: O(n log n).

# Space Complexity Analysis:
# The heap can grow to a maximum size of k, so the space complexity is O(k).
# Overall space complexity: O(k).

# Topic: Greedy, Heap (Priority Queue), Sorting