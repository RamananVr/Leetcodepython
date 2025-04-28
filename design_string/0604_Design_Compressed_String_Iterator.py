"""
LeetCode Problem #604: Design Compressed String Iterator

Problem Statement:
Design and implement a data structure for a compressed string iterator. It should support the following operations: `next` and `hasNext`.

The given compressed string will be in the form of a string where each character is followed by a positive integer representing the number of times the character appears in the uncompressed string.

- `next()`: If the original string still has uncompressed characters, this method should return the next character. Otherwise, it should return a single space `' '`.
- `hasNext()`: This method should return `True` if there is any uncompressed character left in the original string, otherwise it should return `False`.

Constraints:
1. The compressed string will only contain uppercase English letters and digits.
2. The number of characters in the original string is at most 1000.
3. At most 100 calls will be made to `next` and `hasNext`.

Example:
CompressedStringIterator iterator = new CompressedStringIterator("L1e2t1C1o1d1e1");

iterator.next();    // return 'L'
iterator.next();    // return 'e'
iterator.next();    // return 'e'
iterator.hasNext(); // return True
iterator.next();    // return 't'
iterator.hasNext(); // return True
iterator.next();    // return 'C'
iterator.hasNext(); // return True
iterator.next();    // return 'o'
iterator.hasNext(); // return True
iterator.next();    // return 'd'
iterator.hasNext(); // return True
iterator.next();    // return 'e'
iterator.hasNext(); // return False
iterator.next();    // return ' '
"""

class StringIterator:
    def __init__(self, compressedString: str):
        """
        Initialize the iterator with the compressed string.
        """
        self.chars = []
        self.counts = []
        self.index = 0  # Pointer to the current character
        self.remaining = 0  # Remaining count of the current character

        # Parse the compressed string
        i = 0
        while i < len(compressedString):
            char = compressedString[i]
            i += 1
            num_start = i
            while i < len(compressedString) and compressedString[i].isdigit():
                i += 1
            count = int(compressedString[num_start:i])
            self.chars.append(char)
            self.counts.append(count)

    def next(self) -> str:
        """
        Return the next character in the uncompressed string.
        If no characters are left, return a single space ' '.
        """
        if not self.hasNext():
            return ' '

        if self.remaining == 0:
            self.remaining = self.counts[self.index]
        
        self.remaining -= 1
        result = self.chars[self.index]

        if self.remaining == 0:
            self.index += 1

        return result

    def hasNext(self) -> bool:
        """
        Return True if there are uncompressed characters left, otherwise False.
        """
        return self.index < len(self.chars) or self.remaining > 0


# Example Test Cases
if __name__ == "__main__":
    iterator = StringIterator("L1e2t1C1o1d1e1")

    print(iterator.next())    # Output: 'L'
    print(iterator.next())    # Output: 'e'
    print(iterator.next())    # Output: 'e'
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 't'
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 'C'
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 'o'
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 'd'
    print(iterator.hasNext()) # Output: True
    print(iterator.next())    # Output: 'e'
    print(iterator.hasNext()) # Output: False
    print(iterator.next())    # Output: ' '


# Time and Space Complexity Analysis
# Time Complexity:
# - The constructor (`__init__`) parses the compressed string in O(n), where n is the length of the compressed string.
# - The `next` and `hasNext` methods operate in O(1) time.

# Space Complexity:
# - The space complexity is O(k), where k is the number of unique characters in the compressed string. This is because we store the characters and their counts in separate lists.

# Topic: Design, String