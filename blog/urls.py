from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('', BlogCreateView.as_view(), name='blog_create'),
    path('blog/create', BlogListView.as_view(), name='blog_list'),
    path('blog/detail/<int:pk>', BlogDetailView.as_view(), name='blog_view'),
    path('blog/update/<int:pk>', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', BlogDeleteView.as_view(), name='blog_delete'),
]
