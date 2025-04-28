"""
LeetCode Question #2115: Find All Possible Recipes from Given Supplies

Problem Statement:
You have information about `n` different recipes. You are given a string array `recipes` and a 2D string array `ingredients`. The `i-th` recipe has the name `recipes[i]`, and you can create it if you have all the needed ingredients from `ingredients[i]`. You are also given a string array `supplies` containing all the ingredients that you initially have, and you can use them to create new recipes.

Return a list of all the recipes that you can create. You may return the answer in any order.

Note that you can only create a recipe if you have all the ingredients to create it, and you can use the supplies you have at any time to create new recipes. You cannot reuse the ingredients that you create to create other recipes.

Constraints:
- `n == recipes.length == ingredients.length`
- `1 <= n <= 100`
- `1 <= ingredients[i].length, supplies.length <= 100`
- `1 <= recipes[i].length, ingredients[i][j].length, supplies[k].length <= 10`
- `recipes[i], ingredients[i][j]`, and `supplies[k]` consist only of lowercase English letters.
- All the values of `recipes` and `supplies` combined are unique.
- Each `ingredients[i]` does not contain any duplicate values.

"""

from collections import defaultdict, deque

def findAllRecipes(recipes, ingredients, supplies):
    """
    Find all possible recipes that can be created given the initial supplies and recipe dependencies.

    :param recipes: List[str] - List of recipe names.
    :param ingredients: List[List[str]] - List of ingredient lists for each recipe.
    :param supplies: List[str] - List of initial supplies available.
    :return: List[str] - List of recipes that can be created.
    """
    # Build a graph and in-degree map
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Initialize the graph and in-degree map
    for recipe, ingredient_list in zip(recipes, ingredients):
        in_degree[recipe] = len(ingredient_list)
        for ingredient in ingredient_list:
            graph[ingredient].append(recipe)
    
    # Start with the initial supplies
    queue = deque(supplies)
    result = []
    
    # Process the queue
    while queue:
        current = queue.popleft()
        
        # If the current item is a recipe, add it to the result
        if current in recipes:
            result.append(current)
        
        # Reduce the in-degree of dependent recipes
        for dependent_recipe in graph[current]:
            in_degree[dependent_recipe] -= 1
            if in_degree[dependent_recipe] == 0:
                queue.append(dependent_recipe)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    recipes = ["bread", "sandwich"]
    ingredients = [["flour", "water"], ["bread", "meat"]]
    supplies = ["flour", "water", "meat"]
    print(findAllRecipes(recipes, ingredients, supplies))  # Output: ["bread", "sandwich"]

    # Test Case 2
    recipes = ["bread", "sandwich", "salad"]
    ingredients = [["flour", "water"], ["bread", "meat"], ["lettuce", "tomato"]]
    supplies = ["flour", "water", "meat", "lettuce", "tomato"]
    print(findAllRecipes(recipes, ingredients, supplies))  # Output: ["bread", "sandwich", "salad"]

    # Test Case 3
    recipes = ["cake", "pie"]
    ingredients = [["flour", "sugar"], ["flour", "butter"]]
    supplies = ["flour", "sugar"]
    print(findAllRecipes(recipes, ingredients, supplies))  # Output: ["cake"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the graph and in-degree map takes O(n * k), where `n` is the number of recipes and `k` is the average number of ingredients per recipe.
- Processing the queue takes O(n + m), where `m` is the total number of edges in the graph (dependencies between supplies and recipes).
- Overall, the time complexity is O(n * k + n + m).

Space Complexity:
- The graph and in-degree map use O(n + m) space.
- The queue and result list use O(n) space.
- Overall, the space complexity is O(n + m).

Topic: Graphs, Topological Sort
"""