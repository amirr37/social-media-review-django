from django.urls import path

from Home import views

app_name = 'Home'
urlpatterns = [
    path('', views.index_page.as_view(), name='index-page'),
]
