"""
LeetCode Problem #826: Most Profit Assigning Work

Problem Statement:
You have `n` jobs and `m` workers. Each job has a difficulty level and a profit associated with it. 
Each worker has a skill level, and a worker can only complete a job if their skill level is greater 
than or equal to the job's difficulty level. Every worker can complete at most one job, and they 
earn the profit associated with that job.

Given two lists `difficulty` and `profit` of length `n`, representing the difficulty and profit of 
each job, and a list `worker` of length `m`, representing the skill level of each worker, return 
the maximum profit we can achieve.

Constraints:
- `n == difficulty.length == profit.length`
- `1 <= n, m <= 10^4`
- `1 <= difficulty[i], profit[i], worker[j] <= 10^5`

Example:
Input: difficulty = [2, 4, 6, 8, 10], profit = [10, 20, 30, 40, 50], worker = [4, 5, 6, 7]
Output: 100
Explanation: Workers can complete jobs as follows:
- Worker with skill 4 can complete job with difficulty 4 (profit = 20).
- Worker with skill 5 can complete job with difficulty 4 (profit = 20).
- Worker with skill 6 can complete job with difficulty 6 (profit = 30).
- Worker with skill 7 can complete job with difficulty 6 (profit = 30).
Total profit = 20 + 20 + 30 + 30 = 100.
"""

# Python Solution
def maxProfitAssignment(difficulty, profit, worker):
    # Combine difficulty and profit into a list of tuples and sort by difficulty
    jobs = sorted(zip(difficulty, profit))
    worker.sort()
    
    max_profit = 0
    total_profit = 0
    job_index = 0
    
    # Iterate through each worker
    for skill in worker:
        # Update max_profit for jobs the worker can complete
        while job_index < len(jobs) and jobs[job_index][0] <= skill:
            max_profit = max(max_profit, jobs[job_index][1])
            job_index += 1
        # Add the best profit the worker can achieve
        total_profit += max_profit
    
    return total_profit

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    difficulty = [2, 4, 6, 8, 10]
    profit = [10, 20, 30, 40, 50]
    worker = [4, 5, 6, 7]
    print(maxProfitAssignment(difficulty, profit, worker))  # Output: 100

    # Test Case 2
    difficulty = [85, 47, 57]
    profit = [24, 66, 99]
    worker = [40, 25, 25]
    print(maxProfitAssignment(difficulty, profit, worker))  # Output: 0

    # Test Case 3
    difficulty = [1, 2, 3, 4, 5]
    profit = [5, 10, 15, 20, 25]
    worker = [1, 2, 3, 4, 5]
    print(maxProfitAssignment(difficulty, profit, worker))  # Output: 75

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the jobs list takes O(n log n), where n is the number of jobs.
- Sorting the worker list takes O(m log m), where m is the number of workers.
- Iterating through the workers and updating the max_profit takes O(n + m).
Overall time complexity: O(n log n + m log m).

Space Complexity:
- The space required for the jobs list is O(n).
- Sorting operations use O(n) and O(m) space for the jobs and worker lists, respectively.
Overall space complexity: O(n + m).

Topic: Sorting, Greedy
"""