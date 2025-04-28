"""
LeetCode Problem #1868: Product of Two Run-Length Encoded Arrays

Problem Statement:
Run-length encoding is a compression algorithm that allows for an integer array 
to be represented by a sequence of pairs. Each pair `(value, frequency)` represents 
`frequency` occurrences of the `value`.

For example, the array `[1,1,1,2,2,2,2]` can be represented as `[[1,3],[2,4]]`. 
Run-length encoded arrays are allowed to have `frequency` equal to `0`.

Given two run-length encoded arrays `encoded1` and `encoded2`, return the product 
of the two arrays as a run-length encoded array.

The product of two run-length encoded arrays can be calculated using the following process:
1. Expand both encoded arrays to their full length.
2. Multiply the two full-length arrays element by element.
3. Compress the resulting array into a run-length encoded array.

You are not allowed to expand the arrays directly.

Example 1:
Input: encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]
Output: [[6,3],[6,3]]

Explanation:
- Expand encoded1 to [1,1,1,2,2,2].
- Expand encoded2 to [6,6,6,3,3,3].
- Multiply element by element: [6,6,6,6,6,6].
- Compress into run-length encoding: [[6,3],[6,3]].

Example 2:
Input: encoded1 = [[1,1],[2,1],[3,2]], encoded2 = [[2,3]]
Output: [[2,1],[4,1],[6,2]]

Constraints:
- 1 <= encoded1.length, encoded2.length <= 1000
- 1 <= value <= 10^4
- 1 <= frequency <= 10^4
- The given input represents a valid run-length encoded array.

Follow-up: Can you solve this problem without expanding the arrays?

"""

# Python Solution
def findRLEArray(encoded1, encoded2):
    result = []
    i, j = 0, 0

    while i < len(encoded1) and j < len(encoded2):
        # Get the current value and frequency from both arrays
        val1, freq1 = encoded1[i]
        val2, freq2 = encoded2[j]

        # Calculate the product and the minimum frequency
        product = val1 * val2
        min_freq = min(freq1, freq2)

        # Add the product to the result, merging if necessary
        if result and result[-1][0] == product:
            result[-1][1] += min_freq
        else:
            result.append([product, min_freq])

        # Update the frequencies in the original arrays
        encoded1[i][1] -= min_freq
        encoded2[j][1] -= min_freq

        # Move to the next pair if the frequency becomes zero
        if encoded1[i][1] == 0:
            i += 1
        if encoded2[j][1] == 0:
            j += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    encoded1 = [[1, 3], [2, 3]]
    encoded2 = [[6, 3], [3, 3]]
    print(findRLEArray(encoded1, encoded2))  # Output: [[6, 3], [6, 3]]

    # Test Case 2
    encoded1 = [[1, 1], [2, 1], [3, 2]]
    encoded2 = [[2, 3]]
    print(findRLEArray(encoded1, encoded2))  # Output: [[2, 1], [4, 1], [6, 2]]

    # Test Case 3
    encoded1 = [[5, 5]]
    encoded2 = [[2, 2], [3, 3]]
    print(findRLEArray(encoded1, encoded2))  # Output: [[10, 2], [15, 3]]

    # Test Case 4
    encoded1 = [[1, 4], [2, 2]]
    encoded2 = [[3, 3], [4, 3]]
    print(findRLEArray(encoded1, encoded2))  # Output: [[3, 3], [4, 1], [8, 2]]

# Time and Space Complexity Analysis
# Time Complexity: O(n + m), where n is the length of encoded1 and m is the length of encoded2.
#                  We iterate through both arrays once, processing each pair.
# Space Complexity: O(1) additional space, as we only use a result list to store the output.

# Topic: Arrays