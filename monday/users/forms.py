from django import forms 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User



class SignInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Type username')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Type password')
    
    class Meta:
        model = User
        fields=['username','password']

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), label='Create username')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Create password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input'}), label='Repeat password')
    class Meta:
        model = User
        fields=['username','password1', 'password2']