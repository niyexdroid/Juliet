from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostModelForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView, 
    UpdateView,
    DeleteView
)

# Create your views here.
class PostListView(ListView):
    template_name = 'pages/page_list.html'
    queryset = Post.objects.all()

class PostDetailView(DetailView):
    template_name = 'pages/page_detail.html'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

class PostCreateView(CreateView):
    template_name = 'pages/page_create.html'
    form_class = PostModelForm
    queryset = Post.objects.all()

    # def form_valid(self, form) :
    #     print(form.cleaned_data)
    #     return super().form_valid(form)