"""
LeetCode Problem #423: Reconstruct Original Digits from English

Problem Statement:
Given a string `s` containing an out-of-order English representation of digits 0-9, 
return the digits in ascending order.

The English words for digits are:
- "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"

Example:
Input: s = "owoztneoer"
Output: "012"

Input: s = "fviefuro"
Output: "45"

Constraints:
- 1 <= s.length <= 10^5
- `s` contains only lowercase English letters.
- It is guaranteed that `s` is valid and can be rearranged to form the English words for digits 0-9.
"""

def originalDigits(s: str) -> str:
    # Count the frequency of each letter in the input string
    from collections import Counter
    count = Counter(s)
    
    # Array to store the count of each digit
    digit_count = [0] * 10
    
    # Unique letters for certain digits
    digit_count[0] = count['z']  # "zero" has a unique 'z'
    digit_count[2] = count['w']  # "two" has a unique 'w'
    digit_count[4] = count['u']  # "four" has a unique 'u'
    digit_count[6] = count['x']  # "six" has a unique 'x'
    digit_count[8] = count['g']  # "eight" has a unique 'g'
    
    # Letters that appear in multiple digits
    digit_count[1] = count['o'] - digit_count[0] - digit_count[2] - digit_count[4]  # "one"
    digit_count[3] = count['h'] - digit_count[8]  # "three"
    digit_count[5] = count['f'] - digit_count[4]  # "five"
    digit_count[7] = count['s'] - digit_count[6]  # "seven"
    digit_count[9] = count['i'] - digit_count[5] - digit_count[6] - digit_count[8]  # "nine"
    
    # Construct the result string
    result = []
    for i in range(10):
        result.append(str(i) * digit_count[i])
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "owoztneoer"
    print(originalDigits(s1))  # Output: "012"

    # Test Case 2
    s2 = "fviefuro"
    print(originalDigits(s2))  # Output: "45"

    # Test Case 3
    s3 = "nnei"
    print(originalDigits(s3))  # Output: "9"

    # Test Case 4
    s4 = "egithreezro"
    print(originalDigits(s4))  # Output: "0138"

"""
Time Complexity Analysis:
- Counting the frequency of letters in the input string takes O(n), where n is the length of the string.
- Calculating the digit counts involves a constant number of operations (since there are only 10 digits), which is O(1).
- Constructing the result string involves iterating over the digit counts, which is also O(1) since the number of digits is fixed.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The Counter object uses O(26) space to store the frequency of each letter (constant space since there are only 26 letters in the English alphabet).
- The digit_count array uses O(10) space (constant space for 10 digits).
- Overall space complexity: O(1) (constant space).

Topic: Strings
"""