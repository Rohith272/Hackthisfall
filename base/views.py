from django.db.models import Q
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import UserRegisterForm
from django.views.generic import (
    ListView,
)
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
