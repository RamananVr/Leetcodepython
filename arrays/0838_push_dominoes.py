"""
LeetCode Question #838: Push Dominoes

Problem Statement:
There are `n` dominoes in a line, and each domino can be pushed to the left, to the right, or remain upright. 
We represent these states as 'L', 'R', and '.', respectively. Each domino that is pushed will push the next 
domino that is upright in the same direction.

When a vertical domino has dominoes pushing it from both sides, it stays upright because the forces cancel out.

Given a string `dominoes` representing the initial state of the dominoes, return a string representing the final state.

Example 1:
Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first dominoes are already falling to the right, and the last dominoes are standing upright.

Example 2:
Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."

Constraints:
- `1 <= dominoes.length <= 10^5`
- `dominoes[i]` is either 'L', 'R', or '.'.
"""

# Solution
def pushDominoes(dominoes: str) -> str:
    n = len(dominoes)
    forces = [0] * n

    # Calculate forces from the right
    force = 0
    for i in range(n):
        if dominoes[i] == 'R':
            force = n  # Apply maximum force
        elif dominoes[i] == 'L':
            force = 0  # Reset force
        else:
            force = max(force - 1, 0)  # Gradually decrease force
        forces[i] += force

    # Calculate forces from the left
    force = 0
    for i in range(n - 1, -1, -1):
        if dominoes[i] == 'L':
            force = n  # Apply maximum force
        elif dominoes[i] == 'R':
            force = 0  # Reset force
        else:
            force = max(force - 1, 0)  # Gradually decrease force
        forces[i] -= force

    # Determine final state based on net forces
    result = []
    for f in forces:
        if f > 0:
            result.append('R')
        elif f < 0:
            result.append('L')
        else:
            result.append('.')

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dominoes = "RR.L"
    print(pushDominoes(dominoes))  # Output: "RR.L"

    # Test Case 2
    dominoes = ".L.R...LR..L.."
    print(pushDominoes(dominoes))  # Output: "LL.RR.LLRRLL.."

    # Test Case 3
    dominoes = "R...L"
    print(pushDominoes(dominoes))  # Output: "RR.LL"

    # Test Case 4
    dominoes = "R.....L"
    print(pushDominoes(dominoes))  # Output: "RRRRLLL"

    # Test Case 5
    dominoes = "R.L"
    print(pushDominoes(dominoes))  # Output: "R.L"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm involves two passes over the `dominoes` string (one for calculating forces from the right and one for calculating forces from the left).
- Each pass is O(n), where `n` is the length of the string.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses an auxiliary array `forces` of size `n` to store the net forces acting on each domino.
- Therefore, the space complexity is O(n).

Topic: Arrays
"""