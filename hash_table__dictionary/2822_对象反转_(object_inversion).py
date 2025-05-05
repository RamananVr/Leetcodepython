# LeetCode Problem #2822: 对象反转 (Object Inversion)
# Given an object `obj`, return an inverted object `invertedObj`.
# `invertedObj` should use the keys of `obj` as values and the values of `obj` as keys.
# If there are duplicate values in `obj`, the corresponding key in `invertedObj` should map to an array of all keys.

class Solution:
    def invertObject(self, obj: dict) -> dict:
        """
        Inverts the given object such that keys become values and values become keys.
        If multiple keys have the same value, the inverted object will map the value to a list of keys.

        :param obj: Dictionary to be inverted
        :return: Inverted dictionary
        """
        invertedObj = {}
        for key, value in obj.items():
            if value not in invertedObj:
                invertedObj[value] = key
            else:
                # If the value already exists, convert it to a list or append to the existing list
                if isinstance(invertedObj[value], list):
                    invertedObj[value].append(key)
                else:
                    invertedObj[value] = [invertedObj[value], key]
        return invertedObj

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    obj1 = {"a": "1", "b": "2", "c": "1"}
    # Expected Output: {"1": ["a", "c"], "2": "b"}
    print(solution.invertObject(obj1))

    # Test Case 2
    obj2 = {"x": "apple", "y": "banana", "z": "apple"}
    # Expected Output: {"apple": ["x", "z"], "banana": "y"}
    print(solution.invertObject(obj2))

    # Test Case 3
    obj3 = {"key1": "value1", "key2": "value2", "key3": "value3"}
    # Expected Output: {"value1": "key1", "value2": "key2", "value3": "key3"}
    print(solution.invertObject(obj3))

    # Test Case 4
    obj4 = {"a": "x", "b": "x", "c": "x"}
    # Expected Output: {"x": ["a", "b", "c"]}
    print(solution.invertObject(obj4))

# Time Complexity Analysis:
# The function iterates through all key-value pairs in the input dictionary `obj`.
# For each key-value pair, it performs constant-time operations (checking membership, appending to a list, etc.).
# Therefore, the time complexity is O(n), where n is the number of key-value pairs in `obj`.

# Space Complexity Analysis:
# The space complexity is O(n) as we are creating a new dictionary `invertedObj` to store the inverted mappings.
# In the worst case, if all values in `obj` are unique, the size of `invertedObj` will be the same as `obj`.

# Topic: Hash Table / Dictionary