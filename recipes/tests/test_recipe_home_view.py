from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase


class RecipeHomeViewTest(RecipeTestBase):

    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse("recipes:home"))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse("recipes:home"))
        self.assertTemplateUsed(response, "recipes/pages/home.html")

    def test_recipe_home_template_shows_no_recipes_found_if_no_recipes(self):
        # Recipe.objects.get(pk=1).delete()
        response = self.client.get(reverse("recipes:home"))
        self.assertIn("No recipes found here", response.content.decode("utf-8"))
        ########################
        # self.fail("Preciso fazer algo para que este teste funcione corretame")

    def test_recipe_home_template_dont_loads_recipes_not_published(self):
        """test recipe test is_published false dont show"""
        self.make_recipe(is_published=False)
        response = self.client.get(reverse("recipes:home"))
        self.assertIn("No recipes found here", response.content.decode("utf-8"))

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe(
            author_data={"first_name": "joao"}, category_data={"name": "cafe"}
        )
        response = self.client.get(reverse("recipes:home"))
        content = response.content.decode("utf-8")
        response_context_recipes = response.context["recipes"]

        self.assertIn("Recipe Title", content)
        self.assertIn("10 Minutes", content)
        self.assertIn("5   Persons", content)
        self.assertIn("joao", content)
        self.assertIn("cafe", content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_recipe_home_is_paginated(self):
        for i in range(18):
            kwargs = {"author_data": {"username": f"u{i}"}, "slug": f"r{i}"}
            self.make_recipe(**kwargs)
            response = self.client.get(reverse("recipes:home"))
            recipes = response.context["recipes"]
            paginator = recipes.paginator
            self.assertEqual(paginator.num_pages, 2)
