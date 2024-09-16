from django import forms

from Post.models import Post


class PostCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        # todo : add field tag (M2M) in updateForm


