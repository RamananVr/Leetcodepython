"""
LeetCode Problem #1402: Reducing Dishes

Problem Statement:
A chef has collected data on the satisfaction level of his n dishes. Chef can cook any dish in 1 unit of time.

- Like-time coefficient of a dish is defined as the time taken to cook that dish multiplied by its satisfaction level, i.e., time[i] * satisfaction[i].
- Return the maximum sum of like-time coefficient that the chef can obtain after dishes are prepared optimally.

The chef can discard some dishes to reduce the total time spent. In other words, the chef can choose the order of dishes in which they are prepared and only cook a subset of dishes.

Constraints:
- n == satisfaction.length
- 1 <= n <= 500
- -10^3 <= satisfaction[i] <= 10^3
"""

# Solution
def maxSatisfaction(satisfaction):
    """
    Calculate the maximum sum of like-time coefficient that the chef can obtain.

    :param satisfaction: List[int] - List of satisfaction levels of dishes
    :return: int - Maximum like-time coefficient
    """
    # Sort the satisfaction levels in descending order
    satisfaction.sort(reverse=True)
    
    max_sum = 0
    current_sum = 0
    
    # Iterate through the sorted satisfaction levels
    for s in satisfaction:
        # Check if adding the current satisfaction level increases the total
        if current_sum + s > 0:
            current_sum += s
            max_sum += current_sum
        else:
            break
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    satisfaction = [-1, -8, 0, 5, -9]
    print(maxSatisfaction(satisfaction))  # Output: 14

    # Test Case 2
    satisfaction = [4, 3, 2]
    print(maxSatisfaction(satisfaction))  # Output: 20

    # Test Case 3
    satisfaction = [-1, -4, -5]
    print(maxSatisfaction(satisfaction))  # Output: 0

    # Test Case 4
    satisfaction = [1, 2, 3, -1, -2, -3]
    print(maxSatisfaction(satisfaction))  # Output: 20

    # Test Case 5
    satisfaction = [0, 0, 0]
    print(maxSatisfaction(satisfaction))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the satisfaction array takes O(n log n), where n is the number of dishes.
- Iterating through the sorted array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space as it modifies the input array in place and uses a few variables.
- Overall space complexity: O(1).

Topic: Greedy Algorithm
"""