from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre de la categoria', max_length=50,null=False,blank=False)
    estado = models.BooleanField('categoria activada/categoria no activada',default=True)
    fecha_creacion = models.DateField('fecha de creacion', auto_now=False, auto_now_add=True)


    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.nombre

class Autor(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre de autor', max_length=150,null=False,blank=False)
    apellidos = models.CharField('apellidos de autor', max_length=150,null=False,blank=False)
    facebook = models.URLField('facebook', max_length=300,null=True,blank=True)
    twitter = models.URLField('twitter', max_length=300,null=True,blank=True)
    instagram = models.URLField('instagram', max_length=300,null=True,blank=True)
    web = models.URLField('web', max_length=300,null=True,blank=True)
    correo = models.EmailField('correo electronico', max_length=254,blank=False,null=False)
    estado = models.BooleanField('autor activo/autor no activo')
    fecha_creacion = models.DateField('fecha de creacion', auto_now=False, auto_now_add=True)


    class Meta:

        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'

    def __str__(self):
        return  "{0},{1}".format(self.apellidos,self.nombre)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField('Titulo', max_length=90,blank=False,null=False)
    slug = models.CharField('Slug', max_length=50,blank=False,null=False)
    descripcion = models.CharField('Descripcion', max_length=50,blank=False,null=False)
    contenido = RichTextField()
    imagen = models.URLField(max_length=255,blank=False,null=False)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField('Publicado/No Publicado',default=True)
    fecha_creacion = models.DateField('Fecha de Creacion', auto_now=False, auto_now_add=True)

    class Meta:

        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.titulo


