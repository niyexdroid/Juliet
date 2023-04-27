from django.urls import path
from .views import (
    # dynamic_lookup_view,
    PostListView,
    PostDetailView,
    PostCreateView,

)
app_name = 'pages'
urlpatterns = [
    path('', PostListView.as_view(), name='post-list'),
    path('<int:id>/', PostDetailView.as_view(), name='post-detail'),
    path('create/', PostCreateView.as_view(), name='post-create'),
] 