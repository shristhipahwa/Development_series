from django.shortcuts import render
from .models import Post
from django.views.generic import (
                ListView,
                DetailView,
                CreateView,
                UpdateView,
                DeleteView
                )
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# This is a function based ,self created blog view
# But there are class based views build by django that provides greater functionality
# with mininmal coding and also save us a lot of headache

def blog(request):
    context = {
    'posts' : Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'posts' #variable we are looping on in templates
    ordering = ['-date_posted'] #'-'indicates reverse ordering


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detailview.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    # template_name = 'blog/post_form.html' #since we have followed the default convention by naming the html == post_form.html no need to asign it.
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    # template_name = 'blog/post_.html' default convention followed
    success_url = "/blog"
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
