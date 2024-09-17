from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Blog, Comentario
from .forms import ComentarioForm
from django.views.generic.edit import FormMixin

def index(request):
    return render(request, 'Miaplicacion/index.html')  

class BlogListView(ListView):
    model = Blog
    template_name = 'Miaplicacion/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5
def get_queryset(self):
        return Blog.objects.all().order_by('-fecha')  # Ordenar por fecha

from django.views.generic.edit import FormMixin

class BlogDetailView(FormMixin, DetailView):
    model = Blog
    template_name = 'Miaplicacion/blog_detail.html'
    form_class = ComentarioForm

    def get_success_url(self):
        return reverse_lazy('blog_detail', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comentarios'] = Comentario.objects.filter(blog=self.object)
        context['form'] = self.get_form()  # Para manejar el formulario en el template
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()

        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.blog = self.object
            comentario.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
   
    
def guardar_comentario(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        cuerpo = request.POST.get('cuerpo')
        Comentario.objects.create(blog=blog, nombre=nombre, cuerpo=cuerpo)
        return redirect('blog_detail', pk=pk)


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name = 'Miaplicacion/blog_form.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class BlogEditView(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'Miaplicacion/blog_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('blog_list')  

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'Miaplicacion/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

class AboutView(TemplateView):
    template_name = 'Miaplicacion/about.html'

