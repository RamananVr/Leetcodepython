"""
LeetCode Problem #1656: Design an Ordered Stream

Problem Statement:
There is a stream of `n` (1-indexed) integers that you need to process. You are given a class `OrderedStream` that:

- Initializes the object with an integer `n` representing the number of elements in the stream.
- Has a function `insert(int idKey, String value)` that inserts the pair `(idKey, value)` into the stream, then returns the largest possible chunk of currently consecutive values (starting from the pointer).

Implement the `OrderedStream` class:
1. `OrderedStream(int n)` Initializes the object with a stream of size `n`.
2. `List<String> insert(int idKey, String value)` Inserts the pair `(idKey, value)` into the stream, then returns the largest possible list of consecutive values that appear in the stream (starting from the current pointer).

Constraints:
- `1 <= n <= 1000`
- `1 <= id <= n`
- `value` consists only of lowercase English letters.
- Each call to `insert(idKey, value)` will have a unique `idKey`.
- Exactly `n` calls will be made to `insert`.

Example:
Input:
    ["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
    [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output:
    [null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation:
    OrderedStream os = new OrderedStream(5);
    os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
    os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
    os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
    os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
    os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
"""

# Python Solution
class OrderedStream:
    def __init__(self, n: int):
        # Initialize the stream with None values and set the pointer to 0
        self.stream = [None] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> list:
        # Insert the value at the correct index (convert 1-indexed to 0-indexed)
        self.stream[idKey - 1] = value
        result = []

        # Collect consecutive values starting from the pointer
        while self.pointer < len(self.stream) and self.stream[self.pointer] is not None:
            result.append(self.stream[self.pointer])
            self.pointer += 1

        return result


# Example Test Cases
if __name__ == "__main__":
    # Initialize the OrderedStream with size 5
    os = OrderedStream(5)

    # Test case 1
    print(os.insert(3, "ccccc"))  # Output: []

    # Test case 2
    print(os.insert(1, "aaaaa"))  # Output: ["aaaaa"]

    # Test case 3
    print(os.insert(2, "bbbbb"))  # Output: ["bbbbb", "ccccc"]

    # Test case 4
    print(os.insert(5, "eeeee"))  # Output: []

    # Test case 5
    print(os.insert(4, "ddddd"))  # Output: ["ddddd", "eeeee"]


# Time and Space Complexity Analysis
"""
Time Complexity:
- The `insert` method iterates through the stream starting from the pointer until it encounters a `None` value.
- In the worst case, the pointer traverses the entire stream once over all `n` calls to `insert`.
- Therefore, the amortized time complexity for each `insert` call is O(1), and the total time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the storage of the stream in a list of size `n`.
"""

# Topic: Arrays