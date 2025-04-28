"""
LeetCode Problem #2695: Array Wrapper

Problem Statement:
Create a class `ArrayWrapper` that accepts an array of integers in its constructor. This class should have two features:

1. When two instances of `ArrayWrapper` are added together using the `+` operator, the result should be the sum of all the elements in both arrays.
2. When an instance of `ArrayWrapper` is converted to a string using `str()`, it should return the array in string format as it would appear in Python (e.g., `[1,2,3]`).

Example:
    obj1 = ArrayWrapper([1, 2])
    obj2 = ArrayWrapper([3, 4])
    print(obj1 + obj2)  # Output: 10
    print(str(obj1))    # Output: [1,2]
    print(str(obj2))    # Output: [3,4]

Constraints:
- The array passed to the constructor will only contain integers.
- The length of the array will be in the range [0, 1000].
- The sum of the integers in the array will be in the range [-10^6, 10^6].
"""

# Solution
class ArrayWrapper:
    def __init__(self, nums):
        """
        Initialize the ArrayWrapper with a list of integers.
        """
        self.nums = nums

    def __add__(self, other):
        """
        Overload the + operator to return the sum of all elements in both arrays.
        """
        return sum(self.nums) + sum(other.nums)

    def __str__(self):
        """
        Overload the str() function to return the array in string format.
        """
        return str(self.nums)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    obj1 = ArrayWrapper([1, 2])
    obj2 = ArrayWrapper([3, 4])
    print(obj1 + obj2)  # Output: 10
    print(str(obj1))    # Output: [1,2]
    print(str(obj2))    # Output: [3,4]

    # Test Case 2
    obj3 = ArrayWrapper([])
    obj4 = ArrayWrapper([5, -5])
    print(obj3 + obj4)  # Output: 0
    print(str(obj3))    # Output: []
    print(str(obj4))    # Output: [5,-5]

    # Test Case 3
    obj5 = ArrayWrapper([100, 200, 300])
    obj6 = ArrayWrapper([-100, -200, -300])
    print(obj5 + obj6)  # Output: 0
    print(str(obj5))    # Output: [100,200,300]
    print(str(obj6))    # Output: [-100,-200,-300]

# Time and Space Complexity Analysis
"""
Time Complexity:
- __init__: O(1) (initialization of the object)
- __add__: O(n + m), where n is the length of self.nums and m is the length of other.nums (summing both arrays).
- __str__: O(n), where n is the length of self.nums (converting the array to a string).

Space Complexity:
- __init__: O(1) (storing a reference to the input array).
- __add__: O(1) (no additional space is used apart from the input arrays).
- __str__: O(n), where n is the length of self.nums (space required for the string representation).

Overall:
- Time Complexity: O(n + m) for addition, O(n) for string conversion.
- Space Complexity: O(n) for string conversion.

Topic: Object-Oriented Programming (OOP)
"""