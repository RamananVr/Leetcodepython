"""
LeetCode Problem #170: Two Sum III - Data structure design

Problem Statement:
Design and implement a TwoSum class. It should support the following operations: `add` and `find`.

1. `add(number)` - Add the number to an internal data structure.
2. `find(value)` - Find if there exists any pair of numbers which sum is equal to the value.

Example:
    add(1); add(3); add(5);
    find(4) -> True (1 + 3 = 4)
    find(7) -> False (No two numbers sum up to 7)

Constraints:
- The `add` and `find` methods should be optimized for multiple calls.
- The numbers added can be negative, zero, or positive.
"""

class TwoSum:
    def __init__(self):
        """
        Initialize the data structure.
        """
        self.num_counts = {}

    def add(self, number: int) -> None:
        """
        Add the number to the internal data structure.
        """
        if number in self.num_counts:
            self.num_counts[number] += 1
        else:
            self.num_counts[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.num_counts:
            complement = value - num
            if complement in self.num_counts:
                # If complement is the same as num, ensure there are at least two occurrences
                if complement == num and self.num_counts[num] > 1:
                    return True
                elif complement != num:
                    return True
        return False


# Example Test Cases
if __name__ == "__main__":
    ts = TwoSum()
    ts.add(1)
    ts.add(3)
    ts.add(5)
    
    # Test Case 1
    print(ts.find(4))  # Output: True (1 + 3 = 4)
    
    # Test Case 2
    print(ts.find(7))  # Output: False (No two numbers sum up to 7)
    
    # Test Case 3
    ts.add(3)
    print(ts.find(6))  # Output: True (3 + 3 = 6)
    
    # Test Case 4
    ts.add(-1)
    print(ts.find(2))  # Output: True (-1 + 3 = 2)
    
    # Test Case 5
    print(ts.find(10))  # Output: False (No two numbers sum up to 10)


"""
Time and Space Complexity Analysis:

1. `add(number)`:
   - Time Complexity: O(1) - Adding a number to the dictionary is an O(1) operation.
   - Space Complexity: O(1) per call - The space used depends on the number of unique numbers added.

2. `find(value)`:
   - Time Complexity: O(n) - We iterate through the keys of the dictionary to check for pairs.
   - Space Complexity: O(1) - No additional space is used apart from the dictionary.

Overall:
- Time Complexity: O(1) for `add` and O(n) for `find`.
- Space Complexity: O(n), where n is the number of unique numbers added.

Topic: Hash Table
"""