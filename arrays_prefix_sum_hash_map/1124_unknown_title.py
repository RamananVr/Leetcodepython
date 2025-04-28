"""
LeetCode Problem #1124: Longest Well-Performing Interval

Problem Statement:
We are given hours, a list of integers representing the number of hours worked per day for a given employee. 
A day is considered a "tiring day" if the number of hours worked is greater than 8, and a "non-tiring day" otherwise.

A well-performing interval is an interval (i, j) such that the number of tiring days in the interval is strictly 
greater than the number of non-tiring days in the interval.

Return the length of the longest well-performing interval.

Constraints:
- 1 <= len(hours) <= 10^4
- 0 <= hours[i] <= 16
"""

# Solution
def longestWPI(hours):
    """
    This function calculates the length of the longest well-performing interval.
    
    :param hours: List[int] - List of hours worked per day
    :return: int - Length of the longest well-performing interval
    """
    score = 0
    score_map = {}
    max_length = 0

    for i, h in enumerate(hours):
        # Update the score: +1 for tiring day, -1 for non-tiring day
        score += 1 if h > 8 else -1

        # If the score is positive, the interval from the start to the current day is well-performing
        if score > 0:
            max_length = i + 1
        else:
            # If the score is not positive, check if we have seen (score - 1) before
            if score - 1 in score_map:
                max_length = max(max_length, i - score_map[score - 1])
            
            # Record the first occurrence of the current score
            if score not in score_map:
                score_map[score] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    hours1 = [9, 9, 6, 0, 6, 6, 9]
    print("Test Case 1:", longestWPI(hours1))  # Expected Output: 3

    # Test Case 2
    hours2 = [6, 6, 6]
    print("Test Case 2:", longestWPI(hours2))  # Expected Output: 0

    # Test Case 3
    hours3 = [9, 6, 9]
    print("Test Case 3:", longestWPI(hours3))  # Expected Output: 3

    # Test Case 4
    hours4 = [10, 8, 9, 6, 7, 9, 10]
    print("Test Case 4:", longestWPI(hours4))  # Expected Output: 5

    # Test Case 5
    hours5 = [8, 8, 8, 8, 9, 9, 9, 9]
    print("Test Case 5:", longestWPI(hours5))  # Expected Output: 4

"""
Time Complexity Analysis:
- The algorithm iterates through the `hours` list once, performing constant-time operations for each element.
- Thus, the time complexity is O(n), where n is the length of the `hours` list.

Space Complexity Analysis:
- The algorithm uses a dictionary (`score_map`) to store scores, which in the worst case can have up to n entries.
- Thus, the space complexity is O(n).

Topic: Arrays, Prefix Sum, Hash Map
"""