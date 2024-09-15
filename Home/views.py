from django.shortcuts import render
from django.views import View
from Post.models import Post


# Create your views here.


class index_page(View):

    def get(self, request):
        posts = Post.objects.filter(is_active=True)

        return render(request, 'Home/index.html', {'posts': posts})
