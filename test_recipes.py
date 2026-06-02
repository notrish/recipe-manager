import pytest

from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient_creation():
    ingredient = Ingredient("Sugar", 100, "g")

    assert ingredient.name == "Sugar"
    assert ingredient.quantity == 100
    assert ingredient.unit == "g"