"""
LeetCode Question #1054: Distant Barcodes

Problem Statement:
In a warehouse, there is a row of barcodes, where the `i-th` barcode is `barcodes[i]`.

Rearrange the barcodes so that no two adjacent barcodes are equal. You may return any answer that satisfies this condition.

Example 1:
Input: barcodes = [1,1,1,2,2,3]
Output: [1,2,1,2,1,3]

Example 2:
Input: barcodes = [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,1,2,1,2]

Constraints:
- `1 <= barcodes.length <= 10000`
- `1 <= barcodes[i] <= 10000`
"""

from collections import Counter
import heapq

def rearrangeBarcodes(barcodes):
    """
    Rearranges the barcodes such that no two adjacent barcodes are the same.

    :param barcodes: List[int] - List of barcodes
    :return: List[int] - Rearranged barcodes
    """
    # Count the frequency of each barcode
    freq = Counter(barcodes)
    
    # Create a max heap based on the frequency of barcodes
    max_heap = [(-count, barcode) for barcode, count in freq.items()]
    heapq.heapify(max_heap)
    
    # Result list to store the rearranged barcodes
    result = []
    
    # Previous barcode and its count (to ensure no adjacent duplicates)
    prev_count, prev_barcode = 0, None
    
    while max_heap:
        # Pop the most frequent barcode
        count, barcode = heapq.heappop(max_heap)
        result.append(barcode)
        
        # If the previous barcode still has remaining count, push it back into the heap
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_barcode))
        
        # Update the previous barcode and its count
        prev_count, prev_barcode = count + 1, barcode  # Decrease count since we used one instance
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    barcodes1 = [1, 1, 1, 2, 2, 3]
    print(rearrangeBarcodes(barcodes1))  # Output: [1, 2, 1, 2, 1, 3]

    # Test Case 2
    barcodes2 = [1, 1, 1, 1, 2, 2, 3, 3]
    print(rearrangeBarcodes(barcodes2))  # Output: [1, 3, 1, 3, 1, 2, 1, 2]

    # Test Case 3
    barcodes3 = [2, 2, 2, 1, 1, 1]
    print(rearrangeBarcodes(barcodes3))  # Output: [2, 1, 2, 1, 2, 1]

    # Test Case 4
    barcodes4 = [1]
    print(rearrangeBarcodes(barcodes4))  # Output: [1]

    # Test Case 5
    barcodes5 = [1, 1, 2]
    print(rearrangeBarcodes(barcodes5))  # Output: [1, 2, 1]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting frequencies using `Counter` takes O(n), where n is the length of the `barcodes` list.
- Creating the max heap takes O(k log k), where k is the number of unique barcodes.
- Rearranging the barcodes involves popping and pushing elements into the heap, which takes O(n log k).
- Overall time complexity: O(n log k), where n is the length of the input and k is the number of unique barcodes.

Space Complexity:
- The `Counter` object and the heap both require O(k) space, where k is the number of unique barcodes.
- The result list requires O(n) space.
- Overall space complexity: O(n + k).

Topic: Greedy, Heap (Priority Queue)
"""