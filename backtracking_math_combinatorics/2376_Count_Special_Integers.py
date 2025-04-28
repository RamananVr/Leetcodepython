"""
LeetCode Problem #2376: Count Special Integers

Problem Statement:
We call a positive integer special if all of its digits are distinct. Given a positive integer `n`, return the number of special integers that belong to the interval [1, n].

Constraints:
1 <= n <= 2 * 10^9
"""

def countSpecialNumbers(n: int) -> int:
    """
    Function to count the number of special integers in the range [1, n].
    """
    def countUniqueDigitsNumbers(length):
        """
        Helper function to count numbers with unique digits of a given length.
        """
        if length == 0:
            return 0
        count = 9
        available_digits = 9
        for i in range(1, length):
            count *= available_digits
            available_digits -= 1
        return count

    def countNumbersWithUniqueDigitsLessThan(num_str):
        """
        Helper function to count numbers with unique digits less than the given number.
        """
        length = len(num_str)
        total_count = 0

        # Count numbers with fewer digits
        for i in range(1, length):
            total_count += countUniqueDigitsNumbers(i)

        # Count numbers with the same number of digits but less than num_str
        seen = set()
        for i in range(length):
            digit = int(num_str[i])
            for smaller_digit in range(0 if i > 0 else 1, digit):
                if smaller_digit not in seen:
                    total_count += countUniqueDigitsNumbers(length - i - 1)
            if digit in seen:
                break
            seen.add(digit)
        else:
            total_count += 1  # Include the number itself if all digits are unique

        return total_count

    return countNumbersWithUniqueDigitsLessThan(str(n))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 20
    print(f"Number of special integers in range [1, {n1}]: {countSpecialNumbers(n1)}")  # Expected: 19

    # Test Case 2
    n2 = 100
    print(f"Number of special integers in range [1, {n2}]: {countSpecialNumbers(n2)}")  # Expected: 90

    # Test Case 3
    n3 = 135
    print(f"Number of special integers in range [1, {n3}]: {countSpecialNumbers(n3)}")  # Expected: 110

    # Test Case 4
    n4 = 1000
    print(f"Number of special integers in range [1, {n4}]: {countSpecialNumbers(n4)}")  # Expected: 738

    # Test Case 5
    n5 = 2_000_000_000
    print(f"Number of special integers in range [1, {n5}]: {countSpecialNumbers(n5)}")  # Expected: Large value


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Let `L` be the number of digits in `n` (L = log10(n)).
   - The function `countUniqueDigitsNumbers` runs in O(L) for each digit length.
   - The function `countNumbersWithUniqueDigitsLessThan` iterates over the digits of `n` (O(L)) and performs a constant amount of work for each digit.
   - Overall, the time complexity is O(L^2), where L = log10(n).

2. Space Complexity:
   - The space complexity is O(L) due to the recursive calls and the `seen` set used to track digits.

Topic: Backtracking, Math, Combinatorics
"""