"""
LeetCode Question #2188: Minimum Time to Finish the Race

Problem Statement:
You are given an integer `n` representing the number of laps you need to complete, and an array `tires` where `tires[i] = [fi, ri]` indicates that the ith tire takes `fi` seconds to finish the first lap and for every subsequent lap, the time taken increases by a factor of `ri`.

    - For example, if `fi = 2` and `ri = 3`, then the tire would take 2 seconds for the first lap, 2 * 3 = 6 seconds for the second lap, 6 * 3 = 18 seconds for the third lap, and so on.

You can change tires after each lap, but changing tires takes an additional `changeTime` seconds.

Return the minimum time to finish the `n` laps.

Constraints:
- `1 <= n <= 1000`
- `1 <= tires.length <= 10^5`
- `tires[i].length == 2`
- `1 <= fi, changeTime <= 10^5`
- `2 <= ri <= 10`

"""

# Solution
from math import inf

def minimumFinishTime(tires, changeTime, n):
    # Precompute the minimum time to complete up to 18 laps with a single tire
    max_laps = 18  # Beyond 18 laps, the time becomes impractical due to exponential growth
    min_time_single_tire = [inf] * (max_laps + 1)
    
    for fi, ri in tires:
        time = fi
        total_time = fi
        for lap in range(1, max_laps + 1):
            min_time_single_tire[lap] = min(min_time_single_tire[lap], total_time)
            time *= ri
            total_time += time
            if total_time > changeTime + min_time_single_tire[lap]:
                break
    
    # DP array to store the minimum time to complete `i` laps
    dp = [inf] * (n + 1)
    dp[0] = 0  # Base case: 0 laps take 0 time
    
    for laps in range(1, n + 1):
        for k in range(1, min(laps, max_laps) + 1):
            dp[laps] = min(dp[laps], dp[laps - k] + min_time_single_tire[k] + changeTime)
    
    return dp[n] - changeTime  # Subtract the last changeTime as it's not needed after the final lap

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tires = [[2, 3], [3, 4]]
    changeTime = 5
    n = 4
    print(minimumFinishTime(tires, changeTime, n))  # Expected Output: 14

    # Test Case 2
    tires = [[1, 10], [2, 2]]
    changeTime = 6
    n = 5
    print(minimumFinishTime(tires, changeTime, n))  # Expected Output: 25

    # Test Case 3
    tires = [[1, 2], [2, 3]]
    changeTime = 4
    n = 3
    print(minimumFinishTime(tires, changeTime, n))  # Expected Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- Precomputing the minimum time for up to 18 laps with a single tire takes O(tires.length * max_laps).
- Filling the DP array takes O(n * max_laps).
- Overall complexity: O(tires.length * max_laps + n * max_laps), where max_laps is a constant (18).

Space Complexity:
- The space complexity is O(n + max_laps), where `n` is the number of laps and `max_laps` is the constant 18.
"""

# Topic: Dynamic Programming