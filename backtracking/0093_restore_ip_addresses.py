"""
LeetCode Question #93: Restore IP Addresses

Problem Statement:
A valid IP address consists of exactly four integers (each integer is between 0 and 255) separated by single dots, and cannot have leading zeros. For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312", and "192.168@1.1" are invalid IP addresses.

Given a string `s` containing only digits, return all possible valid IP addresses that can be formed by inserting dots into `s`. You are not allowed to reorder or remove any digits in `s`. You may return the valid IP addresses in any order.

Example 1:
Input: s = "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]

Example 2:
Input: s = "0000"
Output: ["0.0.0.0"]

Example 3:
Input: s = "101023"
Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

Constraints:
- `1 <= s.length <= 20`
- `s` consists of digits only.
"""

# Python Solution
def restore_ip_addresses(s: str) -> list[str]:
    def is_valid(segment: str) -> bool:
        # A segment is valid if:
        # 1. It is not empty.
        # 2. It does not have leading zeros unless it is "0".
        # 3. It is between 0 and 255.
        return len(segment) > 0 and (segment == "0" or segment[0] != "0") and 0 <= int(segment) <= 255

    def backtrack(start: int, path: list[str]):
        # If we have 4 segments and we've used all characters in the string, it's a valid IP.
        if len(path) == 4:
            if start == len(s):
                result.append(".".join(path))
            return

        # Try to form segments of length 1 to 3.
        for length in range(1, 4):
            if start + length <= len(s):  # Ensure we don't go out of bounds.
                segment = s[start:start + length]
                if is_valid(segment):
                    backtrack(start + length, path + [segment])

    result = []
    backtrack(0, [])
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "25525511135"
    print(restore_ip_addresses(s1))  # Expected Output: ["255.255.11.135", "255.255.111.35"]

    # Test Case 2
    s2 = "0000"
    print(restore_ip_addresses(s2))  # Expected Output: ["0.0.0.0"]

    # Test Case 3
    s3 = "101023"
    print(restore_ip_addresses(s3))  # Expected Output: ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The backtracking function explores all possible ways to split the string into 4 segments.
- For each segment, we try lengths of 1, 2, and 3, leading to a branching factor of 3.
- The maximum depth of recursion is 4 (since we need exactly 4 segments).
- Therefore, the time complexity is approximately O(3^4 * n), where n is the length of the string.

Space Complexity:
- The space complexity is O(4) for the recursion stack (maximum depth of 4) and O(k) for storing the result, where k is the number of valid IP addresses.
- Thus, the overall space complexity is O(k + 4).
"""

# Topic: Backtracking