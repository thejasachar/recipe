from django.shortcuts import render, redirect
from .models import Recipe
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse  # Add this import for debugging
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm

@login_required
def recipes(request):
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('recipe_image')
        receipe_name = data.get('recipe_name')
        receipe_desc = data.get('recipe_desc')
        print(receipe_name)
        print(receipe_desc)
        print(receipe_image)
        Recipe.objects.create(
            recipe_image=receipe_image,
            recipe_name=receipe_name,
            recipe_desc=receipe_desc,
        )
        return redirect('/recipes/')  

    queryset = Recipe.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'recipe.html', context)

def update_recipe(request,id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('recipe_image')
        receipe_name = data.get('recipe_name')
        receipe_desc = data.get('recipe_desc')
        queryset.recipe_name=receipe_name
        queryset.recipe_desc=receipe_desc
        if receipe_image:
            queryset.recipe_image=receipe_image
        queryset.save()
        return redirect('/recipes/')
    context = {'recipe': queryset}
    return render(request, 'update_recipe.html', context)

def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes/')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/recipes/')
        else:
            form = AuthenticationForm(data=request.POST)  # Pass invalid form data
            messages.error(request, 'Invalid Username or Password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('/')

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'User created successfully. You can now login.')
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

