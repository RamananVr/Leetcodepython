"""
LeetCode Problem #831: Masking Personal Information

Problem Statement:
You are given a string `s` representing either an email address or a phone number. Return the masked version of that string.

When masking an email:
- The email address consists of a local name and a domain name separated by the '@' symbol.
- The local name and domain name consist of lowercase and uppercase English letters.
- The local name will be masked such that only the first and last character are visible, and all other characters between them are replaced by 5 asterisks ('*****').
- The domain name remains unchanged.
- The masked email should be in lowercase.

When masking a phone number:
- A phone number consists of digits, spaces (' '), dashes ('-'), parentheses ('(' and ')'), and may start with a '+'.
- You should remove all non-digit characters and mask the digits as follows:
  - The last 4 digits remain visible.
  - All other digits are replaced by asterisks ('*').
  - If the phone number contains more than 10 digits, the country code is also masked with asterisks.
  - The masked phone number should be formatted as follows:
    - "***-***-XXXX" if it contains 10 digits.
    - "+*-***-***-XXXX" if it contains 11 digits.
    - "+**-***-***-XXXX" if it contains 12 digits.
    - "+***-***-***-XXXX" if it contains 13 digits.

Constraints:
- `s` is either a valid email or a valid phone number.
- If `s` is an email, it will contain exactly one '@' symbol.
- If `s` is a phone number, it will contain at least 10 digits.

"""

# Python Solution
import re

def maskPII(s: str) -> str:
    if '@' in s:  # Masking an email
        local, domain = s.split('@')
        local = local.lower()
        domain = domain.lower()
        return f"{local[0]}*****{local[-1]}@{domain}"
    else:  # Masking a phone number
        digits = re.sub(r'\D', '', s)  # Remove all non-digit characters
        num_digits = len(digits)
        masked_local = "***-***-" + digits[-4:]
        if num_digits == 10:
            return masked_local
        else:
            country_code = "+" + "*" * (num_digits - 10)
            return f"{country_code}-{masked_local}"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Email masking
    email = "LeetCode@LeetCode.com"
    print(maskPII(email))  # Expected: "l*****e@leetcode.com"

    # Test Case 2: Phone number masking (10 digits)
    phone_10_digits = "123-456-7890"
    print(maskPII(phone_10_digits))  # Expected: "***-***-7890"

    # Test Case 3: Phone number masking (11 digits)
    phone_11_digits = "+1 (123) 456-7890"
    print(maskPII(phone_11_digits))  # Expected: "+*-***-***-7890"

    # Test Case 4: Phone number masking (12 digits)
    phone_12_digits = "+91-1234567890"
    print(maskPII(phone_12_digits))  # Expected: "+**-***-***-7890"

    # Test Case 5: Phone number masking (13 digits)
    phone_13_digits = "+123-1234567890"
    print(maskPII(phone_13_digits))  # Expected: "+***-***-***-7890"

# Time and Space Complexity Analysis
# Time Complexity:
# - Masking an email: Splitting the string and formatting takes O(n), where n is the length of the email string.
# - Masking a phone number: Removing non-digit characters and formatting takes O(m), where m is the length of the phone number string.
# Overall: O(max(n, m)).

# Space Complexity:
# - Masking an email: Requires O(n) space for the split and formatted string.
# - Masking a phone number: Requires O(m) space for the cleaned digits and formatted string.
# Overall: O(max(n, m)).

# Topic: String Manipulation