"""
LeetCode Problem #278: First Bad Version

Problem Statement:
You are a product manager and currently leading a team to develop a new product. 
Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, 
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether version is bad. 
Implement a function to find the first bad version. You should minimize the number of calls to the API.

Constraints:
- 1 <= bad <= n <= 2^31 - 1
"""

# Clean and Correct Python Solution
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def firstBadVersion(n: int) -> int:
    """
    Finds the first bad version using binary search.

    Args:
    n (int): The total number of versions.

    Returns:
    int: The version number of the first bad version.
    """
    left, right = 1, n
    while left < right:
        mid = left + (right - left) // 2
        if isBadVersion(mid):
            right = mid  # Narrow down to the left half
        else:
            left = mid + 1  # Narrow down to the right half
    return left  # At the end, left == right, which is the first bad version

# Example Test Cases
def test_firstBadVersion():
    """
    Test cases for the firstBadVersion function.
    """
    global isBadVersion

    # Test Case 1
    def mock_isBadVersion_1(version):
        return version >= 4
    isBadVersion = mock_isBadVersion_1
    assert firstBadVersion(5) == 4, "Test Case 1 Failed"

    # Test Case 2
    def mock_isBadVersion_2(version):
        return version >= 1
    isBadVersion = mock_isBadVersion_2
    assert firstBadVersion(1) == 1, "Test Case 2 Failed"

    # Test Case 3
    def mock_isBadVersion_3(version):
        return version >= 10
    isBadVersion = mock_isBadVersion_3
    assert firstBadVersion(20) == 10, "Test Case 3 Failed"

    # Test Case 4
    def mock_isBadVersion_4(version):
        return version >= 7
    isBadVersion = mock_isBadVersion_4
    assert firstBadVersion(10) == 7, "Test Case 4 Failed"

    print("All test cases passed!")

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function uses binary search, which divides the search space in half at each step.
- Therefore, the time complexity is O(log n), where n is the total number of versions.

Space Complexity:
- The function uses a constant amount of extra space, as it only uses a few variables (left, right, mid).
- Therefore, the space complexity is O(1).
"""

# Topic: Binary Search

# Run the test cases
if __name__ == "__main__":
    test_firstBadVersion()