"""
LeetCode Problem #2308: Calculate Amount Paid in Taxes

Problem Statement:
You are given a 0-indexed 2D integer array `brackets` where `brackets[i] = [upper_i, percent_i]` means that the `i-th` tax bracket has an upper bound of `upper_i` and is taxed at a rate of `percent_i`. The brackets are sorted by upper bound (i.e., `upper_i` for `i` is less than `upper_i` for `i + 1`).

Tax is calculated as follows:
- The first `upper_0` dollars earned are taxed at a rate of `percent_0`.
- The next `upper_1 - upper_0` dollars earned are taxed at a rate of `percent_1`.
- The next `upper_2 - upper_1` dollars earned are taxed at a rate of `percent_2`, and so on.

You are given an integer `income` representing the amount of money you earned. Return the amount of money that you have to pay in taxes. Answers within `10^-5` of the actual answer will be accepted.

Constraints:
- `1 <= brackets.length <= 100`
- `1 <= upper_i <= 1000`
- `0 <= percent_i <= 100`
- `0 <= income <= 1000`
- `upper_i` is sorted in strictly increasing order.

"""

# Python Solution
def calculateTax(brackets, income):
    """
    Calculate the amount of taxes paid based on the given brackets and income.

    :param brackets: List[List[int]] - Tax brackets where each element is [upper, percent].
    :param income: int - The total income earned.
    :return: float - The total amount of taxes paid.
    """
    tax_paid = 0
    previous_upper = 0

    for upper, percent in brackets:
        if income <= previous_upper:
            break
        taxable_income = min(income, upper) - previous_upper
        tax_paid += taxable_income * (percent / 100)
        previous_upper = upper

    return tax_paid


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    brackets1 = [[3, 50], [7, 10], [12, 25]]
    income1 = 10
    print(calculateTax(brackets1, income1))  # Expected Output: 2.65

    # Test Case 2
    brackets2 = [[1, 0], [4, 25], [5, 50]]
    income2 = 2
    print(calculateTax(brackets2, income2))  # Expected Output: 0.25

    # Test Case 3
    brackets3 = [[2, 10], [5, 20], [10, 30]]
    income3 = 7
    print(calculateTax(brackets3, income3))  # Expected Output: 1.9

    # Test Case 4
    brackets4 = [[5, 10], [10, 20], [20, 30]]
    income4 = 15
    print(calculateTax(brackets4, income4))  # Expected Output: 2.5

    # Test Case 5
    brackets5 = [[3, 50], [7, 10], [12, 25]]
    income5 = 0
    print(calculateTax(brackets5, income5))  # Expected Output: 0.0


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the tax brackets, which has a maximum length of 100.
- For each bracket, we perform constant-time operations (comparison, subtraction, multiplication, addition).
- Therefore, the time complexity is O(n), where n is the number of tax brackets.

Space Complexity:
- The function uses a constant amount of extra space for variables (`tax_paid`, `previous_upper`, `taxable_income`).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

"""

# Topic: Arrays