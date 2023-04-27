
from django.urls import path
from .views import (
    # dynamic_lookup_view,
    ArticleListView,
    ArticleDetailView,
    ArticleCreateView,
    
)  
app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:id>/', ArticleDetailView.as_view(), name='article-detail'),
    path('create/', ArticleCreateView.as_view(), name='article-create'),
#     path('<int:id>/', article_detail_view, name='article-detail'),
#     path('<int:id>/delete', article_delete_view, name='article-delete'),
# 
]

