"""
LeetCode Problem #751: IP to CIDR

Problem Statement:
Given a start IP address `ip` and a number of IPs we need to cover `n`, return a list of CIDR (Classless Inter-Domain Routing) blocks that cover all the IPs. A CIDR block is a way to specify a range of IP addresses using a combination of an IP address and a prefix length.

The range of IPs is inclusive, i.e., the range starts from `ip` and includes `n` IPs.

You may return the CIDR blocks in any order. The final output should cover exactly `n` IPs.

Constraints:
- The input IP address `ip` is a valid IPv4 address.
- `n` is an integer in the range `[1, 10^9]`.

Example:
Input: ip = "192.168.1.0", n = 4
Output: ["192.168.1.0/30"]

Input: ip = "192.168.1.0", n = 8
Output: ["192.168.1.0/29"]

Input: ip = "192.168.1.0", n = 16
Output: ["192.168.1.0/28"]
"""

from typing import List

def ip_to_cidr(ip: str, n: int) -> List[str]:
    def ip_to_int(ip: str) -> int:
        """Convert an IP address to its integer representation."""
        parts = map(int, ip.split('.'))
        return sum(part << (8 * (3 - i)) for i, part in enumerate(parts))

    def int_to_ip(num: int) -> str:
        """Convert an integer to its IP address representation."""
        return '.'.join(str((num >> (8 * i)) & 255) for i in range(3, -1, -1))

    def largest_power_of_two(x: int) -> int:
        """Find the largest power of 2 less than or equal to x."""
        return 1 << (x.bit_length() - 1)

    start = ip_to_int(ip)
    result = []

    while n > 0:
        # Find the largest power of 2 that fits in the current range
        max_mask = 32 - (start & -start).bit_length()
        max_range = largest_power_of_two(n)
        mask = 32 - max_range.bit_length()

        # Use the smaller mask to ensure we don't exceed the range
        mask = max(mask, max_mask)
        result.append(f"{int_to_ip(start)}/{mask}")

        # Update the start and remaining count
        covered = 1 << (32 - mask)
        start += covered
        n -= covered

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ip1 = "192.168.1.0"
    n1 = 4
    print(ip_to_cidr(ip1, n1))  # Output: ["192.168.1.0/30"]

    # Test Case 2
    ip2 = "192.168.1.0"
    n2 = 8
    print(ip_to_cidr(ip2, n2))  # Output: ["192.168.1.0/29"]

    # Test Case 3
    ip3 = "192.168.1.0"
    n3 = 16
    print(ip_to_cidr(ip3, n3))  # Output: ["192.168.1.0/28"]

    # Test Case 4
    ip4 = "255.255.255.0"
    n4 = 2
    print(ip_to_cidr(ip4, n4))  # Output: ["255.255.255.0/31"]

    # Test Case 5
    ip5 = "0.0.0.0"
    n5 = 1
    print(ip_to_cidr(ip5, n5))  # Output: ["0.0.0.0/32"]

"""
Time Complexity:
- The while loop runs until `n` becomes 0. In each iteration, the number of IPs covered doubles, so the number of iterations is approximately O(log(n)).
- Each iteration involves constant-time operations (bit manipulation, string formatting, etc.).
- Overall time complexity: O(log(n)).

Space Complexity:
- The space used is primarily for the result list, which stores the CIDR blocks. The number of blocks is proportional to O(log(n)).
- Overall space complexity: O(log(n)).

Topic: Bit Manipulation, Math
"""