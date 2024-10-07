from django.forms import ValidationError
from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_the_test(self):
        recipe = self.recipe
        ...

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
        # self.recipe.full_clean()  # Aqui a validacao ocorre (nao deixa passar da quantidade de caracteres definidas)
        # self.recipe.save()
        # self.fail(len(self.recipe.title))
