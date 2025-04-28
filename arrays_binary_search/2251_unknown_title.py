"""
LeetCode Problem #2251: Number of Flowers in Full Bloom

Problem Statement:
You are given two 0-indexed integer arrays `start` and `end`, both of length `n`, where `start[i]` and `end[i]` denote the start and end times of the i-th flower's blooming period (inclusive). You are also given a 0-indexed integer array `persons` of length `m`, where `persons[j]` is the time a person arrives to see the flowers.

Return an integer array `answer` of length `m`, where `answer[j]` is the number of flowers that are blooming when `persons[j]` arrives.

A flower is considered blooming at time `t` if `start[i] <= t <= end[i]`.

Constraints:
- `n == start.length == end.length`
- `1 <= n <= 10^5`
- `1 <= m <= 10^5`
- `1 <= start[i] <= end[i] <= 10^9`
- `1 <= persons[j] <= 10^9`
"""

from bisect import bisect_left, bisect_right

def fullBloomFlowers(start, end, persons):
    """
    Function to calculate the number of flowers in full bloom for each person's arrival time.

    Args:
    start (List[int]): Start times of flowers blooming.
    end (List[int]): End times of flowers blooming.
    persons (List[int]): Arrival times of persons.

    Returns:
    List[int]: Number of flowers blooming for each person's arrival time.
    """
    # Sort the start and end times
    start.sort()
    end.sort()

    # For each person's arrival time, calculate the number of flowers blooming
    result = []
    for time in persons:
        # Count flowers that have started blooming
        blooming_start = bisect_right(start, time)
        # Count flowers that have finished blooming
        blooming_end = bisect_left(end, time)
        # The difference gives the number of flowers in full bloom
        result.append(blooming_start - blooming_end)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    start = [1, 2, 3]
    end = [3, 4, 5]
    persons = [2, 3, 4]
    print(fullBloomFlowers(start, end, persons))  # Output: [2, 2, 1]

    # Test Case 2
    start = [1, 4, 5]
    end = [4, 5, 6]
    persons = [3, 5, 6]
    print(fullBloomFlowers(start, end, persons))  # Output: [1, 2, 1]

    # Test Case 3
    start = [1, 10, 20]
    end = [5, 15, 25]
    persons = [5, 10, 15, 20]
    print(fullBloomFlowers(start, end, persons))  # Output: [1, 2, 1, 1]

"""
Time Complexity:
- Sorting the `start` and `end` arrays takes O(n log n), where n is the number of flowers.
- For each person's arrival time, we perform two binary searches, each taking O(log n). Since there are m persons, this step takes O(m log n).
- Overall time complexity: O(n log n + m log n).

Space Complexity:
- The space complexity is O(1) additional space, as we are not using any extra data structures apart from the input and output.

Topic: Arrays, Binary Search
"""