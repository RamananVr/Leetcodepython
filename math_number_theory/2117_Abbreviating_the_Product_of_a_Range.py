"""
LeetCode Problem #2117: Abbreviating the Product of a Range

Problem Statement:
You are given two integers left and right representing a range [left, right]. You need to return the product of all integers in the range [left, right] as a string. However, if the product has more than 10 digits, you should abbreviate it.

The abbreviation should be in the format "<leading_digits>...<trailing_digits>e<exponent>", where:
- <leading_digits> is the first 5 digits of the product.
- <trailing_digits> is the last 5 digits of the product.
- <exponent> is the number of digits in the product minus 1.

If the product has 10 or fewer digits, return it as a string without abbreviation.

Constraints:
- 1 <= left <= right <= 10^6
"""

# Solution
import math

def abbreviateProduct(left: int, right: int) -> str:
    # Initialize variables
    total_digits = 0
    leading_digits = 1
    trailing_digits = 1
    trailing_mod = 10**5
    has_large_product = False

    # Calculate the product
    for i in range(left, right + 1):
        # Update trailing digits
        trailing_digits *= i
        trailing_digits %= trailing_mod

        # Update leading digits using logarithms
        leading_digits += math.log10(i)
        total_digits = int(leading_digits)

        # Check if the product exceeds 10 digits
        if total_digits > 10:
            has_large_product = True

    # If the product is large, abbreviate it
    if has_large_product:
        leading = int(10**(leading_digits - total_digits + 5))
        trailing = trailing_digits
        return f"{leading}...{trailing}e{total_digits - 1}"
    else:
        # Calculate the full product directly
        product = 1
        for i in range(left, right + 1):
            product *= i
        return str(product)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small range
    print(abbreviateProduct(1, 5))  # Output: "120"

    # Test Case 2: Large range with abbreviation
    print(abbreviateProduct(1, 100))  # Output: "93326...00000e157"

    # Test Case 3: Single number
    print(abbreviateProduct(10, 10))  # Output: "10"

    # Test Case 4: Large range
    print(abbreviateProduct(100, 200))  # Output: "<leading_digits>...<trailing_digits>e<exponent>"

# Time and Space Complexity Analysis
"""
Time Complexity:
- The loop iterates through all numbers in the range [left, right], so the time complexity is O(right - left).
- Calculating logarithms and modular arithmetic for each number is O(1), so the overall complexity is O(right - left).

Space Complexity:
- The space complexity is O(1) since we use a constant amount of extra space for variables like `leading_digits`, `trailing_digits`, and `total_digits`.

Topic: Math, Number Theory
"""