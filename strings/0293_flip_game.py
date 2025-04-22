"""
LeetCode Question #293: Flip Game

Problem Statement:
You are playing a Flip Game with a string `currentState` that contains only '+' and '-' characters. 
You can flip two consecutive "++" into "--" in one move. 

Write a function to generate all possible states of the string after one valid move. 
You should return them as a list of strings. If there is no valid move, return an empty list.

Example:
Input: currentState = "++++"
Output: ["--++", "+--+", "++--"]

Constraints:
- The input string `currentState` will have a length in the range [1, 50].
- The input string will only contain '+' and '-'.
"""

def generatePossibleNextMoves(currentState: str) -> list:
    """
    Generate all possible states of the string after one valid move.

    :param currentState: A string containing only '+' and '-'.
    :return: A list of strings representing all possible states after one move.
    """
    result = []
    for i in range(len(currentState) - 1):
        # Check for "++" and flip it to "--"
        if currentState[i] == '+' and currentState[i + 1] == '+':
            new_state = currentState[:i] + '--' + currentState[i + 2:]
            result.append(new_state)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    currentState = "++++"
    print("Input:", currentState)
    print("Output:", generatePossibleNextMoves(currentState))  # Expected: ["--++", "+--+", "++--"]

    # Test Case 2
    currentState = "+-++-"
    print("Input:", currentState)
    print("Output:", generatePossibleNextMoves(currentState))  # Expected: ["+----", "+-+--"]

    # Test Case 3
    currentState = "--"
    print("Input:", currentState)
    print("Output:", generatePossibleNextMoves(currentState))  # Expected: []

    # Test Case 4
    currentState = "++"
    print("Input:", currentState)
    print("Output:", generatePossibleNextMoves(currentState))  # Expected: ["--"]

    # Test Case 5
    currentState = "+-"
    print("Input:", currentState)
    print("Output:", generatePossibleNextMoves(currentState))  # Expected: []

"""
Time Complexity Analysis:
- The function iterates through the string once, checking pairs of consecutive characters.
- For each pair, it performs slicing and concatenation, which takes O(n) in the worst case.
- Therefore, the overall time complexity is O(n), where n is the length of the input string.

Space Complexity Analysis:
- The function creates a list to store the results, which in the worst case can contain up to n/2 strings (if all pairs are "++").
- Each string in the result list is of length n.
- Therefore, the space complexity is O(n^2) in the worst case.

Topic: Strings
"""