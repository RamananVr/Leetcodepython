"""
LeetCode Problem #1196: How Many Apples Can You Put into the Basket

Problem Statement:
You have a basket and a list of apples where each apple has a weight. The basket can carry a maximum weight of 5000 units. 
Given an integer array `arr` where `arr[i]` is the weight of the i-th apple, return the maximum number of apples you can 
put into the basket without exceeding the weight limit.

Constraints:
- 1 <= arr.length <= 10^3
- 1 <= arr[i] <= 10^3
"""

def maxNumberOfApples(arr):
    """
    This function calculates the maximum number of apples that can be put into the basket
    without exceeding the weight limit of 5000 units.

    :param arr: List[int] - List of weights of apples
    :return: int - Maximum number of apples that can fit in the basket
    """
    arr.sort()  # Sort the array to prioritize lighter apples
    total_weight = 0
    count = 0

    for weight in arr:
        if total_weight + weight <= 5000:
            total_weight += weight
            count += 1
        else:
            break

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [100, 200, 150, 1000]
    print(maxNumberOfApples(arr1))  # Expected Output: 4

    # Test Case 2
    arr2 = [900, 950, 800, 1000, 700, 800]
    print(maxNumberOfApples(arr2))  # Expected Output: 5

    # Test Case 3
    arr3 = [5000, 1, 1, 1, 1]
    print(maxNumberOfApples(arr3))  # Expected Output: 4

    # Test Case 4
    arr4 = [1000, 1000, 1000, 1000, 1000, 1000]
    print(maxNumberOfApples(arr4))  # Expected Output: 5

    # Test Case 5
    arr5 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(maxNumberOfApples(arr5))  # Expected Output: 10

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array to calculate the total weight takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring the input array storage).

Topic: Arrays
"""