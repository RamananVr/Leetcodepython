"""
LeetCode Question #282: Expression Add Operators

Problem Statement:
Given a string `num` that contains only digits and an integer `target`, return all possible expressions that you can add to the string such that the resulting expression evaluates to the `target`.

You can use the addition ('+'), subtraction ('-'), and multiplication ('*') operators. The input string `num` does not contain any leading zeros.

Example 1:
Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"]

Example 2:
Input: num = "232", target = 8
Output: ["2*3+2", "2+3*2"]

Example 3:
Input: num = "105", target = 5
Output: ["1*0+5", "10-5"]

Example 4:
Input: num = "00", target = 0
Output: ["0+0", "0-0", "0*0"]

Example 5:
Input: num = "3456237490", target = 9191
Output: []

Constraints:
- 1 <= num.length <= 10
- num consists of only digits.
- -2^31 <= target <= 2^31 - 1
"""

# Solution
def addOperators(num: str, target: int):
    def backtrack(index, path, value, prev):
        # Base case: if we've reached the end of the string
        if index == len(num):
            if value == target:
                result.append(path)
            return
        
        for i in range(index, len(num)):
            # Avoid numbers with leading zeros
            if i > index and num[index] == '0':
                break
            
            # Extract the current number
            current = int(num[index:i+1])
            
            # If we're at the start, we can't add an operator
            if index == 0:
                backtrack(i+1, path + str(current), current, current)
            else:
                # Addition
                backtrack(i+1, path + '+' + str(current), value + current, current)
                # Subtraction
                backtrack(i+1, path + '-' + str(current), value - current, -current)
                # Multiplication
                backtrack(i+1, path + '*' + str(current), value - prev + prev * current, prev * current)
    
    result = []
    backtrack(0, "", 0, 0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = "123"
    target = 6
    print(addOperators(num, target))  # Output: ["1+2+3", "1*2*3"]

    # Test Case 2
    num = "232"
    target = 8
    print(addOperators(num, target))  # Output: ["2*3+2", "2+3*2"]

    # Test Case 3
    num = "105"
    target = 5
    print(addOperators(num, target))  # Output: ["1*0+5", "10-5"]

    # Test Case 4
    num = "00"
    target = 0
    print(addOperators(num, target))  # Output: ["0+0", "0-0", "0*0"]

    # Test Case 5
    num = "3456237490"
    target = 9191
    print(addOperators(num, target))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
The time complexity of this solution is O(4^n), where n is the length of the input string `num`. 
This is because at each step, we have three choices for operators (+, -, *) and one choice to skip adding an operator, 
resulting in 4 possible paths for each digit.

Space Complexity:
The space complexity is O(n), where n is the length of the input string `num`. 
This is due to the recursion stack and the storage of intermediate paths.

Topic: Backtracking
"""