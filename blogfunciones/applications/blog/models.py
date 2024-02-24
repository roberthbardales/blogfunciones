from django.db import models

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




