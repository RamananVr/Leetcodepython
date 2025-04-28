"""
LeetCode Problem #1773: Count Items Matching a Rule

Problem Statement:
You are given an array `items`, where each `items[i] = [type_i, color_i, name_i]` describes the type, color, and name of the i-th item. 
You are also given a rule represented by two strings, `ruleKey` and `ruleValue`.

The rule is applied as follows:
- If `ruleKey == "type"`, then you need to match `ruleValue` with `type_i`.
- If `ruleKey == "color"`, then you need to match `ruleValue` with `color_i`.
- If `ruleKey == "name"`, then you need to match `ruleValue` with `name_i`.

Return the number of items that match the given rule.

Constraints:
- 1 <= items.length <= 10^4
- 1 <= type_i.length, color_i.length, name_i.length, ruleValue.length <= 10
- All strings consist only of lowercase letters.

Example:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].
"""

# Clean, Correct Python Solution
def countMatches(items, ruleKey, ruleValue):
    # Map ruleKey to the corresponding index in the item list
    key_to_index = {"type": 0, "color": 1, "name": 2}
    index = key_to_index[ruleKey]
    
    # Count items that match the rule
    return sum(1 for item in items if item[index] == ruleValue)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    items1 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey1 = "color"
    ruleValue1 = "silver"
    print(countMatches(items1, ruleKey1, ruleValue1))  # Output: 1

    # Test Case 2
    items2 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey2 = "type"
    ruleValue2 = "phone"
    print(countMatches(items2, ruleKey2, ruleValue2))  # Output: 2

    # Test Case 3
    items3 = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
    ruleKey3 = "name"
    ruleValue3 = "iphone"
    print(countMatches(items3, ruleKey3, ruleValue3))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `items` list once, checking the value at the specified index for each item.
- Let n be the number of items in the list. The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space (the dictionary `key_to_index` and the index variable).
- The space complexity is O(1).
"""

# Topic: Arrays