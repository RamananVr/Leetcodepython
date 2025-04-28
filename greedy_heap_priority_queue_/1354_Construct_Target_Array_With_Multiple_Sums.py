"""
LeetCode Problem #1354: Construct Target Array With Multiple Sums

Problem Statement:
You are given an array `target` of n integers. From a starting array `arr` consisting of n 1's, you may perform the following procedure:

- Choose any index `i` and set `arr[i] = sum(arr)`.

You can repeat this procedure as many times as needed.

Return `True` if it is possible to construct the `target` array from `arr`, otherwise return `False`.

Constraints:
- n == target.length
- 1 <= n <= 5 * 10^4
- 1 <= target[i] <= 10^9
"""

import heapq

def isPossible(target):
    """
    Determines if it is possible to construct the target array from an array of ones.

    :param target: List[int] - The target array
    :return: bool - True if possible, False otherwise
    """
    if len(target) == 1:
        return target[0] == 1

    # Convert target into a max-heap (using negative values for max-heap simulation)
    total_sum = sum(target)
    max_heap = [-x for x in target]
    heapq.heapify(max_heap)

    while True:
        largest = -heapq.heappop(max_heap)  # Get the largest element
        rest_sum = total_sum - largest  # Sum of the rest of the elements

        # If the largest element is 1 or the rest of the sum is 1, we can construct the target
        if largest == 1 or rest_sum == 1:
            return True

        # If the rest_sum is 0 or largest <= rest_sum, it's impossible to construct the target
        if rest_sum == 0 or largest <= rest_sum:
            return False

        # Calculate the new value for the largest element
        new_value = largest % rest_sum

        # If the new value is 0 or doesn't change, it's impossible to proceed
        if new_value == 0:
            return False

        # Update the total sum and push the new value back into the heap
        total_sum = rest_sum + new_value
        heapq.heappush(max_heap, -new_value)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Possible to construct
    target1 = [9, 3, 5]
    print(isPossible(target1))  # Expected output: True

    # Test Case 2: Not possible to construct
    target2 = [1, 1, 1, 2]
    print(isPossible(target2))  # Expected output: False

    # Test Case 3: Single element array
    target3 = [1]
    print(isPossible(target3))  # Expected output: True

    # Test Case 4: Large numbers, possible to construct
    target4 = [8, 5]
    print(isPossible(target4))  # Expected output: True

    # Test Case 5: Large numbers, not possible to construct
    target5 = [2, 900000001]
    print(isPossible(target5))  # Expected output: False

"""
Time Complexity:
- Let n be the length of the target array.
- Each iteration involves extracting the maximum element from the heap (O(log n)) and performing a modulo operation.
- In the worst case, the largest number is repeatedly reduced by the sum of the rest of the array, which can take O(log(max(target))) iterations.
- Overall time complexity: O(n log(max(target))).

Space Complexity:
- The space complexity is O(n) due to the heap storage.

Topic: Greedy, Heap (Priority Queue)
"""