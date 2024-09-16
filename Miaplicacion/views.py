from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from .models import Blog, Comentario
from .forms import ComentarioForm

def index(request):
    return render(request, 'Miaplicacion/index.html')  

class BlogListView(ListView):
    model = Blog
    template_name = 'Miaplicacion/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'Miaplicacion/blog_detail.html'
    
    
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    comentarios = blog.comentarios.all()
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.blog = blog
            comentario.save()
            return redirect('blog_detail', pk=blog.pk)
    else:
        form = ComentarioForm()
    return render(request, 'blog_detail.html', {
        'blog': blog,
        'comentarios': comentarios,
        'form': form
    })

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

