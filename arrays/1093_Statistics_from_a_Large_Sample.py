"""
LeetCode Problem #1093: Statistics from a Large Sample

Problem Statement:
We sampled integers between 0 and 255, and stored the results in an array `count` where `count[k]` is the number of times the integer `k` was sampled.

Calculate the following statistics:
1. Minimum: The smallest integer that was sampled at least once.
2. Maximum: The largest integer that was sampled at least once.
3. Mean: The average of all sampled numbers, calculated as the total sum of all numbers divided by the total count of numbers.
4. Median:
   - If the total number of samples is odd, the median is the middle element.
   - If the total number of samples is even, the median is the average of the two middle elements.
5. Mode: The most frequently sampled integer. If there is a tie, return the smallest one.

Return the statistics as a list of floats `[minimum, maximum, mean, median, mode]`. The values for mean and median should be rounded to 5 decimal places.

Constraints:
- `count.length == 256`
- `0 <= count[i] <= 10^9`
- `1 <= sum(count) <= 10^9`
"""

def sampleStats(count):
    """
    Calculate the statistics from the given count array.

    :param count: List[int] - An array where count[k] is the number of times integer k was sampled.
    :return: List[float] - A list containing [minimum, maximum, mean, median, mode].
    """
    total_count = sum(count)
    total_sum = 0
    min_val = None
    max_val = None
    mode = None
    max_frequency = 0

    # Calculate minimum, maximum, mean, and mode
    for i in range(256):
        if count[i] > 0:
            if min_val is None:
                min_val = i
            max_val = i
            total_sum += i * count[i]
            if count[i] > max_frequency:
                max_frequency = count[i]
                mode = i

    mean = total_sum / total_count

    # Calculate median
    median = 0
    cumulative_count = 0
    mid1, mid2 = None, None

    for i in range(256):
        if count[i] > 0:
            cumulative_count += count[i]
            if mid1 is None and cumulative_count >= (total_count + 1) // 2:
                mid1 = i
            if mid2 is None and cumulative_count >= total_count // 2 + 1:
                mid2 = i
                break

    if total_count % 2 == 0:
        median = (mid1 + mid2) / 2
    else:
        median = mid1

    return [float(min_val), float(max_val), round(mean, 5), round(median, 5), float(mode)]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    count1 = [0] * 256
    count1[1] = 1
    count1[2] = 2
    count1[3] = 3
    print(sampleStats(count1))  # Expected: [1.0, 3.0, 2.33333, 2.5, 3.0]

    # Test Case 2
    count2 = [0] * 256
    count2[0] = 5
    count2[255] = 1
    print(sampleStats(count2))  # Expected: [0.0, 255.0, 42.5, 0.0, 0.0]

    # Test Case 3
    count3 = [0] * 256
    count3[10] = 1
    count3[20] = 1
    count3[30] = 1
    print(sampleStats(count3))  # Expected: [10.0, 30.0, 20.0, 20.0, 10.0]


"""
Time Complexity:
- Calculating minimum, maximum, mean, and mode: O(256) since we iterate through the `count` array once.
- Calculating the median: O(256) since we iterate through the `count` array again to find the middle elements.
- Total: O(256), which is constant time.

Space Complexity:
- O(1) since we use a constant amount of extra space.

Topic: Arrays
"""