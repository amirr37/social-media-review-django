from django.urls import path
from Account import views

app_name = 'Account'
urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='register'),
    # path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('profile/<str:id>', views.UserProfileView.as_view(), name='profile'),
    path('password-reset/', views.UserPasswordResetView.as_view(), name='password-reset'),
    path('password-reset/done/', views.UserPasswordResetDoneView.as_view(), name='password-reset-done'),
    path('password-reset/confirm/<uidb64>/<token>/', views.UserPasswordResetConfirmView.as_view(),
         name='password-reset-confirm'),
]
