from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from Post.models import Post


class PostDetailView(View):
    def get(self, request, id, slug):
        post = Post.objects.get(pk=id)
        return render(request, 'Post/post_detail.html', {'post': post})


class PostDeleteView(LoginRequiredMixin, View):
    """we dont delete posts, we just dis active them"""

    def get(self, request, id):
        post = Post.objects.get(pk=id)
        if request.user.id == post.author.id:
            post.is_active = False
            post.save()
            messages.success(request, 'Post has been deleted')
            return redirect('Home:index-page')
        messages.warning(request, 'You are not allowed to delete this post')

        return redirect('Post:post-detail' , id=id, slug=post.slug)
