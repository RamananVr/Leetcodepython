"""
LeetCode Problem #860: Lemonade Change

Problem Statement:
At a lemonade stand, each lemonade costs $5. Customers are standing in a queue to buy from you, and order one at a time (in the order specified by the bills array). Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill. You must provide the correct change to each customer so that the net transaction is that the customer pays $5.

Note that you don't have any change in hand at first.

Given an integer array `bills` where `bills[i]` is the bill the i-th customer pays, return `true` if you can provide every customer with the correct change, or `false` otherwise.

Constraints:
- `1 <= bills.length <= 10^5`
- `bills[i]` is either `5`, `10`, or `20`.

Example 1:
Input: bills = [5, 5, 5, 10, 20]
Output: true
Explanation:
- From the first 3 customers, we collect three $5 bills in order.
- From the fourth customer, we collect a $10 bill and give back a $5.
- From the fifth customer, we give a $10 bill and a $5 bill.
Since all customers got correct change, we output true.

Example 2:
Input: bills = [5, 5, 10, 10, 20]
Output: false
Explanation:
- From the first two customers, we collect two $5 bills.
- For the next two customers, we collect a $10 bill and give back a $5 bill.
- For the last customer, we can't give the correct change of $15 ($10 + $5) because we only have two $10 bills.
Since not every customer received correct change, the answer is false.

Example 3:
Input: bills = [5, 5, 10]
Output: true

Example 4:
Input: bills = [10, 10]
Output: false

Follow-up:
Could you solve the problem in O(n) time complexity?
"""

def lemonadeChange(bills):
    """
    Determines if we can provide correct change to every customer.

    :param bills: List[int] - List of bills customers pay with.
    :return: bool - True if we can provide correct change to all customers, False otherwise.
    """
    # Initialize counters for $5 and $10 bills
    five_count = 0
    ten_count = 0

    # Iterate through each bill in the input
    for bill in bills:
        if bill == 5:
            # Customer pays with $5, no change needed
            five_count += 1
        elif bill == 10:
            # Customer pays with $10, give back one $5 as change
            if five_count > 0:
                five_count -= 1
                ten_count += 1
            else:
                return False
        elif bill == 20:
            # Customer pays with $20, prioritize giving one $10 and one $5 as change
            if ten_count > 0 and five_count > 0:
                ten_count -= 1
                five_count -= 1
            elif five_count >= 3:
                # If no $10 bill, give three $5 bills as change
                five_count -= 3
            else:
                return False

    # If we successfully provided change to all customers, return True
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bills1 = [5, 5, 5, 10, 20]
    print(lemonadeChange(bills1))  # Output: True

    # Test Case 2
    bills2 = [5, 5, 10, 10, 20]
    print(lemonadeChange(bills2))  # Output: False

    # Test Case 3
    bills3 = [5, 5, 10]
    print(lemonadeChange(bills3))  # Output: True

    # Test Case 4
    bills4 = [10, 10]
    print(lemonadeChange(bills4))  # Output: False

    # Test Case 5
    bills5 = [5, 5, 5, 5, 10, 5, 10, 10, 10, 20]
    print(lemonadeChange(bills5))  # Output: False

"""
Time Complexity Analysis:
- The algorithm iterates through the `bills` array once, performing constant-time operations for each bill.
- Therefore, the time complexity is O(n), where n is the length of the `bills` array.

Space Complexity Analysis:
- The algorithm uses only a constant amount of extra space to store the counts of $5 and $10 bills.
- Therefore, the space complexity is O(1).

Topic: Greedy Algorithm
"""