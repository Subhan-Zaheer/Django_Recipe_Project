from django.shortcuts import render
from recipe.models import recipe

# Create your views here.

def recipes(request):
    if request.method == 'POST':
        print(request.POST)
        my_recipe_name = request.POST.get('recipe_name')
        my_recipe_description = request.POST.get('recipe_desc')
        my_recipe_image = request.FILES['recipe_image']
        print(f'{my_recipe_name}, {my_recipe_description}, {my_recipe_image}')
        recipe_obj = recipe(recipe_name = my_recipe_name, recipe_desc= my_recipe_description, 
                            recipe_image = my_recipe_image)
        recipe_obj.save()
        pass
    return render(request, 'recipe.html')