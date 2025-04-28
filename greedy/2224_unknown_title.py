"""
LeetCode Problem #2224: Minimum Number of Operations to Convert Time

Problem Statement:
You are given two strings `current` and `correct` representing two 24-hour times.

24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. 
The earliest 24-hour time is 00:00, and the latest is 23:59.

In one operation, you can increase the time `current` by 1, 5, 15, or 60 minutes. 
You can perform this operation any number of times.

Return the minimum number of operations needed to convert `current` to `correct`.

Example 1:
Input: current = "02:30", correct = "04:35"
Output: 3
Explanation:
- Add 60 minutes twice (02:30 -> 03:30 -> 04:30).
- Add 5 minutes once (04:30 -> 04:35).
Total operations = 3.

Example 2:
Input: current = "11:00", correct = "11:01"
Output: 1
Explanation:
- Add 1 minute once (11:00 -> 11:01).
Total operations = 1.

Example 3:
Input: current = "23:59", correct = "00:00"
Output: 1
Explanation:
- Add 1 minute once (23:59 -> 00:00).
Total operations = 1.

Constraints:
- `current` and `correct` are in the format "HH:MM".
- `current` <= `correct` (time is always moving forward).
"""

def convertTime(current: str, correct: str) -> int:
    # Convert both times to minutes
    current_minutes = int(current[:2]) * 60 + int(current[3:])
    correct_minutes = int(correct[:2]) * 60 + int(correct[3:])
    
    # Calculate the difference in minutes
    diff = correct_minutes - current_minutes
    
    # Initialize the number of operations
    operations = 0
    
    # List of possible increments in descending order
    increments = [60, 15, 5, 1]
    
    # Use the largest increments first to minimize operations
    for inc in increments:
        operations += diff // inc
        diff %= inc
    
    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    current = "02:30"
    correct = "04:35"
    print(f"Test Case 1: {convertTime(current, correct)}")  # Expected Output: 3

    # Test Case 2
    current = "11:00"
    correct = "11:01"
    print(f"Test Case 2: {convertTime(current, correct)}")  # Expected Output: 1

    # Test Case 3
    current = "23:59"
    correct = "00:00"
    print(f"Test Case 3: {convertTime(current, correct)}")  # Expected Output: 1

    # Test Case 4
    current = "00:00"
    correct = "01:00"
    print(f"Test Case 4: {convertTime(current, correct)}")  # Expected Output: 1

    # Test Case 5
    current = "12:34"
    correct = "13:45"
    print(f"Test Case 5: {convertTime(current, correct)}")  # Expected Output: 3

"""
Time Complexity Analysis:
- Converting the time strings to minutes takes O(1) time.
- Calculating the difference and iterating over the increments list takes O(1) time.
- Overall, the time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of extra space for variables and the increments list.
- Overall, the space complexity is O(1).

Topic: Greedy
"""