from django.urls import path
from . import views
app_name = 'blog'
urlpatterns = [
    path('', views.blog_home_page, name='blog_home_page'),
    path('blog', views.blog_listing, name='blog_listing'),
    path('blog_detail', views.blog_detail, name='blog_detail'),
]
