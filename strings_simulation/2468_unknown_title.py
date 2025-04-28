"""
LeetCode Problem #2468: Split Message Based on Limit

Problem Statement:
You are given a string `message` and an integer `limit`. You need to split the `message` into parts such that:
1. Each part is of the form "<part>/<total>", where:
   - `<part>` is the 1-based index of the part.
   - `<total>` is the total number of parts.
2. The length of each part (including the "<part>/<total>" suffix) does not exceed `limit`.
3. The parts should be as evenly distributed as possible.

Return the list of parts if it is possible to split the message under the given constraints. Otherwise, return an empty list.

Constraints:
- `1 <= len(message) <= 10^4`
- `1 <= limit <= 100`

Example:
Input: message = "This is a test message", limit = 10
Output: ["This is a", "test", "message"]

Input: message = "Short", limit = 5
Output: []

"""

def splitMessage(message: str, limit: int) -> list:
    """
    Splits the message into parts based on the given limit.

    Args:
    - message (str): The input message to split.
    - limit (int): The maximum length of each part including the suffix.

    Returns:
    - list: A list of parts if splitting is possible, otherwise an empty list.
    """
    # Helper function to calculate the length of the suffix "<part>/<total>"
    def suffix_length(part: int, total: int) -> int:
        return len(str(part)) + len(str(total)) + 2  # "<part>/<total>" has 2 extra characters for '/' and '<>'

    # Determine the total number of parts
    n = len(message)
    for total_parts in range(1, n + 1):
        # Calculate the total length of all suffixes
        total_suffix_length = sum(suffix_length(part, total_parts) for part in range(1, total_parts + 1))
        # Calculate the remaining length for the actual message content
        remaining_length = n - (limit * total_parts - total_suffix_length)
        if remaining_length <= 0:
            break
    else:
        return []  # If no valid total_parts is found, return an empty list

    # Split the message into parts
    parts = []
    current_index = 0
    for part in range(1, total_parts + 1):
        suffix = f"<{part}/{total_parts}>"
        available_length = limit - len(suffix)
        part_content = message[current_index:current_index + available_length]
        parts.append(part_content + suffix)
        current_index += available_length

    return parts


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    message1 = "This is a test message"
    limit1 = 10
    print(splitMessage(message1, limit1))  # Expected: ["This is a", "test", "message"]

    # Test Case 2
    message2 = "Short"
    limit2 = 5
    print(splitMessage(message2, limit2))  # Expected: []

    # Test Case 3
    message3 = "HelloWorld"
    limit3 = 15
    print(splitMessage(message3, limit3))  # Expected: ["HelloWorld<1/1>"]

    # Test Case 4
    message4 = "Split this message into parts"
    limit4 = 12
    print(splitMessage(message4, limit4))  # Expected: ["Split thi<1/3>", "s messag<2/3>", "e into p<3/3>"]

    # Test Case 5
    message5 = "A very long message that needs to be split into multiple parts"
    limit5 = 20
    print(splitMessage(message5, limit5))  # Expected: ["A very long messa<1/5>", "ge that needs t<2/5>", "o be split int<3/5>", "o multiple par<4/5>", "ts<5/5>"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the total number of parts involves iterating over possible values of `total_parts` (up to `n`).
- For each `total_parts`, we calculate the total suffix length, which involves iterating over the range of parts.
- In the worst case, this results in O(n^2) complexity.

Space Complexity:
- The space complexity is O(n) for storing the resulting list of parts.

Overall:
- Time Complexity: O(n^2)
- Space Complexity: O(n)
"""

# Topic: Strings, Simulation