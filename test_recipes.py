import pytest

from recipes import Ingredient, Recipe, ShoppingList, DietaryRecipe

def test_ingredient_creation():
    ingredient = Ingredient("Sugar", 100, "g")

    assert ingredient.name == "Sugar"
    assert ingredient.quantity == 100
    assert ingredient.unit == "g"

def test_ingredient_str():
    ingredient = Ingredient("Sugar", 100, "g")

    assert str(ingredient) == "Sugar: 100 g"


def test_ingredient_invalid_quantity():
    with pytest.raises(ValueError):
        Ingredient("Sugar", 0, "g")