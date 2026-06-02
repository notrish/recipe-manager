class Ingredient:
    def __init__(self, name, quantity, unit):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.name}: {self.quantity} {self.unit}"


class Recipe:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def get_ingredients(self):
        return self.ingredients


class ShoppingList:
    def __init__(self):
        self.items = []

    def add_recipe(self, recipe):
        for ingredient in recipe.get_ingredients():
            self.items.append(ingredient)

    def get_items(self):
        return self.items


class DietaryRecipe(Recipe):
    def __init__(self, name, diet_type):
        super().__init__(name)
        self.diet_type = diet_type
