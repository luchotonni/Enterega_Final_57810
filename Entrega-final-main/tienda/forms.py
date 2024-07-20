from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto, Categoria, Perfil, Orden
from .models import Perfil


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar']
