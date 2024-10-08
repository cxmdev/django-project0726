from django.forms import ValidationError
from .test_recipe_base import RecipeTestBase
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    # def test_the_test(self):
    #     recipe = self.recipe
    #     ...

    # def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
    # self.recipe.title = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    # with self.assertRaises(ValidationError):
    #     self.recipe.full_clean()
    # self.recipe.full_clean()  # Aqui a validacao ocorre (nao deixa passar da quantidade de caracteres definidas)
    # self.recipe.save()
    # self.fail(len(self.recipe.title))

    @parameterized.expand(
        [
            ("title", 65),
            ("description", 765),
            ("preparation_time_unit", 65),
            ("servings_unit", 65),
        ]
    )
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, "A" * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
