from django import forms
from .models import userPost

class postForm(forms.ModelForm):
    class Meta:
        model = userPost
        fields = '__all__'