from django import forms
from .models import userPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class postForm(forms.ModelForm):
    class Meta:
        model = userPost
        fields = '__all__'
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control select-input'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'images': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            }    


class createAuthforms(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")  

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username is already taken.")
        return username          