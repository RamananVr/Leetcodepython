"""
LeetCode Problem #888: Fair Candy Swap

Problem Statement:
Alice and Bob have candy bars of different sizes. Alice has the candy bars represented by an integer array `aliceSizes`, 
where `aliceSizes[i]` is the size of the i-th candy bar she has. Bob has the candy bars represented by an integer array 
`bobSizes`, where `bobSizes[j]` is the size of the j-th candy bar he has.

Since they are friends, they would like to exchange one candy bar each so that after the exchange, they both have the 
same total amount of candy. The total amount of candy a person has is the sum of the sizes of their candy bars.

Return an integer array `answer` where `answer[0]` is the size of the candy bar Alice must exchange, and `answer[1]` is 
the size of the candy bar Bob must exchange. If there are multiple answers, you may return any one of them. It is 
guaranteed that at least one answer exists.

Constraints:
- 1 <= aliceSizes.length, bobSizes.length <= 10^4
- 1 <= aliceSizes[i], bobSizes[j] <= 10^5
- Alice and Bob have different total amounts of candy initially.
- There is guaranteed to be at least one valid answer.

"""

# Solution
def fairCandySwap(aliceSizes, bobSizes):
    """
    Find the candy sizes Alice and Bob should swap to equalize their total candy sizes.

    :param aliceSizes: List[int] - Sizes of Alice's candy bars
    :param bobSizes: List[int] - Sizes of Bob's candy bars
    :return: List[int] - [size of Alice's candy bar to swap, size of Bob's candy bar to swap]
    """
    # Calculate the total candy sizes for Alice and Bob
    sumAlice = sum(aliceSizes)
    sumBob = sum(bobSizes)
    
    # Calculate the difference between their total candy sizes
    # Alice needs to lose (sumAlice - sumBob) // 2 and Bob needs to gain the same amount
    delta = (sumAlice - sumBob) // 2
    
    # Use a set for Bob's candy sizes for quick lookup
    bobSet = set(bobSizes)
    
    # Iterate through Alice's candy sizes to find a valid swap
    for candy in aliceSizes:
        if candy - delta in bobSet:
            return [candy, candy - delta]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    aliceSizes = [1, 1]
    bobSizes = [2, 2]
    print(fairCandySwap(aliceSizes, bobSizes))  # Output: [1, 2]

    # Test Case 2
    aliceSizes = [1, 2, 5]
    bobSizes = [2, 4]
    print(fairCandySwap(aliceSizes, bobSizes))  # Output: [5, 4]

    # Test Case 3
    aliceSizes = [2]
    bobSizes = [1, 3]
    print(fairCandySwap(aliceSizes, bobSizes))  # Output: [2, 3]

    # Test Case 4
    aliceSizes = [1, 2, 3]
    bobSizes = [4, 5, 6]
    print(fairCandySwap(aliceSizes, bobSizes))  # Output: [1, 4]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the sum of `aliceSizes` and `bobSizes` takes O(n + m), where n is the length of `aliceSizes` and m is the 
  length of `bobSizes`.
- Creating the set `bobSet` takes O(m).
- Iterating through `aliceSizes` to find a valid swap takes O(n).
- Overall, the time complexity is O(n + m).

Space Complexity:
- The space complexity is O(m) due to the set `bobSet`.

Topic: Arrays
"""