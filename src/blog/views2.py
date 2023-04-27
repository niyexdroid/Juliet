from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArticleForm
from .models import Article
# Create your views here.


def article_detail_view(request, id):
    obj = Article.objects.get(id=id)
    context = {
        'object': obj
    }
    return render(request, "blog/article_detail.html", context)


def article_list_view(request):
    queryset = Article.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "blog/article_list.html", context)


def article_create_view(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, "blog/article_create.html", context)


def article_delete_view(request, id):
    obj = get_object_or_404(Article, id=id)

    if request.method == "POST":
        print(request.method)
        obj.delete()
        return redirect("blog:article-list")
    context = {
        'post': obj
    }
    return render(request, "blog/article_delete.html", context)
