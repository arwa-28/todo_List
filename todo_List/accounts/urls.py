from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),

    # login + logout
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('logout/', LogoutView.as_view(next_page='welcome'), name='logout'),
    path('logout/', views.user_logout, name='logout'),

    # signup
    path('signup/', views.signup, name='signup'),
]
