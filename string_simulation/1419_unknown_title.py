"""
LeetCode Problem #1419: Minimum Number of Frogs Croaking

Problem Statement:
You are given the string `croakOfFrogs`, which represents a combination of the string "croak" from different frogs, that is, multiple frogs can croak at the same time, so `croakOfFrogs` can be thought of as a concatenation of these croaks.

Return the minimum number of different frogs required to produce the string `croakOfFrogs`. If the string is not a valid combination of "croak" from different frogs, return -1.

A string is a valid combination of "croak" from different frogs if and only if:
- The string can be formed by concatenating one or more "croak" strings.
- Each "croak" must be completed in the correct order: 'c', 'r', 'o', 'a', 'k'.

Constraints:
- `1 <= croakOfFrogs.length <= 10^5`
- `croakOfFrogs` consists of the characters 'c', 'r', 'o', 'a', and 'k'.

"""

def minNumberOfFrogs(croakOfFrogs: str) -> int:
    # Initialize counters for each character in "croak"
    counts = {'c': 0, 'r': 0, 'o': 0, 'a': 0, 'k': 0}
    max_frogs = 0  # Maximum number of frogs needed at any point
    active_frogs = 0  # Frogs currently croaking

    for char in croakOfFrogs:
        if char not in counts:
            return -1  # Invalid character in the string

        counts[char] += 1

        # Check the order of "croak"
        if char == 'c':
            active_frogs += 1
            max_frogs = max(max_frogs, active_frogs)
        elif char == 'r':
            if counts['r'] > counts['c']:
                return -1
        elif char == 'o':
            if counts['o'] > counts['r']:
                return -1
        elif char == 'a':
            if counts['a'] > counts['o']:
                return -1
        elif char == 'k':
            if counts['k'] > counts['a']:
                return -1
            active_frogs -= 1  # A frog finishes croaking

    # Ensure all frogs have completed their croak
    if counts['c'] != counts['r'] or counts['r'] != counts['o'] or counts['o'] != counts['a'] or counts['a'] != counts['k']:
        return -1

    return max_frogs


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid croak sequence
    croakOfFrogs = "croakcroak"
    print(minNumberOfFrogs(croakOfFrogs))  # Output: 1

    # Test Case 2: Overlapping croak sequences
    croakOfFrogs = "crcoakroak"
    print(minNumberOfFrogs(croakOfFrogs))  # Output: 2

    # Test Case 3: Invalid sequence
    croakOfFrogs = "croakcrook"
    print(minNumberOfFrogs(croakOfFrogs))  # Output: -1

    # Test Case 4: Single croak
    croakOfFrogs = "croak"
    print(minNumberOfFrogs(croakOfFrogs))  # Output: 1

    # Test Case 5: Empty string (edge case)
    croakOfFrogs = ""
    print(minNumberOfFrogs(croakOfFrogs))  # Output: -1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `croakOfFrogs` once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The function uses a dictionary `counts` to store counts for the five characters in "croak". This requires O(1) space since the dictionary size is fixed.
- Other variables (`max_frogs`, `active_frogs`) use O(1) space.
- Thus, the space complexity is O(1).

Topic: String, Simulation
"""