from django import forms
from . models import CarModel, Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        fields = '__all__'
        # exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','comment']