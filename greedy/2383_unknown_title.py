"""
LeetCode Problem #2383: Minimum Hours of Training to Win a Competition

Problem Statement:
You are preparing for a competition and are given two arrays: `energy` and `experience`, where:
- `energy[i]` and `experience[i]` represent the energy and experience of the i-th opponent, respectively.

You are also given two integers: `initialEnergy` and `initialExperience`, which represent your initial energy and experience.

To win against the i-th opponent:
1. Your energy must be strictly greater than `energy[i]`.
2. Your experience must be strictly greater than `experience[i]`.

After defeating an opponent:
- Your energy decreases by `energy[i]`.
- Your experience increases by `experience[i]`.

You can train to increase your initial energy and experience. Each hour of training increases either your energy or experience by 1.

Return the minimum number of training hours required to ensure you can defeat all opponents in order.

Constraints:
- `1 <= energy.length == experience.length <= 100`
- `1 <= energy[i], experience[i], initialEnergy, initialExperience <= 100`
"""

def minNumberOfHours(initialEnergy: int, initialExperience: int, energy: list[int], experience: list[int]) -> int:
    """
    Calculate the minimum number of training hours required to win against all opponents.
    """
    # Calculate the total energy required to defeat all opponents
    total_energy_required = sum(energy)
    # Calculate the additional energy needed to meet the requirement
    additional_energy = max(0, total_energy_required + 1 - initialEnergy)
    
    # Initialize the additional experience needed
    additional_experience = 0
    current_experience = initialExperience
    
    # Iterate through each opponent
    for exp in experience:
        # If current experience is not enough, calculate the additional experience needed
        if current_experience <= exp:
            additional_experience += (exp + 1 - current_experience)
            current_experience = exp + 1
        # Gain experience after defeating the opponent
        current_experience += exp
    
    # Total training hours is the sum of additional energy and experience needed
    return additional_energy + additional_experience

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    initialEnergy = 5
    initialExperience = 3
    energy = [1, 4, 3, 2]
    experience = [2, 6, 3, 1]
    print(minNumberOfHours(initialEnergy, initialExperience, energy, experience))  # Output: 8

    # Test Case 2
    initialEnergy = 2
    initialExperience = 4
    energy = [1]
    experience = [3]
    print(minNumberOfHours(initialEnergy, initialExperience, energy, experience))  # Output: 0

    # Test Case 3
    initialEnergy = 1
    initialExperience = 1
    energy = [1, 1, 1, 1]
    experience = [1, 1, 1, 50]
    print(minNumberOfHours(initialEnergy, initialExperience, energy, experience))  # Output: 51

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the total energy required takes O(n), where n is the length of the `energy` array.
- Iterating through the `experience` array also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy
"""