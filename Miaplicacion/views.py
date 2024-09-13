from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, TemplateView
from .models import Blog
from django.views.generic import UpdateView

class BlogEditView(UpdateView):
    model = Blog
    template_name = 'miaplicacion/blog_form.html'
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    success_url = reverse_lazy('blog_list')


def index(request):
    return render(request, 'index.html')


class BlogListView(ListView):
    model = Blog
    template_name = 'miaplicacion/blog_list.html'
    context_object_name = 'blogs'
    paginate_by = 5
    

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'miaplicacion/blog_detail.html'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen']
    template_name = 'miaplicacion/blog_form.html'
    success_url = reverse_lazy('blog_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    template_name = 'miaplicacion/blog_confirm_delete.html'
    success_url = reverse_lazy('blog_list')

class AboutView(TemplateView):
    template_name = 'miaplicacion/about.html'

