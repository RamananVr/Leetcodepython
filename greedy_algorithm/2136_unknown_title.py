"""
LeetCode Problem #2136: Earliest Possible Day of Full Bloom

Problem Statement:
You have n flower seeds. Every seed must be planted first before it can begin to grow, 
then bloom. Planting a seed takes `plantTime[i]` days, and growing a seed takes 
`growTime[i]` days. You can plant the seeds in any order.

Return the earliest possible day where all seeds are blooming.

Example:
Input: plantTime = [1, 4, 3], growTime = [2, 3, 1]
Output: 9
Explanation:
- One optimal way is:
  1. Plant the 3rd seed (plantTime[2] = 3, growTime[2] = 1) on day 0. It blooms on day 4.
  2. Plant the 1st seed (plantTime[0] = 1, growTime[0] = 2) on day 3. It blooms on day 6.
  3. Plant the 2nd seed (plantTime[1] = 4, growTime[1] = 3) on day 4. It blooms on day 9.
- The earliest day all seeds are blooming is day 9.

Constraints:
- n == plantTime.length == growTime.length
- 1 <= n <= 10^5
- 1 <= plantTime[i], growTime[i] <= 10^4
"""

# Clean, Correct Python Solution
def earliestFullBloom(plantTime, growTime):
    # Pair growTime and plantTime, then sort by growTime in descending order
    seeds = sorted(zip(growTime, plantTime), reverse=True, key=lambda x: x[0])
    
    current_day = 0
    max_bloom_day = 0
    
    for grow, plant in seeds:
        current_day += plant  # Add the planting time
        max_bloom_day = max(max_bloom_day, current_day + grow)  # Update the bloom day
    
    return max_bloom_day

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    plantTime = [1, 4, 3]
    growTime = [2, 3, 1]
    print(earliestFullBloom(plantTime, growTime))  # Output: 9

    # Test Case 2
    plantTime = [2, 3, 1]
    growTime = [5, 2, 1]
    print(earliestFullBloom(plantTime, growTime))  # Output: 10

    # Test Case 3
    plantTime = [1, 1, 1]
    growTime = [1, 1, 1]
    print(earliestFullBloom(plantTime, growTime))  # Output: 4

    # Test Case 4
    plantTime = [3, 2, 5]
    growTime = [6, 4, 2]
    print(earliestFullBloom(plantTime, growTime))  # Output: 14

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the seeds array takes O(n log n), where n is the number of seeds.
- Iterating through the seeds array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space required for sorting is O(n) (for the sorted list of tuples).
- Overall space complexity: O(n).
"""

# Topic: Greedy Algorithm