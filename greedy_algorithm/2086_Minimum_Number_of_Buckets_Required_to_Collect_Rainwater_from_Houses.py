"""
LeetCode Problem #2086: Minimum Number of Buckets Required to Collect Rainwater from Houses

Problem Statement:
You are given a string `street` representing a street where:
- `H` represents a house,
- `.` represents an empty space, and
- no two houses are adjacent.

Buckets can be placed on empty spaces to collect rainwater from adjacent houses. A bucket can collect rainwater from at most one house on its left and one house on its right. You cannot place a bucket on a house.

Return the minimum number of buckets required so that every house has access to a bucket. If it is impossible to place buckets to meet the requirements, return `-1`.

Constraints:
- `1 <= street.length <= 10^5`
- `street[i]` is either `'H'` or `'.'`.

"""

def minimumBuckets(street: str) -> int:
    """
    Calculate the minimum number of buckets required to collect rainwater from houses.

    :param street: A string representing the street layout.
    :return: The minimum number of buckets required, or -1 if it's impossible.
    """
    n = len(street)
    street = list(street)  # Convert to list for mutability
    buckets = 0

    for i in range(n):
        if street[i] == 'H':
            # If the house is already covered by a bucket, skip it
            if i > 0 and street[i - 1] == 'B':
                continue
            # Place a bucket to the right if possible
            if i + 1 < n and street[i + 1] == '.':
                street[i + 1] = 'B'
                buckets += 1
            # Otherwise, place a bucket to the left if possible
            elif i > 0 and street[i - 1] == '.':
                street[i - 1] = 'B'
                buckets += 1
            # If neither is possible, return -1
            else:
                return -1

    return buckets


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple case with one house and one empty space
    street1 = "H."
    print(minimumBuckets(street1))  # Expected output: 1

    # Test Case 2: Multiple houses with sufficient empty spaces
    street2 = ".H.H."
    print(minimumBuckets(street2))  # Expected output: 2

    # Test Case 3: Impossible case with adjacent houses
    street3 = "HH"
    print(minimumBuckets(street3))  # Expected output: -1

    # Test Case 4: Complex case with alternating houses and empty spaces
    street4 = "H.H.H"
    print(minimumBuckets(street4))  # Expected output: 3

    # Test Case 5: Edge case with no houses
    street5 = "....."
    print(minimumBuckets(street5))  # Expected output: 0

    # Test Case 6: Edge case with one house and no empty spaces
    street6 = "H"
    print(minimumBuckets(street6))  # Expected output: -1


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string once, performing constant-time operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm converts the input string to a list for mutability, which requires O(n) space.
- No additional data structures are used, so the overall space complexity is O(n).

Topic: Greedy Algorithm
"""