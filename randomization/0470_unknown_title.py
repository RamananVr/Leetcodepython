"""
LeetCode Problem #470: Implement Rand10() Using Rand7()

Problem Statement:
Given a function `rand7()` that generates a uniform random integer in the range [1, 7], 
write a function `rand10()` that generates a uniform random integer in the range [1, 10]. 
You can only call the `rand7()` function, and you shouldn't call any other library function.

Each test case will have one internal call to `rand7()`, and the input to `rand7()` is 
always null. It is guaranteed that `rand7()` generates a uniform random integer in the 
range [1, 7].

Constraints:
- 1 <= rand7() <= 7
- rand7() is uniform, meaning that each integer in the range [1, 7] has an equal probability of being returned.
- rand10() must be uniform, meaning that each integer in the range [1, 10] has an equal probability of being returned.

Follow-up:
What is the expected value for the number of calls to `rand7()` function?

"""

# Clean and Correct Python Solution
import random

def rand7():
    """Simulates the rand7() function, which generates a random integer between 1 and 7."""
    return random.randint(1, 7)

def rand10():
    """
    Generates a uniform random integer in the range [1, 10] using the rand7() function.
    """
    while True:
        # Generate a number in the range [1, 49] using two calls to rand7()
        row = rand7()
        col = rand7()
        num = (row - 1) * 7 + col  # Maps (row, col) to a number in [1, 49]

        # Only accept numbers in the range [1, 40]
        if num <= 40:
            return 1 + (num - 1) % 10  # Map [1, 40] to [1, 10]

# Example Test Cases
if __name__ == "__main__":
    # Test rand10() by generating a large number of samples and checking uniformity
    from collections import Counter

    # Generate 100,000 samples
    samples = [rand10() for _ in range(100000)]
    counts = Counter(samples)

    # Print the counts for each number in [1, 10]
    print("Counts for each number in [1, 10]:")
    for i in range(1, 11):
        print(f"{i}: {counts[i]}")

"""
Time and Space Complexity Analysis:

Time Complexity:
- The expected number of calls to `rand7()` is approximately 2.45.
  This is because we are generating a number in the range [1, 49] and rejecting numbers in the range [41, 49].
  The probability of accepting a number is 40/49, so the expected number of iterations is 1 / (40/49) = 49/40 ≈ 1.225.
  Since each iteration involves 2 calls to `rand7()`, the expected number of calls to `rand7()` is 2 * 1.225 ≈ 2.45.

Space Complexity:
- The space complexity is O(1) because we are using a constant amount of extra space.

Topic: Randomization
"""