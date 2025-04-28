"""
LeetCode Problem #1310: XOR Queries of a Subarray

Problem Statement:
Given the array `arr` of positive integers and the array `queries` where `queries[i] = [Li, Ri]`, 
for each query `i` compute the XOR of elements from `Li` to `Ri` (that is, `arr[Li] XOR arr[Li+1] XOR ... XOR arr[Ri]`). 
Return an array containing the result for the given `queries`.

Example:
Input: arr = [1,3,4,8], queries = [[0,1],[1,2],[0,3],[3,3]]
Output: [2,7,14,8]
Explanation:
- The XOR of elements from 0 to 1 is 1 XOR 3 = 2.
- The XOR of elements from 1 to 2 is 3 XOR 4 = 7.
- The XOR of elements from 0 to 3 is 1 XOR 3 XOR 4 XOR 8 = 14.
- The XOR of elements from 3 to 3 is 8.

Constraints:
1. 1 <= arr.length <= 3 * 10^4
2. 1 <= arr[i] <= 10^9
3. 1 <= queries.length <= 3 * 10^4
4. queries[i].length == 2
5. 0 <= Li <= Ri < arr.length
"""

# Clean and Correct Python Solution
def xorQueries(arr, queries):
    """
    Computes the XOR of elements for each query range in the array.

    :param arr: List[int] - The input array of positive integers.
    :param queries: List[List[int]] - The list of queries, where each query is a range [Li, Ri].
    :return: List[int] - The XOR results for each query.
    """
    # Step 1: Compute the prefix XOR array
    n = len(arr)
    prefix_xor = [0] * (n + 1)
    for i in range(n):
        prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

    # Step 2: Process each query using the prefix XOR array
    result = []
    for Li, Ri in queries:
        result.append(prefix_xor[Ri + 1] ^ prefix_xor[Li])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 3, 4, 8]
    queries1 = [[0, 1], [1, 2], [0, 3], [3, 3]]
    print(xorQueries(arr1, queries1))  # Output: [2, 7, 14, 8]

    # Test Case 2
    arr2 = [4, 8, 2, 10]
    queries2 = [[0, 1], [1, 3], [0, 2], [2, 2]]
    print(xorQueries(arr2, queries2))  # Output: [12, 0, 14, 2]

    # Test Case 3
    arr3 = [5, 1, 7, 3, 9]
    queries3 = [[0, 4], [1, 3], [2, 2], [0, 0]]
    print(xorQueries(arr3, queries3))  # Output: [15, 5, 7, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing the prefix XOR array takes O(n), where n is the length of the input array `arr`.
- Processing each query takes O(1) using the prefix XOR array.
- For `q` queries, the total time complexity is O(n + q).

Space Complexity:
- The prefix XOR array requires O(n) space.
- The result array requires O(q) space.
- Overall space complexity is O(n + q).

Primary Topic: Arrays, Prefix XOR
"""