"""
LeetCode Problem #468: Validate IP Address

Problem Statement:
Given a string `queryIP`, return "IPv4" if it is a valid IPv4 address, "IPv6" if it is a valid IPv6 address, or "Neither" if it is not a valid IP address.

An IPv4 address is valid if:
- It consists of four decimal numbers separated by dots (`.`).
- Each number is between 0 and 255 (inclusive).
- Leading zeros are not allowed (e.g., "01" is invalid, but "1" is valid).

An IPv6 address is valid if:
- It consists of eight groups of hexadecimal numbers separated by colons (`:`).
- Each group is between 1 and 4 hexadecimal digits.
- Hexadecimal digits can include numbers (0-9) and letters (a-f, A-F).

The input string `queryIP` may contain extra leading or trailing spaces, and you should ignore them.

Example:
- Input: queryIP = "172.16.254.1"
  Output: "IPv4"
- Input: queryIP = "2001:0db8:85a3:0:0:8A2E:0370:7334"
  Output: "IPv6"
- Input: queryIP = "256.256.256.256"
  Output: "Neither"

Constraints:
- `queryIP` consists of English letters, digits, and the characters `.` and `:`.
"""

# Python Solution
import re

def validIPAddress(queryIP: str) -> str:
    def is_valid_ipv4(ip):
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        for part in parts:
            if not part.isdigit() or not 0 <= int(part) <= 255 or (part[0] == '0' and len(part) > 1):
                return False
        return True

    def is_valid_ipv6(ip):
        parts = ip.split(":")
        if len(parts) != 8:
            return False
        for part in parts:
            if not (1 <= len(part) <= 4) or not re.match(r'^[0-9a-fA-F]+$', part):
                return False
        return True

    queryIP = queryIP.strip()  # Remove leading/trailing spaces
    if "." in queryIP and is_valid_ipv4(queryIP):
        return "IPv4"
    elif ":" in queryIP and is_valid_ipv6(queryIP):
        return "IPv6"
    else:
        return "Neither"

# Example Test Cases
if __name__ == "__main__":
    test_cases = [
        ("172.16.254.1", "IPv4"),
        ("2001:0db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("256.256.256.256", "Neither"),
        ("1e1.4.5.6", "Neither"),
        ("192.0.2.1", "IPv4"),
        ("2001:db8:85a3:0:0:8A2E:0370:7334", "IPv6"),
        ("02001:0db8:85a3:0000:0000:8a2e:0370:7334", "Neither"),
    ]

    for queryIP, expected in test_cases:
        result = validIPAddress(queryIP)
        print(f"Input: {queryIP}, Output: {result}, Expected: {expected}, Pass: {result == expected}")

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - For IPv4 validation:
     - Splitting the string into 4 parts takes O(n), where n is the length of the string.
     - Checking each part for validity takes O(1) per part (constant checks), so total is O(4) = O(1).
   - For IPv6 validation:
     - Splitting the string into 8 parts takes O(n), where n is the length of the string.
     - Checking each part for validity involves regex matching, which takes O(k) per part, where k is the length of the part. Total is O(8 * k) = O(n) in the worst case.
   - Overall, the time complexity is O(n), where n is the length of the input string.

2. Space Complexity:
   - The space used for splitting the string into parts is proportional to the number of parts (4 for IPv4, 8 for IPv6). This is O(1) since the number of parts is constant.
   - Regex matching does not use additional space.
   - Overall, the space complexity is O(1).

Topic: String Manipulation
"""