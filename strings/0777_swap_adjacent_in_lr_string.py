"""
LeetCode Question #777: Swap Adjacent in LR String

Problem Statement:
In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either:
- Swapping the positions of one occurrence of "XL" with "LX", or
- Swapping the positions of one occurrence of "RX" with "XR".

Given the starting string `start` and the ending string `end`, return `True` if and only if there exists a sequence of moves to transform one string into the other. Otherwise, return `False`.

Constraints:
- `1 <= len(start) == len(end) <= 10^4`
- Both `start` and `end` will only consist of characters 'L', 'R', and 'X'.
"""

def canTransform(start: str, end: str) -> bool:
    """
    Determines if the string `start` can be transformed into the string `end` 
    by following the rules of swapping "XL" with "LX" and "RX" with "XR".
    """
    # Step 1: Check if the strings have the same non-X characters in the same order
    if start.replace('X', '') != end.replace('X', ''):
        return False

    # Step 2: Check the relative positions of 'L' and 'R'
    # L can only move left, and R can only move right
    start_L_positions = [i for i, c in enumerate(start) if c == 'L']
    end_L_positions = [i for i, c in enumerate(end) if c == 'L']
    start_R_positions = [i for i, c in enumerate(start) if c == 'R']
    end_R_positions = [i for i, c in enumerate(end) if c == 'R']

    # Check if L in `start` is always to the right of its corresponding position in `end`
    for s, e in zip(start_L_positions, end_L_positions):
        if s < e:
            return False

    # Check if R in `start` is always to the left of its corresponding position in `end`
    for s, e in zip(start_R_positions, end_R_positions):
        if s > e:
            return False

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic transformation
    start = "RXXLRXRXL"
    end = "XRLXXRRLX"
    print(canTransform(start, end))  # Expected: True

    # Test Case 2: No transformation possible
    start = "X"
    end = "L"
    print(canTransform(start, end))  # Expected: False

    # Test Case 3: Same strings
    start = "XXRXXLXX"
    end = "XXRXXLXX"
    print(canTransform(start, end))  # Expected: True

    # Test Case 4: L moves left, R moves right
    start = "RLX"
    end = "XLR"
    print(canTransform(start, end))  # Expected: True

    # Test Case 5: Invalid transformation due to order mismatch
    start = "RXL"
    end = "LXR"
    print(canTransform(start, end))  # Expected: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Replacing 'X' in both `start` and `end` takes O(n), where n is the length of the strings.
- Extracting positions of 'L' and 'R' takes O(n).
- Comparing positions of 'L' and 'R' takes O(n).
Overall, the time complexity is O(n).

Space Complexity:
- The space used for storing positions of 'L' and 'R' is O(n).
- The space used for the intermediate strings after replacing 'X' is O(n).
Overall, the space complexity is O(n).

Topic: Strings
"""