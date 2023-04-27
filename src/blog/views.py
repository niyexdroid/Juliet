from django.shortcuts import render, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)    
    # Create your views here.

class ArticleListView(ListView):
    template_name = 'blog/article_list.html'
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    template_name = 'blog/article_detail.html'
    # queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_) 

class ArticleCreateView(CreateView):
    template_name = 'blog/article_create.html'
    form_class = ArticleForm
    queryset = Article.objects.all()
    
    # def form_valid(self, form):
    #     print(form.cleaned_data)
    #     return super().form_valid(form)

