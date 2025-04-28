"""
LeetCode Question #1472: Design Browser History

Problem Statement:
You are tasked with implementing a browser history system. You need to design a class `BrowserHistory` that simulates a browser's history functionality. The class should support the following operations:

1. `BrowserHistory(homepage: str)`: Initializes the object with the homepage of the browser.
2. `visit(url: str)`: Visits the given URL from the current page. It clears all forward history.
3. `back(steps: int) -> str`: Moves `steps` back in history. If you can only move `x` steps back, where `x < steps`, you move only `x` steps. Returns the current URL after moving back in history.
4. `forward(steps: int) -> str`: Moves `steps` forward in history. If you can only move `x` steps forward, where `x < steps`, you move only `x` steps. Returns the current URL after moving forward in history.

Constraints:
- `1 <= homepage.length, url.length <= 20`
- `1 <= steps <= 100`
- `homepage` and `url` consist of '.' or lowercase English letters.
- At most `5000` calls will be made to `visit`, `back`, and `forward`.

"""

# Solution
class BrowserHistory:
    def __init__(self, homepage: str):
        """
        Initializes the browser history with the homepage.
        """
        self.history = [homepage]  # List to store the history of URLs
        self.current_index = 0    # Pointer to the current URL in the history

    def visit(self, url: str) -> None:
        """
        Visits the given URL from the current page and clears forward history.
        """
        # Remove all forward history
        self.history = self.history[:self.current_index + 1]
        # Add the new URL to the history
        self.history.append(url)
        # Update the current index to the new URL
        self.current_index += 1

    def back(self, steps: int) -> str:
        """
        Moves 'steps' back in history. Returns the current URL after moving back.
        """
        # Move back by 'steps', but ensure we don't go out of bounds
        self.current_index = max(0, self.current_index - steps)
        return self.history[self.current_index]

    def forward(self, steps: int) -> str:
        """
        Moves 'steps' forward in history. Returns the current URL after moving forward.
        """
        # Move forward by 'steps', but ensure we don't go out of bounds
        self.current_index = min(len(self.history) - 1, self.current_index + steps)
        return self.history[self.current_index]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.visit("youtube.com")
    assert browser.back(1) == "facebook.com"  # Move back to facebook.com
    assert browser.back(1) == "google.com"    # Move back to google.com
    assert browser.forward(1) == "facebook.com"  # Move forward to facebook.com
    browser.visit("linkedin.com")  # Visit linkedin.com, clears forward history
    assert browser.forward(2) == "linkedin.com"  # No forward history, stays on linkedin.com
    assert browser.back(2) == "google.com"       # Move back to google.com
    assert browser.back(7) == "leetcode.com"     # Move back to homepage, can't go further back

    # Test Case 2
    browser = BrowserHistory("example.com")
    assert browser.back(1) == "example.com"  # No history to go back, stays on homepage
    browser.visit("page1.com")
    browser.visit("page2.com")
    assert browser.back(1) == "page1.com"    # Move back to page1.com
    assert browser.forward(1) == "page2.com" # Move forward to page2.com

    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `__init__`: O(1), initializing the history list and index.
   - `visit`: O(1) for appending a URL and clearing forward history.
   - `back`: O(1), as moving the index is a constant-time operation.
   - `forward`: O(1), as moving the index is a constant-time operation.
   Overall, each operation runs in O(1) time.

2. Space Complexity:
   - The space complexity is O(n), where `n` is the number of URLs stored in the history list.

Topic: Design, Data Structures
"""