from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import *
from django.views.generic import (
    ListView,
)
import random

def home(request):
    return render(request, 'base/sign.html')

def user_home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    recipe = Recipe.objects.raw('SELECT name FROM base_recipe' + 
    'WHERE name LIKE %'+q+'% OR step LIKE %'+q+'% GROUP BY recipe_id')
    Recipe_count = recipe.count()
    context = {'Recipe_count': Recipe_count,'Recipe':recipe}
    return render(request, 'base/home.html', context)

def play_recipe(request):
    recipe_id = request.GET.get('recipe_id')
    recipe = Recipe.objects.raw('SELECT * FROM base_recipe WHERE recipe_id = '+ recipe_id + 'ORDER BY step_no');
    context = {'Recipe':recipe}
    return render(request, 'base/Recipe.html', context)

class RecipeListviewevent(ListView):
    model = Recipe
    template_name = 'Recipe.html'
    context_object_name = 'Recipe'

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # messages.success(request, f'Account created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm ()
    return render(request, 'base/sign.html', {'form': form})

def post_recipe(request):
    if request.method == 'POST':
        form = RecipePostForm(request.POST)
        name = form.cleaned_data['name']
        step_no = []
        step = []
        time = []
        i = 0
        recipe_id = random.randint()
        user=request.user

        while(1):
            if(form.cleaned_data['step_no'+str(i)]):
                step_no.append(form.cleaned_data['step_no'+str(i)])
                step.append(form.cleaned_data['step_no'+str(i)])
                time.append(form.cleaned_data['step_no'+str(i)])
            else:
                break
        
        for i in step_no:
            form = RecipePostForm(recipe_id, name, step_no[i], step[i], time[i])
            r = form.save(commit=False)
            r.user = user
            r.save()
        
            
        return redirect('base/home.html')
    else:
        form = RecipePostForm()
    return render(request, 'base/post_recipe.html', {'form': form})