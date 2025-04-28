"""
LeetCode Problem #1944: Number of Visible People in a Queue

Problem Statement:
There are n people standing in a queue, and they numbered from 0 to n - 1 in left to right order. 
You are given an array heights of distinct integers where heights[i] represents the height of the ith person.

A person can see another person to their right in the queue if everybody in between is shorter than both of them. 
More formally, the ith person can see the jth person if i < j and min(heights[i], heights[j]) > max(heights[i+1], heights[i+2], ..., heights[j-1]).

Return an array answer of length n where answer[i] is the number of people the ith person can see to their right in the queue.

Example 1:
Input: heights = [10, 6, 8, 5, 11, 9]
Output: [3, 1, 2, 1, 1, 0]
Explanation:
- Person 0 can see person 1, 2, and 4. 
- Person 1 can see person 2.
- Person 2 can see person 3 and 4.
- Person 3 can see person 4.
- Person 4 can see person 5.
- Person 5 can see no one.

Example 2:
Input: heights = [5, 1, 2, 3, 10]
Output: [4, 1, 1, 1, 0]

Constraints:
- n == heights.length
- 1 <= n <= 10^5
- 1 <= heights[i] <= 10^5
- All the values of heights are unique.
"""

# Solution
def canSeePersonsCount(heights):
    """
    This function calculates the number of people each person in the queue can see to their right.
    It uses a monotonic decreasing stack to efficiently determine visibility.
    """
    n = len(heights)
    answer = [0] * n
    stack = []

    for i in range(n - 1, -1, -1):
        # Pop all shorter people from the stack
        while stack and stack[-1] < heights[i]:
            stack.pop()
            answer[i] += 1
        # If the stack is not empty, the current person can see one more person
        if stack:
            answer[i] += 1
        # Push the current height onto the stack
        stack.append(heights[i])

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights1 = [10, 6, 8, 5, 11, 9]
    print(canSeePersonsCount(heights1))  # Output: [3, 1, 2, 1, 1, 0]

    # Test Case 2
    heights2 = [5, 1, 2, 3, 10]
    print(canSeePersonsCount(heights2))  # Output: [4, 1, 1, 1, 0]

    # Test Case 3
    heights3 = [1, 2, 3, 4, 5]
    print(canSeePersonsCount(heights3))  # Output: [4, 3, 2, 1, 0]

    # Test Case 4
    heights4 = [5, 4, 3, 2, 1]
    print(canSeePersonsCount(heights4))  # Output: [1, 1, 1, 1, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each person is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the heights array.

Space Complexity:
- The stack stores at most n elements, so the space complexity is O(n).
"""

# Topic: Monotonic Stack