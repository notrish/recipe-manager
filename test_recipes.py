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

def test_recipe_creation():
    recipe = Recipe("Pancakes")

    assert recipe.name == "Pancakes"
    assert recipe.ingredients == []


def test_recipe_add_ingredient():
    recipe = Recipe("Pancakes")
    ingredient = Ingredient("Flour", 200, "g")

    recipe.add_ingredient(ingredient)

    assert recipe.get_ingredients() == [ingredient]


def test_shopping_list_creation():
    shopping_list = ShoppingList()

    assert shopping_list.items == []


def test_shopping_list_add_recipe():
    recipe = Recipe("Pancakes")
    ingredient = Ingredient("Flour", 200, "g")
    recipe.add_ingredient(ingredient)

    shopping_list = ShoppingList()
    shopping_list.add_recipe(recipe)

    assert shopping_list.get_items() == [ingredient]