"""
LeetCode Question #1108: Defanging an IP Address

Problem Statement:
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

Constraints:
- The given address is a valid IPv4 address.
"""

# Solution
def defangIPaddr(address: str) -> str:
    """
    This function takes a valid IPv4 address as input and returns its defanged version.
    """
    return address.replace(".", "[.]")

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    address1 = "1.1.1.1"
    print(defangIPaddr(address1))  # Expected Output: "1[.]1[.]1[.]1"

    # Test Case 2
    address2 = "255.100.50.0"
    print(defangIPaddr(address2))  # Expected Output: "255[.]100[.]50[.]0"

    # Test Case 3
    address3 = "192.168.0.1"
    print(defangIPaddr(address3))  # Expected Output: "192[.]168[.]0[.]1"

# Time and Space Complexity Analysis
"""
Time Complexity:
The `replace` method in Python iterates through the string once to replace all occurrences of the target substring.
Let n be the length of the input string `address`. The time complexity is O(n).

Space Complexity:
The `replace` method creates a new string with the replacements, which requires O(n) space for the new string.
Thus, the space complexity is O(n).
"""

# Topic: String Manipulation