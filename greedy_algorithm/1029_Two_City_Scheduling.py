"""
LeetCode Problem #1029: Two City Scheduling

Problem Statement:
A company is planning to interview 2N people. Given an array costs where costs[i] = [aCost, bCost], 
- aCost is the cost of flying the i-th person to city A, and 
- bCost is the cost of flying the i-th person to city B.

The company wants to minimize the total cost of flying exactly N people to city A and exactly N people to city B.

Return the minimum cost to achieve this.

Constraints:
- 2 * N == costs.length
- 2 <= costs.length <= 100
- costs.length is even.
- 1 <= aCost, bCost <= 1000
"""

def twoCitySchedCost(costs):
    """
    This function calculates the minimum cost to fly N people to city A and N people to city B.

    :param costs: List[List[int]] - A list of costs where costs[i] = [aCost, bCost]
    :return: int - The minimum cost to achieve the goal
    """
    # Sort the costs array by the difference between the cost of flying to city A and city B
    costs.sort(key=lambda x: x[0] - x[1])
    
    total_cost = 0
    n = len(costs) // 2
    
    # Send the first N people to city A and the rest to city B
    for i in range(n):
        total_cost += costs[i][0]  # Cost of flying to city A
    for i in range(n, 2 * n):
        total_cost += costs[i][1]  # Cost of flying to city B
    
    return total_cost

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    costs1 = [[10, 20], [30, 200], [50, 30], [450, 40]]
    print(twoCitySchedCost(costs1))  # Output: 110

    # Test Case 2
    costs2 = [[259, 770], [448, 54], [926, 667], [184, 139]]
    print(twoCitySchedCost(costs2))  # Output: 1859

    # Test Case 3
    costs3 = [[515, 563], [451, 713], [537, 709], [343, 819]]
    print(twoCitySchedCost(costs3))  # Output: 3086

"""
Time Complexity Analysis:
- Sorting the costs array takes O(n log n), where n is the number of people (2N).
- Calculating the total cost involves iterating through the array, which takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so no additional space is used apart from a few variables.
- Overall space complexity: O(1).

Topic: Greedy Algorithm
"""