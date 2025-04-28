"""
LeetCode Problem #2827: Number of Beautiful Integers in the Range

Problem Statement:
You are given three integers `low`, `high`, and `k`. An integer is considered beautiful if it satisfies the following conditions:
1. It is divisible by `k`.
2. The number of even digits in the integer is equal to the number of odd digits.

Return the count of beautiful integers in the inclusive range `[low, high]`.

Constraints:
- 1 <= low <= high <= 10^9
- 1 <= k <= 20
"""

def count_beautiful_integers(low: int, high: int, k: int) -> int:
    """
    Function to count the number of beautiful integers in the range [low, high].
    """
    def is_beautiful(num: int) -> bool:
        # Check if the number is divisible by k
        if num % k != 0:
            return False
        
        # Count even and odd digits
        even_count, odd_count = 0, 0
        for digit in str(num):
            if int(digit) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1
        
        # Check if the number of even and odd digits are equal
        return even_count == odd_count

    # Count all beautiful integers in the range
    count = 0
    for num in range(low, high + 1):
        if is_beautiful(num):
            count += 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 10
    high = 20
    k = 2
    print(count_beautiful_integers(low, high, k))  # Expected Output: 1 (Only 12 is beautiful)

    # Test Case 2
    low = 1
    high = 100
    k = 5
    print(count_beautiful_integers(low, high, k))  # Expected Output: 5 (15, 25, 35, 45, 55 are beautiful)

    # Test Case 3
    low = 100
    high = 200
    k = 10
    print(count_beautiful_integers(low, high, k))  # Expected Output: 0 (No beautiful integers in this range)

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The function iterates through all integers in the range [low, high], which takes O(high - low + 1).
   - For each number, it checks divisibility by k (O(1)) and counts even/odd digits (O(d), where d is the number of digits in the number).
   - In the worst case, the number of digits d is log10(high).
   - Overall time complexity: O((high - low + 1) * log10(high)).

2. Space Complexity:
   - The function uses a constant amount of extra space for variables and the digit counting process.
   - Space complexity: O(1).

Topic: Math, Brute Force
"""