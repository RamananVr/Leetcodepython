"""
LeetCode Problem #1871: Jump Game VII

Problem Statement:
You are given a binary string `s` where `s[i]` is '0' or '1'. You are also given two integers `minJump` and `maxJump`.

In the beginning, you are standing at index 0, which is always '0'. You can move from index `i` to index `j` if the following conditions are met:
- `i + minJump <= j <= i + maxJump`
- `s[j] == '0'`

Return `true` if you can reach the last index of the string, or `false` otherwise.

Constraints:
- `2 <= s.length <= 10^5`
- `s[i]` is either '0' or '1'
- `s[0] == '0'`
- `1 <= minJump <= maxJump < s.length`
"""

from collections import deque

def canReach(s: str, minJump: int, maxJump: int) -> bool:
    """
    Determines if you can reach the last index of the binary string `s` 
    following the jump rules defined by `minJump` and `maxJump`.
    """
    n = len(s)
    if s[-1] == '1':  # If the last index is '1', it's impossible to reach
        return False

    queue = deque([0])  # Start BFS from index 0
    farthest = 0  # Tracks the farthest index we've processed

    while queue:
        current = queue.popleft()

        # Calculate the range of valid jumps from the current index
        start = max(current + minJump, farthest + 1)
        end = min(current + maxJump, n - 1)

        for next_index in range(start, end + 1):
            if s[next_index] == '0':  # Only consider valid '0' positions
                queue.append(next_index)
                if next_index == n - 1:  # If we reach the last index, return True
                    return True

        # Update the farthest processed index
        farthest = end

    return False


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "011010"
    minJump1 = 2
    maxJump1 = 3
    print(canReach(s1, minJump1, maxJump1))  # Expected Output: True

    # Test Case 2
    s2 = "01101110"
    minJump2 = 2
    maxJump2 = 3
    print(canReach(s2, minJump2, maxJump2))  # Expected Output: False

    # Test Case 3
    s3 = "0000000000"
    minJump3 = 2
    maxJump3 = 5
    print(canReach(s3, minJump3, maxJump3))  # Expected Output: True

    # Test Case 4
    s4 = "0000000001"
    minJump4 = 2
    maxJump4 = 5
    print(canReach(s4, minJump4, maxJump4))  # Expected Output: False


"""
Time Complexity Analysis:
- The algorithm processes each index of the string at most once.
- For each index, we calculate the range of valid jumps and iterate over it.
- In the worst case, the total number of iterations is proportional to the length of the string `n`.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is determined by the queue used for BFS.
- In the worst case, the queue can hold up to O(n) indices.
- Therefore, the space complexity is O(n).

Topic: Breadth-First Search (BFS), Sliding Window
"""