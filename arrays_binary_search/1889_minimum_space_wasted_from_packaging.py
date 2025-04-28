"""
LeetCode Question #1889: Minimum Space Wasted From Packaging

Problem Statement:
You are given an array `packages` representing the weights of the packages you need to deliver, and an array `boxes` where `boxes[i]` is a sorted array of box sizes available in the ith supplier. The packages can only be placed in boxes that are greater than or equal to the size of the package. The cost of packing the packages is the total wasted space in all the boxes.

- If a package cannot be placed in any box, return -1.
- Otherwise, return the minimum total wasted space across all suppliers. Since the answer may be large, return it modulo 10^9 + 7.

Constraints:
- `1 <= packages.length <= 10^5`
- `1 <= boxes.length <= 100`
- `1 <= boxes[i].length <= 10^5`
- `1 <= packages[j], boxes[i][k] <= 10^9`
- All the elements in `boxes[i]` are distinct.
- The elements in `boxes[i]` are sorted in ascending order.

"""

from bisect import bisect_left
from typing import List

def minWastedSpace(packages: List[int], boxes: List[List[int]]) -> int:
    MOD = 10**9 + 7
    packages.sort()
    total_package_weight = sum(packages)
    min_wasted_space = float('inf')
    
    for box_sizes in boxes:
        box_sizes.sort()
        if box_sizes[-1] < packages[-1]:  # If the largest box cannot fit the largest package
            continue
        
        wasted_space = 0
        prev_index = 0
        for box_size in box_sizes:
            index = bisect_left(packages, box_size + 1)
            wasted_space += box_size * (index - prev_index)
            prev_index = index
        
        min_wasted_space = min(min_wasted_space, wasted_space - total_package_weight)
    
    return min_wasted_space % MOD if min_wasted_space != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    packages = [2, 3, 5]
    boxes = [[4, 8], [2, 8]]
    print(minWastedSpace(packages, boxes))  # Expected Output: 6

    # Test Case 2
    packages = [2, 3, 5]
    boxes = [[1, 4], [2, 3, 8]]
    print(minWastedSpace(packages, boxes))  # Expected Output: -1

    # Test Case 3
    packages = [1, 2, 3]
    boxes = [[3, 4, 5], [1, 2, 3]]
    print(minWastedSpace(packages, boxes))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `packages` array takes O(n log n), where n is the number of packages.
- For each supplier's box sizes, sorting takes O(m log m), where m is the number of box sizes.
- For each supplier, we iterate through the box sizes and use binary search (via `bisect_left`) to find the range of packages that can fit in the current box size. This takes O(m log n) for each supplier.
- If there are k suppliers, the total complexity is O(n log n + k * m log n).

Space Complexity:
- Sorting the packages and box sizes is done in-place, so the space complexity is O(1) additional space.
- The function uses a few variables to store intermediate results, so the overall space complexity is O(1).

Topic: Arrays, Binary Search
"""