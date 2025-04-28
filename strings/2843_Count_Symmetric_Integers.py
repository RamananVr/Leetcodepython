"""
LeetCode Problem #2843: Count Symmetric Integers

Problem Statement:
You are given two integers low and high representing a range of integers [low, high] (inclusive).
An integer x is considered symmetric if the sum of its first half of digits is equal to the sum of its second half of digits.

Return the count of symmetric integers in the range [low, high].

Notes:
- If the number of digits in x is odd, it cannot be symmetric.
- For example:
  - 121 is not symmetric because it has an odd number of digits.
  - 1221 is symmetric because 1 + 2 = 2 + 1.
  - 123321 is symmetric because 1 + 2 + 3 = 3 + 2 + 1.

Constraints:
- 1 <= low <= high <= 10^4
"""

def countSymmetricIntegers(low: int, high: int) -> int:
    def is_symmetric(num: int) -> bool:
        # Convert the number to a string to access its digits
        digits = str(num)
        n = len(digits)
        
        # Symmetric numbers must have an even number of digits
        if n % 2 != 0:
            return False
        
        # Split the digits into two halves
        mid = n // 2
        first_half = digits[:mid]
        second_half = digits[mid:]
        
        # Calculate the sum of digits in both halves
        return sum(map(int, first_half)) == sum(map(int, second_half))
    
    # Count symmetric integers in the range [low, high]
    count = 0
    for num in range(low, high + 1):
        if is_symmetric(num):
            count += 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 1
    high = 100
    print(countSymmetricIntegers(low, high))  # Expected Output: 9 (e.g., 11, 22, 33, ..., 99)

    # Test Case 2
    low = 120
    high = 130
    print(countSymmetricIntegers(low, high))  # Expected Output: 1 (e.g., 1221)

    # Test Case 3
    low = 1
    high = 10
    print(countSymmetricIntegers(low, high))  # Expected Output: 0 (no symmetric integers)

    # Test Case 4
    low = 1000
    high = 1020
    print(countSymmetricIntegers(low, high))  # Expected Output: 1 (e.g., 1001)

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The function iterates through all numbers in the range [low, high], which takes O(high - low + 1).
   - For each number, we check if it is symmetric. This involves converting the number to a string (O(d), where d is the number of digits) and summing its halves (O(d)).
   - In the worst case, d = log10(high), so the complexity for each number is O(log10(high)).
   - Overall time complexity: O((high - low + 1) * log10(high)).

2. Space Complexity:
   - The space used is primarily for the string representation of the number and its halves, which is O(log10(high)).
   - Overall space complexity: O(log10(high)).

Topic: Strings
"""