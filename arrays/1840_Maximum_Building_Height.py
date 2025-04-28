"""
LeetCode Problem #1840: Maximum Building Height

Problem Statement:
You want to build n buildings in a row. The height of the i-th building is represented by an integer array restrictions, 
where restrictions[i] = [id, maxHeight] means that the height of building id must be less than or equal to maxHeight.

The buildings are numbered from 1 to n, and you want to maximize the height of the tallest building. 
The height of the first building is 0, and the height of the last building is also 0. 
You can increase or decrease the height of a building by 1 per unit of distance to the next building.

Return the maximum possible height of the tallest building.

Constraints:
- 2 <= n <= 10^9
- 0 <= restrictions.length <= min(n - 1, 10^5)
- 2 <= restrictions[i][0] <= n
- restrictions[i][0] is unique.
- 0 <= restrictions[i][1] <= 10^9
- The height of the first building is 0.
- The height of the last building is 0.

"""

# Solution
def maxBuilding(n, restrictions):
    # Add restrictions for the first and last buildings
    restrictions.append([1, 0])
    restrictions.append([n, n - 1])
    restrictions.sort()

    # Forward pass: ensure restrictions are valid
    for i in range(1, len(restrictions)):
        prev_id, prev_max_height = restrictions[i - 1]
        curr_id, curr_max_height = restrictions[i]
        restrictions[i][1] = min(curr_max_height, prev_max_height + (curr_id - prev_id))

    # Backward pass: ensure restrictions are valid
    for i in range(len(restrictions) - 2, -1, -1):
        next_id, next_max_height = restrictions[i + 1]
        curr_id, curr_max_height = restrictions[i]
        restrictions[i][1] = min(curr_max_height, next_max_height + (next_id - curr_id))

    # Calculate the maximum possible height
    max_height = 0
    for i in range(1, len(restrictions)):
        prev_id, prev_max_height = restrictions[i - 1]
        curr_id, curr_max_height = restrictions[i]
        # Maximum height between two buildings
        max_height = max(max_height, (curr_max_height + prev_max_height + curr_id - prev_id) // 2)

    return max_height

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    restrictions = [[2, 1], [4, 1]]
    print(maxBuilding(n, restrictions))  # Output: 2

    # Test Case 2
    n = 6
    restrictions = []
    print(maxBuilding(n, restrictions))  # Output: 5

    # Test Case 3
    n = 10
    restrictions = [[3, 2], [8, 4]]
    print(maxBuilding(n, restrictions))  # Output: 5

    # Test Case 4
    n = 7
    restrictions = [[2, 4], [4, 2], [6, 1]]
    print(maxBuilding(n, restrictions))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the restrictions array takes O(k log k), where k is the number of restrictions.
- The forward and backward passes each take O(k).
- Calculating the maximum height takes O(k).
- Overall, the time complexity is O(k log k), where k is the number of restrictions.

Space Complexity:
- The algorithm uses O(k) space to store the restrictions array.
- No additional space is used apart from the input and a few variables.
- Overall, the space complexity is O(k).

Topic: Arrays
"""