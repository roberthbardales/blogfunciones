from django.shortcuts import render
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator



# Create your views here.

from .models import Post,Autor,Categoria

def home(request):
    queryset=request.GET.get("buscar")
    print(f"la consulta es: {queryset}")
    post=Post.objects.filter(estado=True)
    if queryset:
        post=Post.objects.filter(
            Q(titulo__icontains=queryset) |
            Q(descripcion__icontains=queryset)
        ).distinct()

    contexto={'contexto_post':post}

    paginator=Paginator(post,2)
    page=request.GET.get('page')
    post=Paginator

    return render(request,'index.html',contexto)


def detallePost(request,slug):
    try:
        post=Post.objects.get(
            slug=slug
            )
        contexto={'detalle_post':post}
        return render(request,'post.html',contexto)
    except Post.DoesNotExist:
        raise Http404


def generales(request):
    post=Post.objects.filter(
        estado=True,
        categoria=Categoria.objects.get(nombre__iexact='General')
        )
    contexto={'contexto_post':post}
    return render(request,'generales.html',contexto)

def programacion(request):
    post=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact='Programacion')
    )
    contexto={'contexto_post':post}
    return render(request,'programacion.html',contexto)

def tutoriales(request):
    post=Post.objects.filter(
    estado=True,
    categoria=Categoria.objects.get(nombre__iexact='Tutorial')
    )
    contexto={'contexto_post':post}
    return render(request,'tutoriales.html',contexto)



