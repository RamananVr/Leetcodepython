"""
LeetCode Problem #605: Can Place Flowers

Problem Statement:
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer `n`, return if `n` new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Constraints:
- 1 <= flowerbed.length <= 2 * 10^4
- flowerbed[i] is 0 or 1.
- There are no two adjacent flowers in the initial flowerbed.
- 0 <= n <= flowerbed.length
"""

def canPlaceFlowers(flowerbed, n):
    """
    Determines if `n` flowers can be planted in the given flowerbed without violating the no-adjacent-flowers rule.

    :param flowerbed: List[int] - A list representing the flowerbed (0 = empty, 1 = planted).
    :param n: int - The number of flowers to plant.
    :return: bool - True if `n` flowers can be planted, False otherwise.
    """
    count = 0
    length = len(flowerbed)
    
    for i in range(length):
        if flowerbed[i] == 0:
            # Check if the previous and next plots are empty or out of bounds
            prev_empty = (i == 0) or (flowerbed[i - 1] == 0)
            next_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
            
            if prev_empty and next_empty:
                flowerbed[i] = 1  # Plant a flower here
                count += 1
                if count >= n:
                    return True
    
    return count >= n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    flowerbed = [1, 0, 0, 0, 1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))  # Expected Output: True

    # Test Case 2
    flowerbed = [1, 0, 0, 0, 1]
    n = 2
    print(canPlaceFlowers(flowerbed, n))  # Expected Output: False

    # Test Case 3
    flowerbed = [0, 0, 1, 0, 0]
    n = 2
    print(canPlaceFlowers(flowerbed, n))  # Expected Output: True

    # Test Case 4
    flowerbed = [0]
    n = 1
    print(canPlaceFlowers(flowerbed, n))  # Expected Output: True

    # Test Case 5
    flowerbed = [1, 0, 0, 0, 0, 1]
    n = 1
    print(canPlaceFlowers(flowerbed, n))  # Expected Output: True

"""
Time Complexity:
- The algorithm iterates through the flowerbed array once, performing constant-time checks and updates for each element.
- Therefore, the time complexity is O(flowerbed.length), or O(n), where n is the length of the flowerbed.

Space Complexity:
- The algorithm modifies the input array in place and uses a constant amount of extra space.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""