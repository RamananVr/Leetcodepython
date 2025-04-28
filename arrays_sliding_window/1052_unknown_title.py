"""
LeetCode Problem #1052: Grumpy Bookstore Owner

Problem Statement:
Today, the bookstore owner has a store open for customers. However, there are moments when the owner is grumpy. 
The owner can keep themselves not grumpy for X minutes straight by using a special technique. 

Given two integer arrays `customers` and `grumpy`, and an integer `X`:
- `customers[i]` is the number of customers in the store at the i-th minute.
- `grumpy[i]` is 1 if the owner is grumpy at the i-th minute, and 0 otherwise.

When the owner is not grumpy, they will serve all the customers at that minute. 
When the owner is grumpy, they will not serve the customers at that minute unless they use the special technique.

Your task is to return the maximum number of customers that can be served if the owner uses the special technique optimally.

Constraints:
- `n == len(customers) == len(grumpy)`
- `1 <= n <= 20000`
- `0 <= customers[i] <= 1000`
- `0 <= X <= n`
"""

def maxSatisfied(customers, grumpy, X):
    """
    Calculate the maximum number of satisfied customers.

    :param customers: List[int] - Number of customers at each minute.
    :param grumpy: List[int] - Grumpy status of the owner at each minute.
    :param X: int - Duration of the special technique.
    :return: int - Maximum number of satisfied customers.
    """
    # Base satisfied customers when the owner is not grumpy
    base_satisfied = sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0)
    
    # Additional customers that can be satisfied using the special technique
    max_extra_satisfied = 0
    current_extra_satisfied = 0
    
    # Sliding window to calculate the extra satisfied customers for a window of size X
    for i in range(len(customers)):
        if grumpy[i] == 1:
            current_extra_satisfied += customers[i]
        
        # Shrink the window if it exceeds size X
        if i >= X and grumpy[i - X] == 1:
            current_extra_satisfied -= customers[i - X]
        
        # Update the maximum extra satisfied customers
        max_extra_satisfied = max(max_extra_satisfied, current_extra_satisfied)
    
    return base_satisfied + max_extra_satisfied

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    X = 3
    print(maxSatisfied(customers, grumpy, X))  # Expected Output: 16

    # Test Case 2
    customers = [4, 10, 10]
    grumpy = [1, 1, 0]
    X = 2
    print(maxSatisfied(customers, grumpy, X))  # Expected Output: 24

    # Test Case 3
    customers = [2, 6, 6, 9]
    grumpy = [0, 1, 1, 0]
    X = 1
    print(maxSatisfied(customers, grumpy, X))  # Expected Output: 17

    # Test Case 4
    customers = [1, 2, 3, 4, 5]
    grumpy = [1, 1, 1, 1, 1]
    X = 2
    print(maxSatisfied(customers, grumpy, X))  # Expected Output: 9

"""
Time Complexity:
- O(n), where n is the length of the `customers` array. 
  We iterate through the array once to calculate the base satisfied customers and use a sliding window to calculate the extra satisfied customers.

Space Complexity:
- O(1), as we use a constant amount of extra space.

Topic: Arrays, Sliding Window
"""