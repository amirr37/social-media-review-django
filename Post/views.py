from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify
from django.views import View
from django.contrib import messages

from Post.forms import PostCreateUpdateForm
from Post.models import Post


class PostDetailView(View):
    def get(self, request, id, slug):
        # post = Post.objects.get(pk=id)
        post = get_object_or_404(Post, id=id)
        return render(request, 'Post/post_detail.html', {'post': post})


class PostDeleteView(LoginRequiredMixin, View):
    """we dont delete posts, we just dis active them"""

    def get(self, request, id):
        # post = Post.objects.get(pk=id)
        post = get_object_or_404(Post, id=id)
        if request.user.id == post.author.id:
            post.is_active = False
            post.save()
            messages.success(request, 'Post has been deleted')
            return redirect('Home:index-page')
        messages.warning(request, 'You are not allowed to delete this post')

        return redirect('Post:post-detail', id=id, slug=post.slug)


class PostUpdateView(LoginRequiredMixin, View):
    form_class = PostCreateUpdateForm
    template_name = 'Post/post_update.html'

    def setup(self, request, *args, **kwargs):
        # self.post_instance = Post.objects.get(pk=kwargs.get('id'))
        self.post_instance = get_object_or_404(Post, id=kwargs.get('id'))
        return super().setup(request, *args, **kwargs)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.id == self.post_instance.author.id:
            messages.warning(request, 'You are not allowed to edit this post')
            return redirect('Home:index-page')
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=self.post_instance)
        return render(request, 'Post/post_update.html', {'form': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST, instance=self.post_instance)

        if form.is_valid():
            updated_post = form.save(commit=False)
            updated_post.slug = slugify(form.cleaned_data['title'])
            updated_post.save()

            messages.success(request, 'Post has been updated')
            return redirect('Post:post-detail', id=self.post_instance.id, slug=self.post_instance.slug)

        messages.error(request, "form is invalid")
        return redirect('Post:post-detail', id=self.post_instance.id, slug=self.post_instance.slug)


class PostCreateView(LoginRequiredMixin, View):
    template_name = 'Post/post_create.html'
    form_class = PostCreateUpdateForm

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': self.form_class()})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.slug = slugify(form.cleaned_data['title'])
            post.save()

            messages.success(request, 'Post has been created')
            return redirect('Post:post-detail', id=post.id, slug=post.slug)
        messages.error(request, "form is invalid")
        return render(request, self.template_name, {'form': form})
