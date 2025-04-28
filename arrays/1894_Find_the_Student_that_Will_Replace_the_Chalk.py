"""
LeetCode Problem #1894: Find the Student that Will Replace the Chalk

Problem Statement:
There are `n` students in a class numbered from `0` to `n - 1`. The teacher will give each student a problem to solve sequentially, starting from student `0`, and will repeat the process starting from student `0` again once the teacher reaches the last student.

You are given a 0-indexed integer array `chalk` and an integer `k`. The `chalk[i]` denotes the amount of chalk the `i-th` student will use to solve a problem. Initially, there is `k` amount of chalk. Return the index of the student that will replace the chalk after it runs out.

Example:
Input: chalk = [5, 1, 5], k = 22
Output: 0
Explanation: The students go in a cycle:
- Student 0 uses 5 chalk, so k = 17.
- Student 1 uses 1 chalk, so k = 16.
- Student 2 uses 5 chalk, so k = 11.
- Student 0 uses 5 chalk, so k = 6.
- Student 1 uses 1 chalk, so k = 5.
- Student 2 uses 5 chalk, so k = 0.
Student 0 will replace the chalk.

Constraints:
- `chalk.length == n`
- `1 <= n <= 10^4`
- `1 <= chalk[i] <= 10^4`
- `1 <= k <= 10^9`
"""

# Solution
def chalkReplacer(chalk, k):
    # Step 1: Calculate the total chalk required for one full cycle
    total_chalk = sum(chalk)
    
    # Step 2: Reduce k modulo total_chalk to avoid unnecessary cycles
    k %= total_chalk
    
    # Step 3: Find the student who will replace the chalk
    for i, chalk_needed in enumerate(chalk):
        if k < chalk_needed:
            return i
        k -= chalk_needed

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    chalk = [5, 1, 5]
    k = 22
    print(chalkReplacer(chalk, k))  # Output: 0

    # Test Case 2
    chalk = [3, 4, 1, 2]
    k = 25
    print(chalkReplacer(chalk, k))  # Output: 1

    # Test Case 3
    chalk = [1, 2, 3]
    k = 7
    print(chalkReplacer(chalk, k))  # Output: 0

    # Test Case 4
    chalk = [10, 20, 30]
    k = 100
    print(chalkReplacer(chalk, k))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the total chalk required for one cycle takes O(n), where n is the length of the chalk array.
- Reducing k modulo total_chalk is an O(1) operation.
- Iterating through the chalk array to find the student takes O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""