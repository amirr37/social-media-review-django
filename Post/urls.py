from django.urls import path
from Post import views

app_name = 'Post'
urlpatterns = [
    path('post/<int:id>/<slug:slug>', views.PostDetailView.as_view(), name='post-detail'),
    path('post-delete/<int:id>/', views.PostDeleteView.as_view(), name='post-delete'),

    path('post-update/<int:id>', views.PostUpdateView.as_view(), name='post-update'),
    path('post-create/', views.PostCreateView.as_view(), name='post-create'),
]
