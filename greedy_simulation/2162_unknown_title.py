"""
LeetCode Problem #2162: Minimum Cost to Set Cooking Time

Problem Statement:
A generic microwave supports cooking times from 1 second to 99 minutes and 99 seconds (inclusive). 
To set the cooking time, you push at most four digits. The microwave normalizes the cooking time so 
that it falls within the range of 1 second to 99 minutes and 99 seconds. It then interprets the 
pushed digits as the cooking time in minutes and seconds.

- For example, if you push 1, 2, 3, and 4, then it represents 12 minutes and 34 seconds.
- If you push 0, 0, 0, and 8, then it represents 8 seconds.
- If you push 8, 0, 0, and 0, then it represents 80 minutes and 0 seconds.

You are given integers `startAt`, `moveCost`, `pushCost`, and `targetSeconds`. Initially, your 
finger is on the digit `startAt`. Moving the finger to another digit costs `moveCost` units of 
effort. Pushing the digit under the finger costs `pushCost` units of effort.

Return the minimum cost to set the microwave to cook for `targetSeconds` seconds.

Notes:
- You can push the digits in any order.
- The microwave normalizes the cooking time, so leading zeros are ignored.
- The cooking time must be between 1 second and 99 minutes and 99 seconds.

Constraints:
- 0 <= startAt <= 9
- 1 <= moveCost, pushCost <= 10^4
- 1 <= targetSeconds <= 99 * 60 + 99
"""

def minCostSetTime(startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
    def calculate_cost(start, digits):
        cost = 0
        current = start
        for digit in digits:
            if digit != current:
                cost += moveCost
                current = digit
            cost += pushCost
        return cost

    def format_time(seconds):
        minutes = seconds // 60
        seconds = seconds % 60
        if minutes > 99 or seconds > 99:
            return None
        if minutes == 0:
            return f"{seconds}"
        return f"{minutes:02}{seconds:02}"

    min_cost = float('inf')
    for minutes in range(100):
        for seconds in range(100):
            if minutes * 60 + seconds == targetSeconds:
                time_str = format_time(minutes * 60 + seconds)
                if time_str:
                    digits = [int(d) for d in time_str]
                    min_cost = min(min_cost, calculate_cost(startAt, digits))
    return min_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startAt = 1
    moveCost = 2
    pushCost = 1
    targetSeconds = 600
    print(minCostSetTime(startAt, moveCost, pushCost, targetSeconds))  # Expected Output: 6

    # Test Case 2
    startAt = 0
    moveCost = 1
    pushCost = 2
    targetSeconds = 800
    print(minCostSetTime(startAt, moveCost, pushCost, targetSeconds))  # Expected Output: 8

    # Test Case 3
    startAt = 5
    moveCost = 3
    pushCost = 2
    targetSeconds = 100
    print(minCostSetTime(startAt, moveCost, pushCost, targetSeconds))  # Expected Output: 6

"""
Time Complexity:
- The outer loop iterates over 100 possible minute values.
- The inner loop iterates over 100 possible second values.
- For each valid combination, we calculate the cost of pressing the digits, which takes O(d) time, 
  where d is the number of digits (at most 4).
- Thus, the overall time complexity is O(100 * 100 * 4) = O(10,000).

Space Complexity:
- The space complexity is O(1) since we only use a constant amount of extra space.

Topic: Greedy, Simulation
"""