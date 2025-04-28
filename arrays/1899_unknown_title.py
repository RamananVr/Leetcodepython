"""
LeetCode Problem #1899: Merge Triplets to Form Target Triplet

Problem Statement:
A triplet is an array of three integers. You are given a 2D integer array `triplets`, where `triplets[i] = [ai, bi, ci]` describes the ith triplet. You are also given an integer array `target = [x, y, z]` that describes the target triplet.

To form the target triplet `[x, y, z]`, you can select some of the triplets and update each element of the target triplet to be the maximum value of that element among the selected triplets. In other words, if you select triplets `triplets[i1], triplets[i2], ..., triplets[ik]`, then:
- `x = max(ai1, ai2, ..., aik)`
- `y = max(bi1, bi2, ..., bik)`
- `z = max(ci1, ci2, ..., cik)`

Return `true` if it is possible to form the target triplet `[x, y, z]` as described above. Otherwise, return `false`.

Constraints:
- `1 <= triplets.length <= 10^5`
- `triplets[i].length == target.length == 3`
- `1 <= ai, bi, ci, x, y, z <= 1000`
"""

def mergeTriplets(triplets, target):
    """
    Determines if the target triplet can be formed by merging triplets.

    Args:
    triplets (List[List[int]]): List of triplets.
    target (List[int]): Target triplet.

    Returns:
    bool: True if the target triplet can be formed, False otherwise.
    """
    x, y, z = target
    found_x, found_y, found_z = False, False, False

    for a, b, c in triplets:
        # Only consider triplets that do not exceed the target values
        if a <= x and b <= y and c <= z:
            if a == x:
                found_x = True
            if b == y:
                found_y = True
            if c == z:
                found_z = True

    # Check if all components of the target triplet are found
    return found_x and found_y and found_z


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    triplets = [[2, 5, 3], [1, 8, 4], [1, 7, 5]]
    target = [2, 7, 5]
    print(mergeTriplets(triplets, target))  # Expected output: True

    # Test Case 2
    triplets = [[1, 3, 4], [2, 5, 8], [1, 7, 5]]
    target = [2, 7, 5]
    print(mergeTriplets(triplets, target))  # Expected output: False

    # Test Case 3
    triplets = [[1, 3, 4], [2, 5, 8], [2, 7, 5]]
    target = [2, 7, 5]
    print(mergeTriplets(triplets, target))  # Expected output: True

    # Test Case 4
    triplets = [[1, 3, 4], [2, 5, 8], [1, 7, 5]]
    target = [3, 7, 5]
    print(mergeTriplets(triplets, target))  # Expected output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the list of triplets once, performing constant-time operations for each triplet.
- Let `n` be the number of triplets. The time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space to store flags (`found_x`, `found_y`, `found_z`).
- The space complexity is O(1).

Topic: Arrays
"""