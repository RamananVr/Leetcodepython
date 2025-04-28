"""
LeetCode Problem #2600: K Items With the Maximum Sum

Problem Statement:
You are given three integers `numOnes`, `numZeros`, and `numNegOnes`. 
You have an array consisting of:
- `numOnes` ones,
- `numZeros` zeros, and
- `numNegOnes` negative ones.

You want to choose exactly `k` elements from this array such that their sum is maximized.

Return the maximum possible sum of the `k` elements.

Constraints:
- `0 <= numOnes, numZeros, numNegOnes <= 100`
- `0 <= k <= numOnes + numZeros + numNegOnes`
"""

def kItemsWithMaximumSum(numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
    """
    Calculate the maximum possible sum of k items chosen from the array.

    :param numOnes: Number of ones in the array
    :param numZeros: Number of zeros in the array
    :param numNegOnes: Number of negative ones in the array
    :param k: Number of items to choose
    :return: Maximum possible sum of k items
    """
    # First, take as many 1s as possible
    ones_taken = min(k, numOnes)
    k -= ones_taken

    # Then, take as many 0s as possible (they don't affect the sum)
    zeros_taken = min(k, numZeros)
    k -= zeros_taken

    # Finally, take the remaining items as -1s
    neg_ones_taken = k  # Whatever is left must be taken from -1s

    # Calculate the sum
    return ones_taken * 1 + zeros_taken * 0 + neg_ones_taken * -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 2
    print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))  # Expected Output: 2

    # Test Case 2
    numOnes = 3
    numZeros = 2
    numNegOnes = 0
    k = 4
    print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))  # Expected Output: 3

    # Test Case 3
    numOnes = 3
    numZeros = 2
    numNegOnes = 2
    k = 5
    print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))  # Expected Output: 2

    # Test Case 4
    numOnes = 0
    numZeros = 0
    numNegOnes = 5
    k = 3
    print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))  # Expected Output: -3

    # Test Case 5
    numOnes = 5
    numZeros = 5
    numNegOnes = 5
    k = 10
    print(kItemsWithMaximumSum(numOnes, numZeros, numNegOnes, k))  # Expected Output: 5


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a constant number of operations (min, subtraction, and multiplication).
- Therefore, the time complexity is O(1).

Space Complexity:
- The function uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Greedy
"""