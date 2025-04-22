"""
LeetCode Problem #765: Couples Holding Hands

Problem Statement:
There are `n` couples sitting in `2n` seats arranged in a row and want to hold hands. 
The people and seats are represented by an integer array `row` where `row[i]` is the 
ID of the person sitting in the `i-th` seat. The couples are numbered in order, the 
first couple being (0, 1), the second couple being (2, 3), and so on with the last 
couple being (2n-2, 2n-1).

Return the minimum number of swaps required so that every couple is sitting side by side.

Constraints:
- `2 <= row.length <= 60`
- `row.length` is even.
- `0 <= row[i] < row.length`
- All `row[i]` are unique.

Example:
Input: row = [0, 2, 1, 3]
Output: 1
Explanation: We only need to swap the second (row[1]) and third (row[2]) person.

Input: row = [3, 2, 0, 1]
Output: 0
Explanation: All couples are already seated side by side.
"""

def minSwapsCouples(row):
    """
    Function to calculate the minimum number of swaps required to seat all couples together.
    
    :param row: List[int] - The seating arrangement of people.
    :return: int - Minimum number of swaps required.
    """
    n = len(row)
    # Create a mapping of person to their current index in the row
    position = {person: i for i, person in enumerate(row)}
    swaps = 0

    for i in range(0, n, 2):
        first_person = row[i]
        # Find the partner of the first person
        partner = first_person ^ 1  # XOR with 1 flips the last bit (0 <-> 1, 2 <-> 3, etc.)
        
        # If the partner is not already next to the first person
        if row[i + 1] != partner:
            swaps += 1
            # Find the current index of the partner
            partner_index = position[partner]
            
            # Swap the partner with the person sitting next to the first person
            row[i + 1], row[partner_index] = row[partner_index], row[i + 1]
            
            # Update the position mapping after the swap
            position[row[partner_index]] = partner_index
            position[row[i + 1]] = i + 1

    return swaps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    row1 = [0, 2, 1, 3]
    print("Test Case 1 Output:", minSwapsCouples(row1))  # Expected Output: 1

    # Test Case 2
    row2 = [3, 2, 0, 1]
    print("Test Case 2 Output:", minSwapsCouples(row2))  # Expected Output: 0

    # Test Case 3
    row3 = [5, 4, 2, 6, 3, 1, 0, 7]
    print("Test Case 3 Output:", minSwapsCouples(row3))  # Expected Output: 2

    # Test Case 4
    row4 = [1, 0, 3, 2, 5, 4, 7, 6]
    print("Test Case 4 Output:", minSwapsCouples(row4))  # Expected Output: 0

"""
Time Complexity Analysis:
- Constructing the `position` dictionary takes O(n) time.
- The loop iterates over half the array (n/2 iterations), and each iteration involves 
  constant-time operations (finding indices, swapping, and updating the dictionary).
- Overall time complexity: O(n).

Space Complexity Analysis:
- The `position` dictionary requires O(n) space to store the mapping of person to index.
- Overall space complexity: O(n).

Topic: Arrays, Greedy
"""