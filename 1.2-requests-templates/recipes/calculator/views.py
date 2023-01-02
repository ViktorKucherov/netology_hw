from django.http import HttpResponse
from django.shortcuts import render
import copy

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'sandwich': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


# Create your views here.

def getServingsData(number: int) -> dict:
    result_DATA = copy.deepcopy(DATA)
    for recipe in result_DATA.values():
        for ingridient, count in recipe.items():
            recipe[ingridient] = count * number
    return result_DATA


def index(request, recipe):
    template = "calculator/index.html"
    servings = int(request.GET.get('servings', 1))
    data = getServingsData(servings)

    context = {
        'recipe': data[recipe]
    }

    return render(request=request,
                  template_name=template,
                  context=context)



