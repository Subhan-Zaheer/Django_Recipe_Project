from django.shortcuts import render, redirect
from recipe.models import recipe
from django.contrib.auth.models import User

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
        return redirect('/recipe')
    recipe_obj = recipe.objects.all()
    if request.method == 'GET':
        if request.GET.get('search'):
            recipe_obj = recipe.objects.filter(recipe_name__icontains = request.GET.get('search'))
            data = {
                'recipes':recipe_obj
            }
            return render(request, 'recipe.html', data) 
    
    recipes = recipe.objects.all()
    data = {'recipes':recipes}    
    return render(request, 'recipe.html', data)

def update_recipe(request, id):
    my_recipe = recipe.objects.get(id = id)
    print(my_recipe.id, my_recipe.recipe_name, my_recipe.recipe_image)
    if request.method == 'POST':
        print(request.POST)
        my_recipe_name = request.POST.get('recipe_name')
        my_recipe.recipe_name = my_recipe_name
        my_recipe_description = request.POST.get('recipe_desc')
        my_recipe.recipe_desc = my_recipe_description
        try:
            my_recipe_image = request.FILES.get('recipe_image')
            my_recipe.recipe_image = my_recipe_image
        except KeyError as e:
            my_recipe.recipe_image = None
            print(f" Except part My recipe image contains : {my_recipe_image}")
            print(e)
        print(f"My recipe image contains : {my_recipe_image}")
        if my_recipe_image == None:
            print(f"if my recipe image is none.")
            my_recipe_image = my_recipe.recipe_image
        my_recipe.save()
        return redirect('/recipe')
    data = {
        'recipe':my_recipe
    }
    return render(request, 'update_recipe.html', data)

def delete_recipe(request, id):
    recipe.objects.filter(id = id).delete()
    return redirect('/recipe')


def login_page(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.create(username= user_name, first_name= firstname, last_name = lastname)
        print(password)
        user.set_password(password)
        user.save()
        return redirect('/login/')
    return render(request, 'register.html')