from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# To use class based views use this module
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
import datetime
from .models import Post

# Create your views here.

# To show posts
class PostListView(ListView):
    model = Post
    # General naming convention used for templates when using ListView is -> <app>/<model>_<viewtype>.html
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    # This is used to order the blogs by date posted from newest to oldest. '-' means newest to oldest blog posts
    ordering = ['-date_posted']
    paginate_by = 4


# To show a particular users posts
class UserPostListView(ListView):
    model = Post
    # General naming convention used for templates when using ListView is -> <app>/<model>_<viewtype>.html
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    # This is used to order the blogs by date posted from newest to oldest. '-' means newest to oldest blog posts
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # Creating a method that checks if the form is valid. Form is valid only if any user is currently logged on.
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post Created Successfully.')
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # Creating a method that checks if the form is valid. Form is valid only if any user is currently logged on.
    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post Updated Successfully.')
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
