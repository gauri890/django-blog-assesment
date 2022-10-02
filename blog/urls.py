from django.urls import path, include
from . import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('ckeditor/content/', include('ckeditor_uploader.urls')),
] +static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
