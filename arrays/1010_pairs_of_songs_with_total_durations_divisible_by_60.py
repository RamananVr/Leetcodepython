"""
LeetCode Question #1010: Pairs of Songs With Total Durations Divisible by 60

Problem Statement:
You are given a list of songs where the i-th song has a duration of `time[i]` seconds.

Return the number of pairs of songs for which their total duration in seconds is divisible by 60.
Formally, we want the number of indices `i, j` such that `i < j` and `(time[i] + time[j]) % 60 == 0`.

Constraints:
- 1 <= time.length <= 6 * 10^4
- 1 <= time[i] <= 500

Example 1:
Input: time = [30, 20, 150, 100, 40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(30, 150), (20, 100), (20, 40)

Example 2:
Input: time = [60, 60, 60]
Output: 3
Explanation: All three pairs (60, 60), (60, 60), (60, 60) have a total duration divisible by 60.

Follow-up:
Can you solve it in O(n) time complexity?
"""

# Solution
def numPairsDivisibleBy60(time):
    """
    Function to calculate the number of pairs of songs with total durations divisible by 60.

    :param time: List[int] - List of song durations in seconds.
    :return: int - Number of pairs with total duration divisible by 60.
    """
    # Create a frequency array to store remainders
    remainder_count = [0] * 60
    count = 0

    for t in time:
        remainder = t % 60
        # Find the complement remainder that makes the sum divisible by 60
        complement = (60 - remainder) % 60
        count += remainder_count[complement]
        # Increment the count for the current remainder
        remainder_count[remainder] += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    time1 = [30, 20, 150, 100, 40]
    print(numPairsDivisibleBy60(time1))  # Output: 3

    # Test Case 2
    time2 = [60, 60, 60]
    print(numPairsDivisibleBy60(time2))  # Output: 3

    # Test Case 3
    time3 = [10, 50, 90, 30]
    print(numPairsDivisibleBy60(time3))  # Output: 2

    # Test Case 4
    time4 = [20, 40, 60, 80, 100]
    print(numPairsDivisibleBy60(time4))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the `time` list once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `time` list.

Space Complexity:
- The function uses a fixed-size array `remainder_count` of size 60 to store the frequency of remainders.
- Therefore, the space complexity is O(1), as the size of the array does not depend on the input size.

Topic: Arrays
"""