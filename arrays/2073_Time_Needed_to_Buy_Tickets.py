"""
LeetCode Problem #2073: Time Needed to Buy Tickets

Problem Statement:
There are `n` people in a line, where the `0th` person is at the front of the line and the `(n - 1)th` person is at the back of the line. You are given a 0-indexed integer array `tickets` of length `n` where the number of tickets that the `ith` person needs is `tickets[i]`.

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and has to go to the end of the line (the back of the line) after buying a ticket. If a person does not need any more tickets, they will leave the line.

Return the time taken for the person at position `k` (0-indexed) to finish buying all their tickets.

Constraints:
- `n == tickets.length`
- `1 <= n <= 100`
- `1 <= tickets[i] <= 100`
- `0 <= k < n`
"""

def timeRequiredToBuy(tickets, k):
    """
    Calculate the time needed for the person at position k to finish buying all their tickets.

    :param tickets: List[int] - Number of tickets each person needs
    :param k: int - Index of the person we are interested in
    :return: int - Total time in seconds
    """
    time = 0
    for i in range(len(tickets)):
        if i <= k:
            time += min(tickets[i], tickets[k])
        else:
            time += min(tickets[i], tickets[k] - 1)
    return time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tickets = [2, 3, 2]
    k = 2
    print(timeRequiredToBuy(tickets, k))  # Output: 6

    # Test Case 2
    tickets = [5, 1, 1, 1]
    k = 0
    print(timeRequiredToBuy(tickets, k))  # Output: 8

    # Test Case 3
    tickets = [1, 1, 1, 1]
    k = 3
    print(timeRequiredToBuy(tickets, k))  # Output: 4

    # Test Case 4
    tickets = [3, 3, 3]
    k = 1
    print(timeRequiredToBuy(tickets, k))  # Output: 7

"""
Time Complexity Analysis:
- Let `n` be the length of the `tickets` array.
- The solution iterates through the `tickets` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The solution uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""