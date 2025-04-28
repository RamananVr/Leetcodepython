"""
LeetCode Problem #1494: Parallel Courses II

Problem Statement:
You are given an integer n, which indicates that there are n courses labeled from 1 to n. 
You are also given an array dependencies where dependencies[i] = [xi, yi] indicates that 
you must take course xi before you can take course yi. Additionally, you are given an 
integer k.

In one semester, you can take at most k courses as long as you have taken all the 
prerequisite courses for the courses you are taking.

Return the minimum number of semesters needed to take all courses. If there is no way to 
take all the courses, return -1.

Constraints:
- 1 <= n <= 15
- 1 <= k <= n
- 0 <= dependencies.length <= n * (n - 1) / 2
- dependencies[i].length == 2
- 1 <= xi, yi <= n
- xi != yi
- All prerequisite relationships are distinct, i.e., no duplicate dependencies.

"""

from collections import defaultdict
from functools import lru_cache

def minNumberOfSemesters(n: int, dependencies: list[list[int]], k: int) -> int:
    # Step 1: Build the prerequisite graph
    prereq = [0] * n
    for x, y in dependencies:
        prereq[y - 1] |= 1 << (x - 1)

    # Step 2: Use bitmask DP to solve the problem
    @lru_cache(None)
    def dp(mask):
        if mask == (1 << n) - 1:  # All courses are taken
            return 0

        # Find all courses that can be taken in the current state
        available = []
        for i in range(n):
            if (mask & (1 << i)) == 0 and (mask & prereq[i]) == prereq[i]:
                available.append(i)

        # If the number of available courses is less than or equal to k, take all of them
        if len(available) <= k:
            new_mask = mask
            for course in available:
                new_mask |= 1 << course
            return 1 + dp(new_mask)

        # Otherwise, try all combinations of k courses from the available courses
        min_semesters = float('inf')
        for subset in combinations(available, k):
            new_mask = mask
            for course in subset:
                new_mask |= 1 << course
            min_semesters = min(min_semesters, 1 + dp(new_mask))

        return min_semesters

    # Helper function to generate combinations
    def combinations(courses, k):
        if k == 0:
            yield []
        elif len(courses) == 0:
            return
        else:
            for i in range(len(courses)):
                for rest in combinations(courses[i + 1:], k - 1):
                    yield [courses[i]]

    # Start the DP with an empty mask
    return dp(0)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    dependencies1 = [[2, 1], [3, 1], [1, 4]]
    k1 = 2
    print(minNumberOfSemesters(n1, dependencies1, k1))  # Expected Output: 3

    # Test Case 2
    n2 = 5
    dependencies2 = [[2, 1], [3, 1], [4, 1], [1, 5]]
    k2 = 2
    print(minNumberOfSemesters(n2, dependencies2, k2))  # Expected Output: 4

    # Test Case 3
    n3 = 11
    dependencies3 = []
    k3 = 2
    print(minNumberOfSemesters(n3, dependencies3, k3))  # Expected Output: 6


"""
Time and Space Complexity Analysis:

Time Complexity:
- The total number of states in the DP is 2^n (all possible subsets of courses).
- For each state, we iterate over all available courses and generate combinations of size k.
- Generating combinations of size k from a set of size m takes O(m choose k), which is bounded by O(m^k).
- Thus, the overall time complexity is O(2^n * n^k), where n is the number of courses.

Space Complexity:
- The space complexity is O(2^n) for the DP cache and O(n) for the recursion stack.
- Thus, the total space complexity is O(2^n).

Topic: Dynamic Programming (DP), Bitmasking
"""