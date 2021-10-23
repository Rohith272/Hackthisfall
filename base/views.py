from django.shortcuts import render, redirect
from .models import *
from .forms import UserRegisterForm
from django.views.generic import (
    ListView,
)
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    Recipe = Recipe.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    )
    Recipe_count = Recipe.count()
    context = {'Recipe_count': Recipe_count,'Recipe':Recipe}
    return render(request, 'base/home.html', context)


class RecipeListviewevent(ListView):
    model = Recipe
    template_name = 'Recipe.html'
    context_object_name = 'Recipe'

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
    return render(request, 'user_register.html', {'form': form})
