from django.urls import reverse, resolve
from recipes import views
from recipes.models import Category, Recipe, User
from .test_recipe_base import RecipeTestBase
from unittest import skip


class RecipeDetailViewTest(RecipeTestBase):

    def test_recipe_detail_view_function_is_correct(self):
        view = resolve(reverse("recipes:recipe", kwargs={"id": 1}))
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1000}))
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_the_correct_recipes(self):
        needed_title = "this is a detail page - it loads one recipe"
        self.make_recipe(title=needed_title)
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": 1}))
        content = response.content.decode("utf-8")

        # check if one recipe exists
        self.assertIn(needed_title, content)

    def test_recipe_detail_template_dont_load_recipe_not_published(self):
        """test recipe test is_published false dont show"""
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:recipe", kwargs={"id": recipe.id}))
        self.assertEqual(response.status_code, 404)
