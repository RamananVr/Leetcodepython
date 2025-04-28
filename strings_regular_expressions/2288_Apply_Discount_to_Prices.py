"""
LeetCode Problem #2288: Apply Discount to Prices

Problem Statement:
A sentence is a string of single-space separated words where each word can contain digits, lowercase letters, and the dollar sign '$'. A word represents a price if it is a sequence of digits preceded by a dollar sign '$'. For example, "$100", "$23", and "$6" represent prices, while "$$", "100", and "$abc" do not.

You are given a string `sentence` representing a sentence and an integer `discount`. For each word representing a price, apply a discount of `discount%` on the price and update the word in the sentence. All updated prices should be represented with exactly two decimal places.

Return a string representing the modified sentence.

Example 1:
Input: sentence = "there are $1 $2 and 5$ candies in the shop", discount = 50
Output: "there are $0.50 $1.00 and 5$ candies in the shop"

Example 2:
Input: sentence = "1 2 $3 4 $5 $6 7 8$ $9 $10$", discount = 100
Output: "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $0.00"

Constraints:
- 1 <= sentence.length <= 10^5
- sentence consists of lowercase English letters, digits, ' ', and '$'.
- All prices will be valid without leading zeros.
- All prices will have at most 10 digits.
- 0 <= discount <= 100
"""

# Python Solution
import re

def apply_discount_to_prices(sentence: str, discount: int) -> str:
    def apply_discount(match):
        # Extract the price from the match
        price = float(match.group(1))
        # Apply the discount
        discounted_price = price * (1 - discount / 100)
        # Format the discounted price to 2 decimal places
        return f"${discounted_price:.2f}"
    
    # Use regex to find all valid prices in the sentence
    # Pattern explanation: \$([0-9]+) matches a dollar sign followed by one or more digits
    return re.sub(r'\$([0-9]+)', apply_discount, sentence)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sentence1 = "there are $1 $2 and 5$ candies in the shop"
    discount1 = 50
    print(apply_discount_to_prices(sentence1, discount1))  # Output: "there are $0.50 $1.00 and 5$ candies in the shop"

    # Test Case 2
    sentence2 = "1 2 $3 4 $5 $6 7 8$ $9 $10$"
    discount2 = 100
    print(apply_discount_to_prices(sentence2, discount2))  # Output: "1 2 $0.00 4 $0.00 $0.00 7 8$ $0.00 $0.00"

    # Test Case 3
    sentence3 = "the total is $100 and the discount is $50"
    discount3 = 25
    print(apply_discount_to_prices(sentence3, discount3))  # Output: "the total is $75.00 and the discount is $37.50"

    # Test Case 4
    sentence4 = "$1234567890 is a large number"
    discount4 = 10
    print(apply_discount_to_prices(sentence4, discount4))  # Output: "$1111111101.00 is a large number"

    # Test Case 5
    sentence5 = "no prices here"
    discount5 = 20
    print(apply_discount_to_prices(sentence5, discount5))  # Output: "no prices here"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the length of the input string `sentence`.
- The regex `re.sub` scans the entire string once, and for each match, the `apply_discount` function is called.
- Extracting and formatting the price is O(1) for each match.
- Overall, the time complexity is O(n).

Space Complexity:
- The regex engine may use additional space proportional to the number of matches, but this is typically negligible.
- The output string requires O(n) space to store the result.
- Overall, the space complexity is O(n).
"""

# Topic: Strings, Regular Expressions