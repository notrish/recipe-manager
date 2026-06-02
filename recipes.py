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
    pass


class ShoppingList:
    pass


class DietaryRecipe(Recipe):
    pass
