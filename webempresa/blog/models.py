from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200,verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="categoría"
        verbose_name_plural="categorías"
        ordering=['-created']

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Título")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name="Categorías", related_name="get_posts")
    content = models.TextField(verbose_name="Contenido")
    image = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    published = models.DateTimeField(default=timezone.now(), verbose_name="Fecha de publicación")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")

    class Meta:
        verbose_name="entrada"
        verbose_name_plural="entradas"
        ordering=['-created']

    def __str__(self):
        return self.title