"""
LeetCode Problem #1772: Sort Features by Popularity

Problem Statement:
You are given a list of strings `features` and a list of strings `responses` where each string in `responses` is a single user response containing space-separated words. The `features` list contains the names of features that users could mention in their responses.

Your task is to sort the `features` list by their popularity in the `responses`. The popularity of a feature is defined as the number of unique responses in which the feature is mentioned. If two features have the same popularity, they should be sorted in the order they appear in the `features` list.

Return the sorted list of features.

Constraints:
- 1 <= len(features) <= 10^4
- 1 <= len(responses) <= 10^3
- 1 <= len(features[i]) <= 10
- 1 <= len(responses[i]) <= 10^3
- All strings in `features` and `responses` consist of lowercase English letters.
- All the values in `features` are unique.
"""

from collections import defaultdict

def sortFeatures(features, responses):
    """
    Sorts the features by their popularity in the responses.

    :param features: List[str] - List of feature names.
    :param responses: List[str] - List of user responses.
    :return: List[str] - Sorted list of features by popularity.
    """
    # Step 1: Count the number of unique responses mentioning each feature
    feature_count = defaultdict(int)
    for response in responses:
        # Use a set to ensure we only count unique mentions in a single response
        mentioned_features = set(response.split())
        for feature in features:
            if feature in mentioned_features:
                feature_count[feature] += 1

    # Step 2: Sort the features by popularity and then by their original order
    sorted_features = sorted(features, key=lambda x: (-feature_count[x], features.index(x)))

    return sorted_features

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    features = ["cooler", "lock", "touch"]
    responses = ["i like cooler cooler", "lock touch cool", "locker like touch"]
    print(sortFeatures(features, responses))  # Output: ["touch", "cooler", "lock"]

    # Test Case 2
    features = ["a", "b", "c"]
    responses = ["a b c", "a b", "a"]
    print(sortFeatures(features, responses))  # Output: ["a", "b", "c"]

    # Test Case 3
    features = ["feature1", "feature2", "feature3"]
    responses = ["feature1 feature2", "feature2 feature3", "feature1 feature3"]
    print(sortFeatures(features, responses))  # Output: ["feature1", "feature2", "feature3"]

"""
Time Complexity Analysis:
1. Splitting each response into words and creating a set takes O(L), where L is the average length of a response.
   Since there are `len(responses)` responses, this step takes O(len(responses) * L).
2. For each feature, we check if it exists in the set of words for each response. This takes O(len(features) * len(responses)).
3. Sorting the features takes O(len(features) * log(len(features))).

Overall Time Complexity: O(len(responses) * L + len(features) * len(responses) + len(features) * log(len(features)))

Space Complexity Analysis:
1. The `feature_count` dictionary stores counts for each feature, which takes O(len(features)).
2. The set of words for each response takes O(L) space, but this is reused for each response.

Overall Space Complexity: O(len(features) + L)

Topic: Strings, Sorting, Hash Table
"""