# LeetCode Problem #2823: Minimize XOR

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        """
        Finds the positive integer x such that:
        1. x has the same number of set bits as num2.
        2. The value x XOR num1 is minimal.
        
        :param num1: First positive integer
        :param num2: Second positive integer
        :return: Integer x that satisfies the conditions
        """
        # Count the number of set bits in num2
        num2_set_bits = bin(num2).count('1')
        
        # Start with num1 and try to adjust its bits to match the set bits of num2
        result = 0
        # First, set bits in num1 from left to right to minimize XOR
        for i in range(31, -1, -1):
            if num2_set_bits > 0 and (num1 & (1 << i)):
                result |= (1 << i)
                num2_set_bits -= 1
        
        # If there are still set bits needed, set the lowest unset bits in result
        for i in range(32):
            if num2_set_bits > 0 and not (result & (1 << i)):
                result |= (1 << i)
                num2_set_bits -= 1
        
        return result

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    num1 = 3
    num2 = 5
    # num2 has 2 set bits (binary: 101), so x should have 2 set bits and minimize XOR with num1.
    print(solution.minimizeXor(num1, num2))  # Expected output: 3
    
    # Test Case 2
    num1 = 1
    num2 = 12
    # num2 has 2 set bits (binary: 1100), so x should have 2 set bits and minimize XOR with num1.
    print(solution.minimizeXor(num1, num2))  # Expected output: 3
    
    # Test Case 3
    num1 = 65
    num2 = 7
    # num2 has 3 set bits (binary: 111), so x should have 3 set bits and minimize XOR with num1.
    print(solution.minimizeXor(num1, num2))  # Expected output: 67

# Time Complexity Analysis:
# - Counting set bits in num2 takes O(log(num2)) time.
# - Adjusting bits in num1 to match the set bits of num2 involves iterating over 32 bits, which is O(1).
# - Overall, the time complexity is O(1) since the operations are bounded by the fixed size of integers.

# Space Complexity Analysis:
# - The solution uses a constant amount of extra space, so the space complexity is O(1).

# Topic: Bit Manipulation