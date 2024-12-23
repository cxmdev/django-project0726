from django.urls import path
from . import (
    views,
)  # quando se quer importar um  arquivo irmao, ou seja que esta na mesma pasta, basta coocar um .  e importar o que se quer.

app_name = "recipes"

urlpatterns = [
    path("", views.home, name="home"),
    path("recipes/search/", views.search, name="search"),
    path("recipes/category/<int:category_id>/", views.category, name="category"),
    path("recipes/<int:id>/", views.recipe, name="recipe"),
]
