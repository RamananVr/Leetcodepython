"""
LeetCode Problem #1352: Product of the Last K Numbers

Problem Statement:
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the `ProductOfNumbers` class:
- `ProductOfNumbers()` Initializes the object with an empty stream.
- `void add(int num)` Adds the integer `num` to the stream.
- `int getProduct(int k)` Returns the product of the last `k` numbers in the current list. You can assume that always the last `k` numbers will exist when calling `getProduct`.

The product of any sequence of numbers including zero is defined to be 0.

Example:
Input:
["ProductOfNumbers", "add", "add", "add", "add", "add", "getProduct", "getProduct", "getProduct", "add", "getProduct"]
[[], [3], [0], [2], [5], [4], [2], [3], [4], [8], [2]]

Output:
[null, null, null, null, null, null, 20, 40, 0, null, 32]

Explanation:
ProductOfNumbers productOfNumbers = new ProductOfNumbers();
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3, 0]
productOfNumbers.add(2);        // [3, 0, 2]
productOfNumbers.add(5);        // [3, 0, 2, 5]
productOfNumbers.add(4);        // [3, 0, 2, 5, 4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
productOfNumbers.add(8);        // [3, 0, 2, 5, 4, 8]
productOfNumbers.getProduct(2); // return 32. The product of the last 2 numbers is 4 * 8 = 32
"""

# Python Solution
class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Initialize with 1 for easier calculations

    def add(self, num: int) -> None:
        if num == 0:
            # Reset the prefix product list when a zero is added
            self.prefix_products = [1]
        else:
            # Append the product of the current number with the last prefix product
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            # If k exceeds the range of valid prefix products, it means a zero was added
            return 0
        # Calculate the product of the last k numbers using prefix products
        return self.prefix_products[-1] // self.prefix_products[-k - 1]


# Example Test Cases
if __name__ == "__main__":
    productOfNumbers = ProductOfNumbers()
    productOfNumbers.add(3)  # [3]
    productOfNumbers.add(0)  # [3, 0]
    productOfNumbers.add(2)  # [3, 0, 2]
    productOfNumbers.add(5)  # [3, 0, 2, 5]
    productOfNumbers.add(4)  # [3, 0, 2, 5, 4]
    assert productOfNumbers.getProduct(2) == 20  # 5 * 4 = 20
    assert productOfNumbers.getProduct(3) == 40  # 2 * 5 * 4 = 40
    assert productOfNumbers.getProduct(4) == 0   # 0 * 2 * 5 * 4 = 0
    productOfNumbers.add(8)  # [3, 0, 2, 5, 4, 8]
    assert productOfNumbers.getProduct(2) == 32  # 4 * 8 = 32
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `add(num)`: O(1) - Adding a number involves appending to the prefix product list.
   - `getProduct(k)`: O(1) - Retrieving the product involves a single division operation.

2. Space Complexity:
   - O(n) - The space used by the `prefix_products` list, where `n` is the number of elements added.

Topic: Prefix Product, Arrays
"""