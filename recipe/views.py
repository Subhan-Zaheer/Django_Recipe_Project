from django.shortcuts import render, redirect
from recipe.models import recipe, my_user
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def recipes(request):
    if request.user.is_authenticated:
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
    return redirect('/login/')


@login_required(login_url='/login/')
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
            if my_recipe_image == None:
                print(f"if my recipe image is none.")
                my_recipe_image = my_recipe.recipe_image
            my_recipe.recipe_image = my_recipe_image
        except KeyError as e:
            my_recipe.recipe_image = None
            print(f" Except part My recipe image contains : {my_recipe_image}")
            print(e)
        print(f"My recipe image contains : {my_recipe_image}")
        my_recipe.save()
        return redirect('/recipe')
    data = {
        'recipe':my_recipe
    }
    return render(request, 'update_recipe.html', data)


@login_required(login_url='/login/')
def delete_recipe(request, id):
    recipe.objects.filter(id = id).delete()
    return redirect('/recipe')




def login_page(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = user_name).exists():
            messages.error(request, "Invalid UserName or UserName doesnot exist.")
            return redirect('/login/')
        elif authenticate(username= user_name, password= password) is None:
            messages.error(request, "Invalid Password or Username.")
            return redirect('/login/')
        else:
            
            user = authenticate(username= user_name, password= password)
            print("User is authentic.")
            login(request, user=user)
            return redirect('/recipe/')
    return render(request, 'login.html')



def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=user_name)
        if user.exists():
            messages.info(request, "UserName already taken. Try with different UserName.")
            return redirect('/register/')
            pass
        user = User.objects.create(username= user_name, first_name= firstname, last_name = lastname)
        print(password)
        user.set_password(password)
        user.save()
        my_model_user = my_user.objects.create(first_name = firstname, last_name=lastname, user_name=user_name, password=password)
        my_model_user.save()
        return redirect('/login/')
    return render(request, 'register.html')