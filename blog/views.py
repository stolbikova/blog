from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.views import View


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        # post.published_date = timezone.now()
        post.save()
        return redirect('post_detail', pk=post.pk)


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment_to_post.html'

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return redirect('post_detail', pk=post.pk)


class CommentApproveView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        comment.approve()
        return redirect('post_detail', pk=comment.post.pk)


class CommentRemoveView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs['pk'])
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)


class DeletePostView(LoginRequiredMixin, View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_confirm_delete.html', {'post': post})
