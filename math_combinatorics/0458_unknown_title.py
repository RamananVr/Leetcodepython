"""
LeetCode Problem #458: Poor Pigs

Problem Statement:
There are buckets of liquid, where exactly one of the buckets is poisonous. To figure out which one is poisonous, 
you can feed some number of pigs with the liquid to test it. Each pig can drink from multiple buckets, and the 
test results are returned simultaneously after a fixed time. 

If a pig drinks the poisonous liquid, it will die within a certain time frame. Otherwise, it will survive. 
You are given the following parameters:

- `buckets`: an integer representing the number of buckets.
- `minutesToDie`: an integer representing the time it takes for a pig to die after drinking the poisonous liquid.
- `minutesToTest`: an integer representing the total time you have to test.

Return the minimum number of pigs needed to figure out which bucket is poisonous within the allotted time.

Constraints:
- 1 <= buckets <= 1000
- 1 <= minutesToDie <= minutesToTest <= 100

"""

def poorPigs(buckets: int, minutesToDie: int, minutesToTest: int) -> int:
    """
    Calculate the minimum number of pigs needed to determine the poisonous bucket.
    """
    # Calculate the number of states a pig can represent
    states = minutesToTest // minutesToDie + 1
    
    # Use logarithmic calculation to determine the minimum number of pigs
    pigs = 0
    while (states ** pigs) < buckets:
        pigs += 1
    
    return pigs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60
    print(poorPigs(buckets, minutesToDie, minutesToTest))  # Expected Output: 5

    # Test Case 2
    buckets = 4
    minutesToDie = 15
    minutesToTest = 15
    print(poorPigs(buckets, minutesToDie, minutesToTest))  # Expected Output: 2

    # Test Case 3
    buckets = 1
    minutesToDie = 15
    minutesToTest = 15
    print(poorPigs(buckets, minutesToDie, minutesToTest))  # Expected Output: 0

"""
Time Complexity:
- The time complexity of the solution is O(log(buckets)) because we are iteratively increasing the number of pigs 
  until the condition (states ** pigs >= buckets) is satisfied.

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Math, Combinatorics
"""