from django.shortcuts import render, get_list_or_404
from utils.recipes.factory import make_recipe
from recipes.models import Recipe


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by("-id")
    return render(
        request,
        "recipes/pages/home.html",
        context={
            "recipes": recipes,
        },
    )


def category(request, category_id):
<<<<<<< HEAD
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
    ).order_by("-id")
=======
    recipes = get_list_or_404(
        Recipe.objects.filter(category__id=category_id, is_published=True).order_by(
            "-id"
        )
    )
>>>>>>> cba365020fb0655bc322791b681ac627d3f60991
    return render(
        request,
        "recipes/pages/category.html",
        context={
            "recipes": recipes,
<<<<<<< HEAD
=======
            "title": f"{recipes[0].category.name} - Category",
>>>>>>> cba365020fb0655bc322791b681ac627d3f60991
        },
    )


def recipe(request, id):
    return render(
        request,
        "recipes/pages/recipe-view.html",
        context={"recipe": make_recipe(), "is_detail_page": True},
    )
