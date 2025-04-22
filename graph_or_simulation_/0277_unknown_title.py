"""
LeetCode Problem #277: Find the Celebrity

Problem Statement:
Suppose you are at a party with `n` people (labeled from 0 to n - 1), and among them, there may exist one celebrity. 
The definition of a celebrity is that all the other `n - 1` people know the celebrity, but the celebrity does not know any of them.

You are given a helper function `knows(a: int, b: int) -> bool` which tells you whether person `a` knows person `b`. 
Implement a function `findCelebrity(n: int) -> int`.

The function should return the label of the celebrity if there is a celebrity in the party. If there is no celebrity, return -1.

Constraints:
- The helper function `knows(a, b)` is provided and can be called to check if person `a` knows person `b`.
- You must minimize the number of calls to the `knows` function.
- Time complexity should be O(n).
- Space complexity should be O(1).

"""

# Clean and Correct Python Solution
def findCelebrity(n: int) -> int:
    # Step 1: Find a potential celebrity
    candidate = 0
    for i in range(1, n):
        if knows(candidate, i):
            candidate = i

    # Step 2: Verify if the candidate is a celebrity
    for i in range(n):
        if i != candidate:
            if knows(candidate, i) or not knows(i, candidate):
                return -1

    return candidate

# Example Test Cases
def knows(a: int, b: int) -> bool:
    """
    Mock implementation of the knows function for testing purposes.
    Replace this with the actual knows function in a real scenario.
    """
    # Example: Person 2 is the celebrity
    celebrity = 2
    if a == celebrity:
        return False  # Celebrity knows no one
    if b == celebrity:
        return True  # Everyone knows the celebrity
    return False  # Other relationships

if __name__ == "__main__":
    # Test Case 1: Celebrity exists
    n = 4
    print(findCelebrity(n))  # Output: 2

    # Test Case 2: No celebrity
    def knows(a: int, b: int) -> bool:
        # Example: No celebrity in this case
        return False
    n = 3
    print(findCelebrity(n))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Step 1: The first loop runs `n - 1` times to find the potential celebrity. Each iteration makes one call to `knows`, so this step takes O(n) time.
- Step 2: The second loop runs `n` times to verify the candidate. Each iteration makes at most two calls to `knows`, so this step also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (only a few variables), so the space complexity is O(1).

Topic: Graph (or Simulation)
"""