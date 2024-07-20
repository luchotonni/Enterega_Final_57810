from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, ProductoForm, CategoriaForm, PerfilForm
from .models import Producto, Categoria
from .models import Perfil


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'tienda/registro.html', {'form': form})


def home(request):
    productos = Producto.objects.all()
    return render(request, 'tienda/home.html', {'productos': productos})


@login_required
def editar_perfil(request):
    user = request.user
    perfil, created = Perfil.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            return redirect('perfil')
    else:
        user_form = UserForm(instance=user)
        perfil_form = PerfilForm(instance=perfil)

    context = {
        'user_form': user_form,
        'perfil_form': perfil_form,
    }
    return render(request, 'editar_perfil.html', context)


@login_required
def crear_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm()
    return render(request, 'tienda/crear_producto.html', {'form': form})


@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoriaForm()
    return render(request, 'tienda/crear_categoria.html', {'form': form})


def ver_perfil(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)
    context = {
        'perfil': perfil,
    }
    return render(request, 'ver_perfil.html', context)
