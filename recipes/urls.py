from django.urls import path
from . import (
    views,
)  # quando se quer importar um  arquivo irmao, ou seja que esta na mesma pasta, basta coocar um . e importar o que se quer.


urlpatterns = [
    path("", views.home),
    path("recipes/<int:id>/", views.recipe),
]
