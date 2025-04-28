"""
LeetCode Problem #1701: Average Waiting Time

Problem Statement:
-------------------
There is a restaurant with a single chef. You are given an array `customers`, where `customers[i] = [arrival_i, time_i]`:
- `arrival_i` is the arrival time of the i-th customer.
- `time_i` is the time needed to prepare the food for the i-th customer.

When a customer arrives, they wait for the chef to finish preparing the food for all previous customers. Once the chef is ready, they immediately begin preparing the food for the current customer. The customer's waiting time is defined as:

    waiting_time_i = (start_time_i + time_i) - arrival_i

Where:
- `start_time_i` is the time at which the chef begins preparing the customer's food.
- The average waiting time of all customers is the sum of their waiting times divided by the total number of customers.

Return the average waiting time of all customers. Answers within 10^-5 of the actual answer are considered correct.

Constraints:
- `1 <= customers.length <= 10^4`
- `1 <= arrival_i, time_i <= 10^4`

"""

def averageWaitingTime(customers):
    """
    Calculate the average waiting time for all customers.

    :param customers: List[List[int]] - A list of customers where each customer is represented as [arrival_i, time_i].
    :return: float - The average waiting time of all customers.
    """
    current_time = 0
    total_waiting_time = 0

    for arrival, time in customers:
        # Update the current time to the maximum of the current time or the customer's arrival time
        current_time = max(current_time, arrival)
        # Calculate the waiting time for the current customer
        waiting_time = (current_time + time) - arrival
        # Update the total waiting time
        total_waiting_time += waiting_time
        # Update the current time to reflect the end of the current customer's service
        current_time += time

    # Calculate and return the average waiting time
    return total_waiting_time / len(customers)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    customers1 = [[1, 2], [2, 5], [4, 3]]
    print(f"Test Case 1: {averageWaitingTime(customers1)}")  # Expected Output: 5.0

    # Test Case 2
    customers2 = [[5, 2], [5, 4], [10, 3]]
    print(f"Test Case 2: {averageWaitingTime(customers2)}")  # Expected Output: 3.66667

    # Test Case 3
    customers3 = [[1, 1]]
    print(f"Test Case 3: {averageWaitingTime(customers3)}")  # Expected Output: 1.0

    # Test Case 4
    customers4 = [[1, 3], [2, 3], [3, 3]]
    print(f"Test Case 4: {averageWaitingTime(customers4)}")  # Expected Output: 4.0


"""
Time and Space Complexity Analysis:
-----------------------------------
Time Complexity:
- The algorithm iterates through the `customers` list once, performing constant-time operations for each customer.
- Therefore, the time complexity is O(n), where n is the number of customers.

Space Complexity:
- The algorithm uses a constant amount of extra space, regardless of the input size.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""