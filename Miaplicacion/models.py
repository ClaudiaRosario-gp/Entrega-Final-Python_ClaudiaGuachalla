from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Autor(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_completo = models.CharField(max_length=100)
    biografia = models.TextField(blank=True)
    imagen = models.ImageField(upload_to='autores/', null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_completo


class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=200, blank=True)
    cuerpo = models.TextField()
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comentarios')
    nombre = models.CharField(max_length=100)
    cuerpo = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.nombre} en {self.blog.titulo}"


