from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields
from base.models import Recipe

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']

class RecipePostForm(forms.Form):
    name = forms.CharField(max_length=50)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        steps = Recipe.objects.filter(
            profile=self.instance
        )
        for i in range(len(steps) + 1):
            self.fields['step_no'+str(i)] = forms.IntegerField(required=False)
            self.fields['step_'+str(i)] = forms.Textarea(required=False)
            self.fields['time_'+str(i)] = forms.Textarea(required=False)

    def __init__(self, recipe_id, name, step_no, step, time, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['recipe_id'] = name
        self.fields['name'] = recipe_id
        self.fields['step_no'] = step_no
        self.fields['step'] = step
        self.fields['time'] = time

