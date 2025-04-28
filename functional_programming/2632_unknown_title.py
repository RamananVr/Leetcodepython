"""
LeetCode Problem #2632: Curry Function

Problem Statement:
Create a function `curry` that accepts a function and returns a curried version of that function.
A curried function is a function that takes one argument at a time and returns a new function until all arguments have been provided.

Example:
    const join = (a, b, c) => {
        return `${a}_${b}_${c}`;
    };
    const curriedJoin = curry(join);
    curriedJoin("a")("b")("c"); // "a_b_c"
    curriedJoin("a", "b")("c"); // "a_b_c"
    curriedJoin("a", "b", "c"); // "a_b_c"

Constraints:
- The input function will have a fixed number of parameters.
- The curried function should support partial application.
"""

# Solution
def curry(func):
    def curried(*args):
        if len(args) >= func.__code__.co_argcount:
            return func(*args)
        return lambda *next_args: curried(*(args + next_args))
    return curried

# Example Test Cases
if __name__ == "__main__":
    # Example 1
    def join(a, b, c):
        return f"{a}_{b}_{c}"

    curried_join = curry(join)
    print(curried_join("a")("b")("c"))  # Output: "a_b_c"
    print(curried_join("a", "b")("c"))  # Output: "a_b_c"
    print(curried_join("a", "b", "c"))  # Output: "a_b_c"

    # Example 2
    def add(a, b, c, d):
        return a + b + c + d

    curried_add = curry(add)
    print(curried_add(1)(2)(3)(4))  # Output: 10
    print(curried_add(1, 2)(3)(4))  # Output: 10
    print(curried_add(1, 2, 3, 4))  # Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- The time complexity of the curried function depends on the underlying function `func`.
- Each invocation of the curried function adds a layer of function calls, but the actual computation happens only when all arguments are provided.
- If `func` has a time complexity of O(f), the curried version will also have a time complexity of O(f).

Space Complexity:
- The space complexity is O(n), where `n` is the number of arguments passed so far. This is because the curried function stores the arguments in a tuple until all arguments are provided.

Overall, the space complexity is proportional to the number of arguments stored, and the time complexity is determined by the underlying function.
"""

# Topic: Functional Programming