"""
LeetCode Problem #1797: Design Authentication Manager

Problem Statement:
An authentication manager is a system that manages user authentication tokens. For each session, a user receives a token that is valid for a certain period of time. The manager should be able to:
1. Generate a new token for a user with a given `tokenId` and set its expiration time.
2. Renew a token if it is still valid.
3. Count the number of unexpired tokens at any given time.

Implement the `AuthenticationManager` class:
- `AuthenticationManager(int timeToLive)`: Initializes the object with the `timeToLive` parameter, which represents the time (in seconds) a token is valid after being generated or renewed.
- `generate(string tokenId, int currentTime)`: Generates a new token with the given `tokenId` at the given `currentTime`.
- `renew(string tokenId, int currentTime)`: Renews the unexpired token with the given `tokenId` at the given `currentTime`. If the token is expired, the renewal request is ignored.
- `countUnexpiredTokens(int currentTime)`: Returns the number of tokens that are unexpired at the given `currentTime`.

Constraints:
- `1 <= timeToLive <= 10^4`
- `1 <= tokenId.length <= 5`
- `tokenId` consists only of lowercase letters.
- `1 <= currentTime <= 10^8`
- All calls to `generate`, `renew`, and `countUnexpiredTokens` will be made in non-decreasing order of `currentTime`.
- The total number of calls to all functions will not exceed `2 * 10^4`.

"""

from collections import OrderedDict

class AuthenticationManager:
    def __init__(self, timeToLive: int):
        """
        Initialize the AuthenticationManager with a given timeToLive.
        """
        self.timeToLive = timeToLive
        self.tokens = OrderedDict()  # Stores tokenId -> expirationTime

    def generate(self, tokenId: str, currentTime: int) -> None:
        """
        Generate a new token with the given tokenId and set its expiration time.
        """
        self.tokens[tokenId] = currentTime + self.timeToLive

    def renew(self, tokenId: str, currentTime: int) -> None:
        """
        Renew the token if it is still valid. Ignore if the token is expired.
        """
        if tokenId in self.tokens and self.tokens[tokenId] > currentTime:
            self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        """
        Count the number of unexpired tokens at the given currentTime.
        """
        # Remove expired tokens
        expired_tokens = [token for token, expiry in self.tokens.items() if expiry <= currentTime]
        for token in expired_tokens:
            del self.tokens[token]
        
        return len(self.tokens)


# Example Test Cases
if __name__ == "__main__":
    # Initialize the AuthenticationManager with a timeToLive of 5 seconds
    auth_manager = AuthenticationManager(5)

    # Generate a token with ID "token1" at time 1
    auth_manager.generate("token1", 1)

    # Count unexpired tokens at time 2 (should return 1)
    print(auth_manager.countUnexpiredTokens(2))  # Output: 1

    # Renew "token1" at time 6 (should have no effect since it is expired)
    auth_manager.renew("token1", 6)

    # Count unexpired tokens at time 6 (should return 0)
    print(auth_manager.countUnexpiredTokens(6))  # Output: 0

    # Generate a new token with ID "token2" at time 10
    auth_manager.generate("token2", 10)

    # Count unexpired tokens at time 15 (should return 1)
    print(auth_manager.countUnexpiredTokens(15))  # Output: 1

    # Renew "token2" at time 12 (should extend its expiration to 17)
    auth_manager.renew("token2", 12)

    # Count unexpired tokens at time 16 (should return 1)
    print(auth_manager.countUnexpiredTokens(16))  # Output: 1

    # Count unexpired tokens at time 18 (should return 0 since "token2" is expired)
    print(auth_manager.countUnexpiredTokens(18))  # Output: 0


"""
Time and Space Complexity Analysis:

1. `generate`:
   - Time Complexity: O(1) (insertion into an OrderedDict is O(1) on average).
   - Space Complexity: O(1) (only a single token is added).

2. `renew`:
   - Time Complexity: O(1) (lookup and update in an OrderedDict is O(1) on average).
   - Space Complexity: O(1) (no additional space is used).

3. `countUnexpiredTokens`:
   - Time Complexity: O(n), where n is the number of tokens in the OrderedDict. This is because we iterate through the tokens to remove expired ones.
   - Space Complexity: O(1) (no additional space is used apart from the list of expired tokens, which is temporary).

Overall:
- Time Complexity: O(n) for `countUnexpiredTokens`, O(1) for `generate` and `renew`.
- Space Complexity: O(n), where n is the number of tokens stored in the OrderedDict.

Topic: Design, Hash Table
"""