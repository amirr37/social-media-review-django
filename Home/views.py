from django.shortcuts import render
from django.views import View


# Create your views here.


class index_page(View):
    def get(self, request):
        return render(request, 'Home/index.html')

    def post(self, request):
        return render(request, 'Home/index.html')
