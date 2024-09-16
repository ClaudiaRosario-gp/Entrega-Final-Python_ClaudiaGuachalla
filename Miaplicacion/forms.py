from django import forms
from .models import Blog
from .models import Comentario
#from django.contrib.auth.forms import 
#from django.contrib.auth.models import U

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class': 'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
  
class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'cuerpo']
        widgets = {
            'cuerpo': forms.Textarea(attrs={'rows': 4}),
        }
