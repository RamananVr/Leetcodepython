"""
LeetCode Problem #1629: Slowest Key

Problem Statement:
A newly designed keypad was tested, where a tester pressed a sequence of n keys, one at a time.

You are given a string `keysPressed` of length n, where `keysPressed[i]` was the ith key pressed in the testing sequence, and a sorted list `releaseTimes`, where `releaseTimes[i]` was the time the ith key was released. Both arrays are 0-indexed. The `0th` key was pressed at the time 0, and every subsequent key was pressed at the exact time the previous key was released.

The duration of a key press is defined as the difference between the release time of the key and the release time of the previous key. The `0th` key's duration is equal to its release time.

Return the key of the keypress that had the longest duration. If there is a tie, return the lexicographically largest key of the keys pressed.

Constraints:
- `releaseTimes.length == n`
- `keysPressed.length == n`
- `2 <= n <= 1000`
- `1 <= releaseTimes[i] <= 10^9`
- `releaseTimes[i] < releaseTimes[i+1]`
- `keysPressed` contains only lowercase English letters.
"""

def slowestKey(releaseTimes, keysPressed):
    """
    Function to find the key with the longest duration.
    If there is a tie, the lexicographically largest key is returned.
    """
    n = len(releaseTimes)
    max_duration = releaseTimes[0]
    slowest_key = keysPressed[0]

    for i in range(1, n):
        duration = releaseTimes[i] - releaseTimes[i - 1]
        if duration > max_duration or (duration == max_duration and keysPressed[i] > slowest_key):
            max_duration = duration
            slowest_key = keysPressed[i]

    return slowest_key

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    releaseTimes1 = [9, 29, 49, 50]
    keysPressed1 = "cbcd"
    print(slowestKey(releaseTimes1, keysPressed1))  # Output: "c"

    # Test Case 2
    releaseTimes2 = [12, 23, 36, 46, 62]
    keysPressed2 = "spuda"
    print(slowestKey(releaseTimes2, keysPressed2))  # Output: "a"

    # Test Case 3
    releaseTimes3 = [1, 2, 3, 4, 5]
    keysPressed3 = "abcde"
    print(slowestKey(releaseTimes3, keysPressed3))  # Output: "e"

    # Test Case 4
    releaseTimes4 = [10, 20, 30, 40, 50]
    keysPressed4 = "aaaaa"
    print(slowestKey(releaseTimes4, keysPressed4))  # Output: "a"

"""
Time Complexity Analysis:
- The function iterates through the `releaseTimes` and `keysPressed` arrays once, making it O(n), where n is the length of the arrays.

Space Complexity Analysis:
- The function uses a constant amount of extra space, making the space complexity O(1).

Topic: Arrays
"""